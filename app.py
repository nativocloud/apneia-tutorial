"""Tutorial sobre Apneia Obstrutiva do Sono — entry point Streamlit.

Para correr localmente:
    uv run streamlit run app.py
"""

import streamlit as st

from components.ui import init_session_state, injetar_css_global, progress_tracker
from modulos import (
    glossario_pagina,
    m00_introducao,
    m01_anatomia,
    m02_sono,
    m03_saos,
    m04_diagnostico,
    m05_tratamentos,
    m06_plano_cirurgico,
    m07_prevencao,
    m08_pos_operatorio,
)

st.set_page_config(
    page_title="Apneia do Sono — Tutorial",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": (
            "Tutorial educativo sobre cirurgia multinível para SAOS. "
            "Apoiado em literatura científica recente (Antunes et al. 2023)."
        ),
    },
)

# Mapeamento (label do menu, módulo, ID interno)
MODULOS = [
    ("0. Comece aqui", m00_introducao, "m00_intro"),
    ("1. Anatomia das vias aéreas", m01_anatomia, "m01_anatomia"),
    ("2. Como dormimos", m02_sono, "m02_sono"),
    ("3. O que é a SAOS", m03_saos, "m03_saos"),
    ("4. Diagnóstico", m04_diagnostico, "m04_diagnostico"),
    ("5. Tratamentos disponíveis", m05_tratamentos, "m05_tratamentos"),
    ("6. O seu plano cirúrgico", m06_plano_cirurgico, "m06_plano"),
    ("7. Prevenção e estilo de vida", m07_prevencao, "m07_prevencao"),
    ("8. Pós-operatório", m08_pos_operatorio, "m08_pos_op"),
]

REFERENCIA = [
    ("📖 Glossário completo", glossario_pagina, "glossario"),
]


def render_sidebar() -> tuple:
    with st.sidebar:
        st.markdown(
            """
            <div style="padding:1rem 0 0.5rem 0;">
              <div style="font-family:'Outfit',sans-serif;font-size:1.4rem;
                          font-weight:600;color:#252728;letter-spacing:-0.01em;">
                🌙 Apneia do Sono
              </div>
              <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.85rem;
                          color:#73787A;font-weight:400;margin-top:0.2rem;">
                Tutorial educativo
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown(
            '<div style="font-size:0.75rem;font-weight:600;color:#475569;'
            'text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.5rem;">'
            "Módulos"
            "</div>",
            unsafe_allow_html=True,
        )

        labels_modulos = [m[0] for m in MODULOS]
        labels_ref = [r[0] for r in REFERENCIA]
        opcoes = labels_modulos + labels_ref

        # Suportar navegação programática (botões Anterior/Próximo)
        nav_target = st.session_state.pop("nav_target", None)
        if nav_target and nav_target in opcoes:
            st.session_state["sidebar_radio"] = nav_target

        escolhido = st.radio(
            "Módulo",
            options=opcoes,
            key="sidebar_radio",
            label_visibility="collapsed",
        )

        st.divider()

        # Progresso
        concluidos = st.session_state.get("modulos_concluidos", set())
        progress_tracker(concluidos=len(concluidos), total=9)

        st.divider()

        with st.expander("📚 Fontes (papers)"):
            st.markdown(
                """
                **Estudos clínicos**
                - **Antunes J, Órfão J, Rito J, Adónis C, Freire F.** (2023).
                  *Surgical treatment for OSA: effect on sleep architecture.*
                  Eur Arch Otorhinolaryngol 280:5059-5065.
                  [DOI](https://doi.org/10.1007/s00405-023-08093-8)
                - **Kim SW.** (2026). *REM-OSA.* Curr Sleep Med Rep 12:8.
                - **Krüger M et al.** (2026). *Smoking and OSA.* Sci Rep 16:13382.
                - **Hartenbaum NP.** (2026). *OSA in Commercial Trucking.*
                  Curr Sleep Med Rep 12:19.

                **Guidelines clínicas**
                - **AASM** *Clinical Practice Guidelines* (2023).
                - **ICSD-3-TR** (AASM 2023).
                - **FIPAT** *Terminologia Anatomica* 2.ª ed. (2019).
                """
            )

        with st.expander("🖼️ Fontes das imagens"):
            st.markdown(
                """
                - **OpenStax College.** *Anatomy & Physiology* (2022).
                  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
                - **NIH SeniorHealth / NHLBI.** Domínio público.
                - **Wikimedia Commons** — diagramas auxiliares.

                Animações geradas localmente em SVG.
                """
            )

        with st.expander("ℹ️ Sobre"):
            st.markdown(
                """
                Tutorial educativo sobre **cirurgia multinível para SAOS**
                (Síndrome de Apneia Obstrutiva do Sono).

                Apoia a decisão informada de pacientes em pré-operatório.

                **Não substitui consulta médica.** Decisões clínicas devem
                ser tomadas com a equipa cirúrgica de otorrinolaringologia.
                """
            )

    return escolhido


def main() -> None:
    init_session_state()
    injetar_css_global()

    escolhido_label = render_sidebar()

    # Encontrar módulo correspondente em MODULOS ou REFERENCIA
    todos = MODULOS + REFERENCIA
    modulo, modulo_id = next(
        (m, mid) for label, m, mid in todos if label == escolhido_label
    )
    st.session_state["modulo_atual_id"] = modulo_id

    modulo.render()


if __name__ == "__main__":
    main()
