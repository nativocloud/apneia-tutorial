"""Módulo 0 — Dashboard inicial. Página de aterragem do tutorial."""

import streamlit as st

from components.navegacao import ORDEM_MODULOS, breadcrumb, metadata
from components.ui import (
    callout,
    hero,
    progress_tracker,
    secao_titulo,
)


def _proximo_modulo_recomendado(concluidos: set[str]) -> dict:
    """Devolve o primeiro módulo não concluído na ordem (ou m00_intro)."""
    for m in ORDEM_MODULOS[1:]:  # saltar o próprio M0
        if m["id"] not in concluidos:
            return m
    return ORDEM_MODULOS[1]


def render() -> None:
    breadcrumb("m00_intro", "Comece aqui")

    concluidos = st.session_state.get("modulos_concluidos", set())
    total = len(ORDEM_MODULOS)
    n_concluidos = len(concluidos)
    pct = int(n_concluidos / total * 100) if total else 0
    proximo = _proximo_modulo_recomendado(concluidos)
    tempo_total_min = sum(m["tempo_min"] for m in ORDEM_MODULOS)

    hero(
        eyebrow="Tutorial educativo · Apneia obstrutiva do sono",
        titulo="Entenda a SAOS, a cirurgia multinível, e como prevenir.",
        subtitulo=(
            "9 módulos para passar de zero a paciente informado. "
            "Apoiado em literatura científica recente: Antunes et al. 2023, "
            "Kim 2026, Krüger 2026 e Hartenbaum 2026."
        ),
        stats=[
            (str(total), "módulos"),
            ("4", "papers científicos"),
            (f"~{tempo_total_min} min", "duração total"),
        ],
    )

    # ─── Continuar de onde parei (se aplicável) ───────────────────────
    if n_concluidos > 0:
        secao_titulo(
            eyebrow="Bom regresso",
            titulo=f"Continuar de onde parou ({n_concluidos}/{total})",
        )
        st.markdown(
            f"""
<div style="background:white;border:2px solid #00D3C8;border-radius:16px;
            padding:1.5rem 1.75rem;margin-bottom:1rem;
            font-family:'IBM Plex Sans',sans-serif;">
  <div style="font-size:11px;font-weight:500;color:#0EAA9F;
              text-transform:uppercase;letter-spacing:0.18em;">
    Próximo módulo recomendado
  </div>
  <h3 style="font-family:'Outfit',sans-serif;font-weight:600;
             color:#252728;margin:0.4rem 0;font-size:1.4rem;">
    {proximo['icone']} {proximo['titulo']}
  </h3>
  <div style="color:#3E4244;font-size:0.95rem;">
    {proximo['descricao']} · ⏱️ {proximo['tempo_min']} min
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if st.button(
                f"Continuar para {proximo['icone']} {proximo['titulo']} →",
                type="primary",
                use_container_width=True,
                key="cta_continuar",
            ):
                st.session_state["nav_target"] = proximo["label"]
                st.rerun()
    else:
        secao_titulo(
            eyebrow="Pronto a começar",
            titulo="Como funciona este tutorial",
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                """
<div style="text-align:center;padding:1rem;font-family:'IBM Plex Sans',sans-serif;">
  <div style="font-size:2rem;margin-bottom:0.5rem;">📚</div>
  <div style="font-family:'Outfit',sans-serif;font-weight:600;color:#252728;">
    Sequencial
  </div>
  <div style="font-size:0.875rem;color:#73787A;margin-top:0.25rem;">
    9 módulos numa ordem pensada
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                """
<div style="text-align:center;padding:1rem;font-family:'IBM Plex Sans',sans-serif;">
  <div style="font-size:2rem;margin-bottom:0.5rem;">🎯</div>
  <div style="font-family:'Outfit',sans-serif;font-weight:600;color:#252728;">
    Objetivos claros
  </div>
  <div style="font-size:0.875rem;color:#73787A;margin-top:0.25rem;">
    Cada módulo abre com objetivos
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                """
<div style="text-align:center;padding:1rem;font-family:'IBM Plex Sans',sans-serif;">
  <div style="font-size:2rem;margin-bottom:0.5rem;">🧠</div>
  <div style="font-family:'Outfit',sans-serif;font-weight:600;color:#252728;">
    Quiz por módulo
  </div>
  <div style="font-size:0.875rem;color:#73787A;margin-top:0.25rem;">
    Verifica a compreensão
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )

    # ─── Progresso global ─────────────────────────────────────────────
    progress_tracker(concluidos=n_concluidos, total=total)

    # ─── Mapa do tutorial ─────────────────────────────────────────────
    secao_titulo(
        eyebrow="Mapa do tutorial",
        titulo="9 módulos · ~75 minutos no total",
        subtitulo="Cada módulo prepara o seguinte. Pode seguir a ordem ou saltar.",
    )

    # Cards clicáveis em grelha 3 colunas
    cols_per_row = 3
    for row_start in range(0, len(ORDEM_MODULOS), cols_per_row):
        cols = st.columns(cols_per_row)
        for col_idx, m in enumerate(ORDEM_MODULOS[row_start:row_start + cols_per_row]):
            with cols[col_idx]:
                idx_global = row_start + col_idx
                concluido = m["id"] in concluidos
                badge = "✓ Concluído" if concluido else f"⏱ {m['tempo_min']} min"
                cor_borda = "#0EAA9F" if concluido else "#E2E4E6"
                cor_fundo = "#E6FAF8" if concluido else "white"
                st.markdown(
                    f"""
<div style="background:{cor_fundo};border:1px solid {cor_borda};
            border-radius:12px;padding:1rem 1.1rem;height:100%;
            font-family:'IBM Plex Sans',sans-serif;margin-bottom:0.5rem;">
  <div style="display:flex;justify-content:space-between;align-items:center;
              margin-bottom:0.3rem;">
    <div style="font-size:11px;font-weight:500;color:#0EAA9F;
                text-transform:uppercase;letter-spacing:0.18em;">
      Módulo {idx_global}
    </div>
    <div style="font-size:11px;color:#73787A;">{badge}</div>
  </div>
  <div style="font-size:1.5rem;line-height:1;margin:0.3rem 0;">
    {m['icone']}
  </div>
  <div style="font-family:'Outfit',sans-serif;font-weight:600;
              color:#252728;font-size:1rem;line-height:1.2;
              margin-bottom:0.3rem;">
    {m['titulo']}
  </div>
  <div style="font-size:0.825rem;color:#3E4244;line-height:1.5;
              margin-bottom:0.5rem;">
    {m['descricao']}
  </div>
</div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(
                    "Abrir →" if not concluido else "Rever →",
                    key=f"card_btn_{m['id']}",
                    use_container_width=True,
                ):
                    st.session_state["nav_target"] = m["label"]
                    st.rerun()

    # ─── O que é a SAOS — em uma frase ──────────────────────────────
    secao_titulo(
        eyebrow="Em uma frase",
        titulo="O que é a apneia obstrutiva do sono",
    )

    st.markdown(
        """
> A **via aérea superior** (o tubo por onde o ar passa do nariz aos pulmões)
> **fecha-se sozinha durante o sono**, dezenas de vezes por noite, e isto
> **estraga o sono** sem o paciente se aperceber.

Cada vez que fecha, falta ar. O cérebro acorda **brevemente** — sem o paciente
se lembrar — para reabrir a via aérea, depois volta a dormir, depois fecha
outra vez. Resultado: **passa a noite inteira a "lutar"** em vez de descansar.
        """
    )

    callout(
        tipo="info",
        icone="💡",
        titulo="Analogia rápida",
        corpo=(
            "Imagine uma <strong>palhinha</strong>. Se a apertar suavemente, "
            "ainda passa líquido. Se apertar mais, fecha. A sua garganta, "
            "durante o sono, comporta-se como essa palhinha — os músculos "
            "que a mantêm aberta relaxam, e em algumas pessoas relaxam tanto "
            "que a via aérea <strong>colapsa</strong>."
        ),
    )

    # ─── Aviso ético ─────────────────────────────────────────────────
    callout(
        tipo="aviso",
        titulo="Aviso importante",
        corpo=(
            "Este tutorial é <strong>educativo</strong>, não substitui a "
            "consulta médica. As decisões clínicas devem ser tomadas com a "
            "sua equipa cirúrgica de otorrinolaringologia, com base no caso "
            "individual de cada paciente."
        ),
    )

    # ─── CTA final ───────────────────────────────────────────────────
    if n_concluidos == 0:
        secao_titulo(
            titulo="Pronto para começar?",
            subtitulo="Comece pelo Módulo 1 — Anatomia. ~8 minutos.",
        )
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if st.button(
                "🫁 Iniciar Módulo 1 — Anatomia →",
                type="primary",
                use_container_width=True,
                key="cta_iniciar",
            ):
                st.session_state["nav_target"] = "1. Anatomia das vias aéreas"
                st.rerun()
