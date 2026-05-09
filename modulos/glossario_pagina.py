"""Página de glossário completo — acessível pelo sidebar."""

import streamlit as st

from components.glossario import GLOSSARIO, pagina_glossario_completa
from components.navegacao import breadcrumb
from components.ui import hero, secao_titulo


def render() -> None:
    breadcrumb("glossario", "Glossário")

    hero(
        eyebrow="Referência · Glossário",
        titulo="Glossário de termos médicos",
        subtitulo=(
            "Todos os termos usados no tutorial, organizados por categoria. "
            "Pesquise abaixo ou navegue pelas tabs."
        ),
    )

    secao_titulo(
        eyebrow="Pesquisar",
        titulo="Encontrar um termo",
    )

    pesquisa = st.text_input(
        "Pesquisar termo",
        placeholder="ex.: cornetos, AHI, palatoplastia...",
        label_visibility="collapsed",
    )

    if pesquisa:
        pesquisa_lower = pesquisa.lower().strip()
        resultados = [
            t for t in GLOSSARIO.values()
            if (
                pesquisa_lower in t.nome.lower()
                or pesquisa_lower in t.definicao.lower()
                or pesquisa_lower in (t.detalhe or "").lower()
                or any(pesquisa_lower in s.lower() for s in (t.sinonimos or []))
            )
        ]

        if resultados:
            st.caption(
                f"**{len(resultados)}** termos encontrados para *{pesquisa}*"
            )
            for t in resultados:
                with st.container(border=True):
                    st.markdown(
                        f"<span style='display:inline-block;background:#dbeafe;"
                        f"color:#1e40af;padding:0.15rem 0.5rem;border-radius:4px;"
                        f"font-size:0.7rem;font-weight:600;'>{t.categoria}</span> "
                        f"**{t.nome}**",
                        unsafe_allow_html=True,
                    )
                    st.markdown(t.definicao)
                    if t.detalhe:
                        with st.expander("Detalhe"):
                            st.markdown(t.detalhe)
        else:
            st.info(
                f"Nenhum termo encontrado para *{pesquisa}*. "
                f"Tente outra palavra ou navegue por categoria."
            )
        return

    secao_titulo(
        eyebrow="Por categoria",
        titulo="Anatomia · Cirurgia · Diagnóstico · Tratamento · Sono",
    )

    pagina_glossario_completa()
