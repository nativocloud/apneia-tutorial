"""Validação clínica do tutorial via MedLM (Google Cloud Vertex AI).

Lê os ficheiros em conteudo_validacao/mXX_*.md e envia cada módulo para o
modelo MedLM, guardando o relatório em conteudo_validacao/relatorios/.

Pré-requisitos:
1. Projeto GCP com Vertex AI ativado:
   gcloud services enable aiplatform.googleapis.com
2. Acesso aprovado ao MedLM (formulário Google, requer organização):
   https://cloud.google.com/vertex-ai/docs/generative-ai/medlm/medlm-overview
3. Autenticação:
   gcloud auth application-default login
4. Variáveis de ambiente:
   export GCP_PROJECT_ID=seu-projeto
   export GCP_REGION=us-central1   # MedLM disponível em us-central1

Uso:
    uv run python scripts/validar_com_medlm.py             # todos os módulos
    uv run python scripts/validar_com_medlm.py m06         # só um módulo
    uv run python scripts/validar_com_medlm.py --modelo medlm-medium  # mais barato

Custo estimado: $0.03-0.10 por módulo com medlm-large.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTEUDO_DIR = ROOT / "conteudo_validacao"
RELATORIOS_DIR = CONTEUDO_DIR / "relatorios"

PROMPT_SISTEMA = """Você é um revisor clínico sénior em Otorrinolaringologia e \
Medicina do Sono, com formação em comunicação médica para pacientes. Vai \
rever um módulo de um tutorial educativo destinado a um paciente adulto \
(49 anos, sem formação médica) que se vai submeter a cirurgia multinível \
da via aérea superior para SAOS.

CONTEXTO CLÍNICO DO PACIENTE
- Cirurgia agendada: 13/04/2026, Hospital da Luz – Oeiras
- Cirurgiã: Dra. Maria Cristina de Almeida Adónis
- Procedimentos: septoplastia + microcirurgia endonasal + turbinectomia \
bilateral + palatoplastia para roncopatia + amigdalectomia por Sluder
- Paper-âncora: Antunes, Órfão, Rito, Adónis, Freire (2023). Surgical \
treatment for OSA: effect on sleep architecture. Eur Arch Otorhinolaryngol \
280:5059-5065. DOI: 10.1007/s00405-023-08093-8

TAREFA
Reveja o conteúdo do módulo abaixo nos 8 eixos:
1. PRECISÃO CIENTÍFICA — erros factuais, mecanismos errados.
2. ATUALIDADE — vs guidelines AASM 2023, ICSD-3-TR 2023.
3. NOMENCLATURA — Terminologia Anatómica FIPAT 2019.
4. LINGUAGEM — acessível sem ser infantil; jargão explicado.
5. RISCO DE MAL-ENTENDIDO — frases que possam levar o paciente a \
subestimar/sobreestimar tratamento.
6. COMPLETUDE — tópicos críticos em falta.
7. ÉTICA — limites do educativo vs prescritivo.
8. ALINHAMENTO COM PAPER ANTUNES 2023 — citações e dados corretos.

FORMATO DE RESPOSTA (Markdown estruturado):
Para cada eixo:
- Estado: 🟢 OK / 🟡 Pontos de melhoria / 🔴 Erro crítico
- Lista numerada de issues (citação exata + problema + sugestão concreta)

NO FINAL:
- Pontuação global (0-100) de qualidade clínica
- Top 3 prioridades de correção
- Recomendação: APROVAR / APROVAR COM CORREÇÕES / REFAZER"""


def chamar_medlm(prompt: str, modelo: str, projeto: str, regiao: str) -> str:
    """Chama o modelo MedLM via Vertex AI.

    MedLM usa a API de PaLM (text-bison style), não Gemini.
    """
    try:
        import vertexai
        from vertexai.language_models import TextGenerationModel
    except ImportError:
        raise SystemExit(
            "Falta google-cloud-aiplatform. Instale: uv add google-cloud-aiplatform"
        )

    vertexai.init(project=projeto, location=regiao)

    try:
        model = TextGenerationModel.from_pretrained(modelo)
    except Exception as e:
        if "PERMISSION_DENIED" in str(e) or "not found" in str(e).lower():
            raise SystemExit(
                f"\n❌ Sem acesso ao modelo '{modelo}'.\n"
                f"   MedLM requer aprovação prévia do Google Cloud.\n"
                f"   1. Solicite acesso: https://cloud.google.com/vertex-ai/docs/generative-ai/medlm/overview\n"
                f"   2. Alternativa imediata: use 'gemini-1.5-pro' (sem aprovação especial)\n"
                f"      uv run python scripts/validar_com_medlm.py --modelo gemini-1.5-pro\n"
            )
        raise

    response = model.predict(
        prompt,
        max_output_tokens=2048,
        temperature=0.2,  # baixo — queremos consistência clínica
        top_k=40,
        top_p=0.8,
    )
    return response.text


def chamar_gemini(prompt: str, modelo: str, projeto: str, regiao: str) -> str:
    """Fallback: usa Gemini Pro (não fine-tuned em medicina, mas capaz)."""
    try:
        import vertexai
        from vertexai.generative_models import GenerativeModel
    except ImportError:
        raise SystemExit("Falta google-cloud-aiplatform.")

    vertexai.init(project=projeto, location=regiao)
    model = GenerativeModel(modelo)
    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0.2, "max_output_tokens": 4096},
    )
    return response.text


def validar_modulo(
    caminho_md: Path,
    modelo: str,
    projeto: str,
    regiao: str,
) -> str:
    """Carrega o módulo, monta o prompt completo e chama o modelo."""
    conteudo = caminho_md.read_text(encoding="utf-8")
    prompt_completo = (
        f"{PROMPT_SISTEMA}\n\n"
        f"{'=' * 70}\n"
        f"CONTEÚDO DO MÓDULO A REVER:\n"
        f"{'=' * 70}\n\n"
        f"{conteudo}"
    )

    if modelo.startswith("medlm"):
        return chamar_medlm(prompt_completo, modelo, projeto, regiao)
    else:
        return chamar_gemini(prompt_completo, modelo, projeto, regiao)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "modulo",
        nargs="?",
        default=None,
        help="Prefixo do módulo a validar (ex.: m06). Se omitido, valida todos.",
    )
    parser.add_argument(
        "--modelo",
        default="medlm-large",
        help="Modelo: medlm-large (default), medlm-medium, gemini-1.5-pro, gemini-2.0-pro-exp",
    )
    parser.add_argument(
        "--projeto",
        default=os.environ.get("GCP_PROJECT_ID"),
        help="Projeto GCP (ou env GCP_PROJECT_ID)",
    )
    parser.add_argument(
        "--regiao",
        default=os.environ.get("GCP_REGION", "us-central1"),
        help="Região GCP (default us-central1, onde MedLM está disponível)",
    )
    args = parser.parse_args()

    if not args.projeto:
        print(
            "❌ GCP_PROJECT_ID não definido. Use --projeto ou:\n"
            "   export GCP_PROJECT_ID=seu-projeto",
            file=sys.stderr,
        )
        sys.exit(1)

    if not CONTEUDO_DIR.exists():
        print(
            "❌ Pasta conteudo_validacao/ não existe. Corra primeiro:\n"
            "   uv run python scripts/exportar_para_validacao.py",
            file=sys.stderr,
        )
        sys.exit(1)

    RELATORIOS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    if args.modulo:
        ficheiros = list(CONTEUDO_DIR.glob(f"{args.modulo}*.md"))
    else:
        ficheiros = sorted(
            f for f in CONTEUDO_DIR.glob("m*.md") if not f.stem.startswith("_")
        )

    if not ficheiros:
        print(f"❌ Sem ficheiros a validar (filtro: {args.modulo or 'todos'})")
        sys.exit(1)

    print(f"🩺 Validando {len(ficheiros)} módulo(s) com {args.modelo}")
    print(f"   Projeto: {args.projeto} · Região: {args.regiao}\n")

    for f in ficheiros:
        print(f"→ {f.name} ... ", end="", flush=True)
        try:
            relatorio = validar_modulo(f, args.modelo, args.projeto, args.regiao)
            out = RELATORIOS_DIR / f"{f.stem}_validacao_{args.modelo}_{timestamp}.md"
            cabecalho = (
                f"# Validação clínica — {f.stem}\n"
                f"**Modelo:** {args.modelo}\n"
                f"**Data:** {datetime.now().isoformat(timespec='seconds')}\n"
                f"**Projeto GCP:** {args.projeto}\n\n"
                f"---\n\n"
            )
            out.write_text(cabecalho + relatorio, encoding="utf-8")
            print(f"✓ {out.relative_to(ROOT)}")
        except Exception as e:
            print(f"✗ ERRO: {e}")

    print(f"\n📋 Relatórios em {RELATORIOS_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
