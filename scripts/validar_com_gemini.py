"""Validação clínica do tutorial via Gemini API (Google AI Studio).

Mais simples que MedLM: requer apenas API key gratuita, sem aprovação GCP.

Setup (uma vez):
1. Obter API key: https://aistudio.google.com/apikey
2. Exportar: export GEMINI_API_KEY="sua-chave"

Uso:
    uv run python scripts/validar_com_gemini.py            # todos os módulos
    uv run python scripts/validar_com_gemini.py m06        # só um módulo
    uv run python scripts/validar_com_gemini.py --modelo gemini-2.5-pro  # mais capaz
    uv run python scripts/validar_com_gemini.py --consolidado  # tutorial todo de uma vez

Modelos disponíveis (sem aprovação especial):
- gemini-2.5-pro       → mais capaz, contexto 2M, lento
- gemini-2.0-flash     → rápido, contexto 1M, default
- gemini-1.5-pro       → estável, contexto 2M
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
- Lista numerada de issues encontradas (citação exata + problema + sugestão concreta)

NO FINAL:
- Pontuação global (0-100) de qualidade clínica
- Top 3 prioridades de correção
- Recomendação final: APROVAR / APROVAR COM CORREÇÕES / REFAZER

Responda em português europeu. Seja específico e cite frases exatas. \
Não invente referências bibliográficas.
"""


def chamar_gemini(prompt: str, modelo: str, api_key: str) -> str:
    """Chama Gemini via google-genai SDK (Google AI Studio)."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=modelo,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            top_p=0.9,
            max_output_tokens=8192,
        ),
    )
    return response.text or "(resposta vazia)"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "modulo",
        nargs="?",
        default=None,
        help="Prefixo do módulo (ex.: m06). Omitir para validar todos.",
    )
    parser.add_argument(
        "--modelo",
        default="gemini-2.5-pro",
        help="Modelo Gemini (default: gemini-2.5-pro)",
    )
    parser.add_argument(
        "--consolidado",
        action="store_true",
        help="Valida tutorial_completo.md de uma vez só (visão global)",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("GEMINI_API_KEY"),
        help="API key (ou env GEMINI_API_KEY)",
    )
    args = parser.parse_args()

    if not args.api_key:
        print(
            "❌ GEMINI_API_KEY não definida.\n"
            "   1. Obtenha em: https://aistudio.google.com/apikey\n"
            "   2. Exporte:    export GEMINI_API_KEY='sua-chave'",
            file=sys.stderr,
        )
        sys.exit(1)

    if not CONTEUDO_DIR.exists():
        print(
            "❌ conteudo_validacao/ não existe. Corra primeiro:\n"
            "   uv run python scripts/exportar_para_validacao.py",
            file=sys.stderr,
        )
        sys.exit(1)

    RELATORIOS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    if args.consolidado:
        ficheiros = [CONTEUDO_DIR / "tutorial_completo.md"]
    elif args.modulo:
        ficheiros = list(CONTEUDO_DIR.glob(f"{args.modulo}*.md"))
    else:
        ficheiros = sorted(
            f for f in CONTEUDO_DIR.glob("m*.md") if not f.stem.startswith("_")
        )

    if not ficheiros:
        print(f"❌ Sem ficheiros (filtro: {args.modulo or 'todos'})")
        sys.exit(1)

    print(f"🩺 A validar {len(ficheiros)} ficheiro(s) com {args.modelo}\n")

    for f in ficheiros:
        print(f"→ {f.name} ... ", end="", flush=True)
        try:
            conteudo = f.read_text(encoding="utf-8")
            prompt = (
                f"{PROMPT_SISTEMA}\n\n"
                f"{'=' * 70}\nCONTEÚDO A REVER:\n{'=' * 70}\n\n{conteudo}"
            )
            relatorio = chamar_gemini(prompt, args.modelo, args.api_key)

            out = RELATORIOS_DIR / f"{f.stem}_validacao_{args.modelo}_{timestamp}.md"
            cabecalho = (
                f"# Validação clínica — {f.stem}\n"
                f"**Modelo:** {args.modelo}\n"
                f"**Data:** {datetime.now().isoformat(timespec='seconds')}\n\n"
                f"---\n\n"
            )
            out.write_text(cabecalho + relatorio, encoding="utf-8")
            print(f"✓ {out.relative_to(ROOT)}")
        except Exception as e:
            print(f"✗ ERRO: {type(e).__name__}: {e}")

    print(f"\n📋 Relatórios em {RELATORIOS_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
