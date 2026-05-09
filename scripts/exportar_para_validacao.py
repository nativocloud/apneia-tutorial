"""Exporta o conteúdo dos módulos como texto plano para validação clínica externa.

Uso:
    uv run python scripts/exportar_para_validacao.py

Gera ficheiros em conteudo_validacao/, um por módulo, prontos para colar
num modelo médico (MedLM, Gemini Pro, Med-Gemini) com o prompt de validação.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULOS_DIR = ROOT / "modulos"
OUTPUT_DIR = ROOT / "conteudo_validacao"

# Padrão para extrair strings de hero(), secao_titulo(), st.markdown(), callout()
RE_TRIPLE_QUOTED = re.compile(r'"""(.*?)"""', re.DOTALL)
RE_KW_STRING = re.compile(
    r'(titulo|subtitulo|eyebrow|corpo|enunciado|explicacao|definicao|detalhe|nome)='
    r'(?:\(\s*)?[\'"](.*?)[\'"](?:\s*\))?',
    re.DOTALL,
)
RE_MD = re.compile(r'st\.markdown\(\s*"""(.+?)"""', re.DOTALL)
RE_CAPTION = re.compile(r'st\.caption\(\s*[\'"](.+?)[\'"]', re.DOTALL)


def limpar_texto(texto: str) -> str:
    # Remove marcas markdown que confundem a leitura
    texto = re.sub(r"\*\*(.+?)\*\*", r"\1", texto)
    texto = re.sub(r"\*(.+?)\*", r"\1", texto)
    texto = re.sub(r"^[ \t]+", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def extrair_conteudo_modulo(caminho: Path) -> str:
    fonte = caminho.read_text(encoding="utf-8")

    # Remove imports e definições de funções
    fonte_sem_imports = re.sub(
        r"^(from|import)\s.*$", "", fonte, flags=re.MULTILINE
    )

    blocos_texto: list[str] = []

    for m in RE_MD.finditer(fonte_sem_imports):
        blocos_texto.append(m.group(1))

    for m in RE_KW_STRING.finditer(fonte_sem_imports):
        blocos_texto.append(f"[{m.group(1)}] {m.group(2)}")

    for m in RE_CAPTION.finditer(fonte_sem_imports):
        blocos_texto.append(f"[caption] {m.group(1)}")

    return "\n\n".join(limpar_texto(b) for b in blocos_texto)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    modulos = sorted(MODULOS_DIR.glob("m*.py"))
    todos = []

    for caminho in modulos:
        if caminho.name == "__init__.py":
            continue
        nome = caminho.stem
        conteudo = extrair_conteudo_modulo(caminho)
        if not conteudo.strip():
            continue

        cabecalho = (
            f"# Módulo a validar: {nome}\n"
            f"# Ficheiro fonte: modulos/{caminho.name}\n"
            f"# Tutorial: Apneia Obstrutiva do Sono — paciente pré-cirurgia\n"
            f"# Equipa: Dra. Maria Cristina Adónis, Hospital da Luz – Oeiras\n"
            f"# Paper-âncora: Antunes et al. 2023, Eur Arch Otorhinolaryngol\n"
            f"\n{'=' * 70}\n\n"
        )
        texto_completo = cabecalho + conteudo

        out = OUTPUT_DIR / f"{nome}.md"
        out.write_text(texto_completo, encoding="utf-8")
        todos.append(texto_completo)
        print(f"✓ {out.relative_to(ROOT)} ({len(conteudo)} chars)")

    # Versão consolidada com todos os módulos
    consolidado = OUTPUT_DIR / "tutorial_completo.md"
    consolidado.write_text("\n\n\n".join(todos), encoding="utf-8")
    print(f"\n📋 Consolidado: {consolidado.relative_to(ROOT)}")
    print(f"   {sum(len(t) for t in todos):,} caracteres total")
    print(f"\nPara validar, abra cada ficheiro e cole no modelo médico após o prompt de validação.")


if __name__ == "__main__":
    main()
