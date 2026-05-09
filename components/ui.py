"""Componentes UI alinhados com o Native Stride Design System.

Fonte: Native Stride Brand Book (Oct 2024) + colors_and_type.css.
Paleta: turquesa #00D3C8 + grey #3E4244 + blue-dark #080119 + white.
Tipografia: Outfit (display) + IBM Plex Sans (body).
"""

from typing import Literal

import streamlit as st


PALETA = {
    "turquesa": "#00D3C8",
    "turquesa_light": "#2CF4E5",
    "turquesa_dark": "#0EAA9F",
    "turquesa_soft": "#E6FAF8",
    "orange": "#FF8D10",
    "orange_dark": "#D86D03",
    "grey": "#3E4244",
    "grey_light": "#73787A",
    "grey_dark": "#252728",
    "white": "#FFFFFF",
    "blue_dark": "#080119",
    "bg_subtle": "#F5F6F7",
    "line": "#E2E4E6",
}


def injetar_css_global() -> None:
    """CSS global Native Stride — tipografia, paleta, espaçamento, motion."""
    st.markdown(
        """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0&family=Material+Icons" rel="stylesheet">

<style>
:root {
  /* Native Stride Design System — Brand Book Oct 2024 */
  --ns-turquoise: #00D3C8;
  --ns-turquoise-light: #2CF4E5;
  --ns-turquoise-dark: #0EAA9F;
  --ns-turquoise-soft: #E6FAF8;
  --ns-orange: #FF8D10;
  --ns-orange-dark: #D86D03;
  --ns-grey: #3E4244;
  --ns-grey-light: #73787A;
  --ns-grey-dark: #252728;
  --ns-blue-dark: #080119;
  --ns-bg-subtle: #F5F6F7;
  --ns-line: #E2E4E6;

  --grad-hero: linear-gradient(135deg, #080119 0%, #0EAA9F 85%, #00D3C8 100%);
  --grad-turquoise: linear-gradient(135deg, #2CF4E5 0%, #00D3C8 50%, #0EAA9F 100%);

  --font-display: 'Outfit', ui-sans-serif, system-ui, sans-serif;
  --font-body: 'IBM Plex Sans', ui-sans-serif, system-ui, sans-serif;

  --ls-eyebrow: 0.18em;
  --ls-display: -0.015em;

  --shadow-1: 0 1px 2px rgba(8, 1, 25, 0.06);
  --shadow-2: 0 4px 12px rgba(8, 1, 25, 0.08);
  --shadow-3: 0 12px 32px rgba(8, 1, 25, 0.12);

  --ease-out: cubic-bezier(0.2, 0.7, 0.2, 1);
  --dur-base: 240ms;
}

/* Esconder branding Streamlit */
#MainMenu { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; height: 2.5rem !important; }
.stDeployButton { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
footer { visibility: hidden; }

/* Aplicar fonts ao corpo Streamlit */
html, body, [class*="css"], .stApp, .main, [data-testid="stAppViewContainer"] {
  font-family: var(--font-body) !important;
  color: var(--ns-grey);
}

/* Headings com Outfit */
.main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
  font-family: var(--font-display) !important;
  color: var(--ns-grey-dark) !important;
  letter-spacing: var(--ls-display);
  font-weight: 600;
}
.main h1 { font-weight: 600; letter-spacing: -0.02em; }
.main h2 { font-weight: 600; margin-top: 2.5rem !important; }
.main h3 { font-weight: 500; }

/* Container principal */
.main .block-container {
  padding-top: 1.5rem !important;
  padding-bottom: 4rem !important;
  max-width: 1100px !important;
  font-family: var(--font-body) !important;
}

/* Transição suave entre páginas */
.main .block-container { animation: nsFadeIn 240ms var(--ease-out); }
@keyframes nsFadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Cards de módulo */
.modulo-card {
  background: var(--ns-white, white);
  border: 1px solid var(--ns-line);
  border-radius: 12px;
  padding: 1.25rem;
  height: 100%;
  transition: all var(--dur-base) var(--ease-out);
  position: relative;
  font-family: var(--font-body);
}
.modulo-card:hover {
  border-color: var(--ns-turquoise);
  box-shadow: var(--shadow-2);
  transform: translateY(-2px);
}
.modulo-card.atual {
  border-color: var(--ns-turquoise);
  background: var(--ns-turquoise-soft);
  box-shadow: 0 0 0 3px rgba(0, 211, 200, 0.18);
}
.modulo-card.concluido {
  border-color: var(--ns-turquoise-dark);
  background: var(--ns-turquoise-soft);
}
.modulo-card-numero {
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 500;
  color: var(--ns-turquoise-dark);
  text-transform: uppercase;
  letter-spacing: var(--ls-eyebrow);
}
.modulo-card-titulo {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--ns-grey-dark);
  margin: 0.5rem 0 0.4rem 0;
  line-height: 1.2;
}
.modulo-card-descr {
  font-family: var(--font-body);
  font-size: 0.875rem;
  color: var(--ns-grey);
  line-height: 1.55;
}
.modulo-card-badge {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  font-size: 11px;
  padding: 0.15rem 0.6rem;
  border-radius: 999px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  font-family: var(--font-body);
}

/* HERO — gradiente Native Stride */
.hero-container {
  background: var(--grad-hero);
  color: white;
  padding: 3.5rem 2.75rem;
  border-radius: 24px;
  margin-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
}
.hero-container::after {
  content: '';
  position: absolute;
  bottom: -50px;
  right: -50px;
  width: 250px;
  height: 250px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(44,244,229,0.15) 0%, transparent 70%);
  pointer-events: none;
}
.hero-eyebrow {
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: var(--ls-eyebrow);
  text-transform: uppercase;
  color: var(--ns-turquoise-light);
  margin-bottom: 1rem;
}
.hero-titulo {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 600;
  line-height: 1.1;
  margin: 0 0 1rem 0;
  letter-spacing: var(--ls-display);
  color: white;
}
.hero-subtitulo {
  font-family: var(--font-body);
  font-size: 1.1rem;
  font-weight: 300;
  line-height: 1.55;
  opacity: 0.92;
  max-width: 680px;
  margin: 0 0 1.5rem 0;
  color: white;
}
.hero-stats {
  display: flex;
  gap: 2.5rem;
  margin-top: 1.75rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255,255,255,0.18);
  flex-wrap: wrap;
}
.hero-stat-num {
  font-family: var(--font-display);
  font-size: 2rem;
  font-weight: 500;
  display: block;
  color: var(--ns-turquoise-light);
  line-height: 1;
}
.hero-stat-label {
  font-family: var(--font-body);
  font-size: 0.8rem;
  font-weight: 400;
  opacity: 0.85;
  margin-top: 0.25rem;
  display: block;
}

/* Eyebrow para secao_titulo */
.ns-eyebrow {
  font-family: var(--font-body);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: var(--ls-eyebrow);
  text-transform: uppercase;
  color: var(--ns-turquoise-dark);
  margin-bottom: 0.4rem;
  display: block;
}

/* Callout boxes — bordas Native Stride */
.callout {
  padding: 1rem 1.25rem;
  border-radius: 12px;
  border-left: 3px solid;
  margin: 1.25rem 0;
  font-family: var(--font-body);
}
.callout-info { background: var(--ns-turquoise-soft); border-color: var(--ns-turquoise-dark); }
.callout-aviso { background: #FFF7ED; border-color: var(--ns-orange-dark); }
.callout-perigo { background: #FEF2F2; border-color: #DC2626; }
.callout-sucesso { background: var(--ns-turquoise-soft); border-color: var(--ns-turquoise-dark); }
.callout-titulo {
  font-family: var(--font-display);
  font-weight: 600;
  margin-bottom: 0.4rem;
  color: var(--ns-grey-dark);
  font-size: 1rem;
}

/* Progress bar — gradient turquesa */
.progress-bar-wrapper {
  background: var(--ns-line);
  border-radius: 999px;
  height: 8px;
  overflow: hidden;
  margin: 0.5rem 0;
}
.progress-bar-fill {
  background: var(--grad-turquoise);
  height: 100%;
  border-radius: 999px;
  transition: width 420ms var(--ease-out);
}

/* Sidebar polish — forçar visível e estilizado */
section[data-testid="stSidebar"] {
  background: var(--ns-bg-subtle) !important;
  display: block !important;
  visibility: visible !important;
  min-width: 300px !important;
  width: 300px !important;
  transform: none !important;
}
/* Garantir fonte Material Icons em elementos que usam ligaduras de ícones */
.material-icons,
.material-icons-outlined,
.material-symbols-rounded,
.material-symbols-outlined,
[class*="material-symbols"],
[class*="material-icons"] {
  font-family: 'Material Symbols Rounded', 'Material Icons' !important;
  font-weight: 400 !important;
  font-style: normal !important;
  font-size: 20px;
  line-height: 1;
  letter-spacing: normal !important;
  text-transform: none !important;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  font-feature-settings: 'liga' !important;
  -webkit-font-feature-settings: 'liga' !important;
  -moz-font-feature-settings: 'liga' !important;
  font-variant-ligatures: discretionary-ligatures !important;
  -webkit-font-smoothing: antialiased;
}

/* Botões NS */
.stButton > button[kind="primary"] {
  background: var(--ns-turquoise) !important;
  border-color: var(--ns-turquoise) !important;
  color: var(--ns-blue-dark) !important;
  font-family: var(--font-body) !important;
  font-weight: 600 !important;
  border-radius: 8px !important;
  transition: all var(--dur-base) var(--ease-out);
}
.stButton > button[kind="primary"]:hover {
  background: var(--ns-turquoise-dark) !important;
  border-color: var(--ns-turquoise-dark) !important;
  color: white !important;
  transform: translateY(-1px);
}
.stButton > button {
  font-family: var(--font-body) !important;
  border-radius: 8px !important;
}

/* Links */
.main a {
  color: var(--ns-turquoise-dark);
  border-bottom: 1px solid transparent;
  text-decoration: none;
  transition: border-color 150ms var(--ease-out);
}
.main a:hover {
  border-bottom-color: var(--ns-turquoise);
}

/* Mobile responsive */
@media (max-width: 768px) {
  .main .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }
  .hero-container { padding: 2rem 1.5rem !important; border-radius: 16px; }
  .hero-titulo { font-size: 1.75rem !important; }
  .hero-subtitulo { font-size: 1rem !important; }
  .hero-stats { flex-direction: column; gap: 1rem !important; }
  .nav-buttons { flex-direction: column; }
}

/* Scrollbar minimalista */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--ns-bg-subtle); }
::-webkit-scrollbar-thumb { background: var(--ns-line); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--ns-grey-light); }

/* Selection */
::selection { background: var(--ns-turquoise); color: var(--ns-blue-dark); }
</style>
        """,
        unsafe_allow_html=True,
    )


def hero(
    eyebrow: str,
    titulo: str,
    subtitulo: str,
    stats: list[tuple[str, str]] | None = None,
) -> None:
    """Hero section Native Stride com gradient hero (#080119 → turquesa)."""
    stats_html = ""
    if stats:
        stats_html = '<div class="hero-stats">'
        for num, label in stats:
            stats_html += (
                f'<div><span class="hero-stat-num">{num}</span>'
                f'<span class="hero-stat-label">{label}</span></div>'
            )
        stats_html += "</div>"

    st.markdown(
        f"""
<div class="hero-container">
  <div class="hero-eyebrow">{eyebrow}</div>
  <h1 class="hero-titulo">{titulo}</h1>
  <p class="hero-subtitulo">{subtitulo}</p>
  {stats_html}
</div>
        """,
        unsafe_allow_html=True,
    )


def progress_tracker(concluidos: int, total: int) -> None:
    pct = int(concluidos / total * 100) if total else 0
    st.markdown(
        f"""
<div style="margin: 1rem 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;
              margin-bottom:0.4rem;font-family:var(--font-body);">
    <span style="font-size:11px;font-weight:500;color:var(--ns-grey-light);
                 text-transform:uppercase;letter-spacing:var(--ls-eyebrow);">
      Progresso do tutorial
    </span>
    <span style="font-size:0.85rem;color:var(--ns-grey);">
      {concluidos} de {total} · {pct}%
    </span>
  </div>
  <div class="progress-bar-wrapper">
    <div class="progress-bar-fill" style="width:{pct}%"></div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def modulo_card(
    numero: str,
    titulo: str,
    descricao: str,
    estado: Literal["pendente", "atual", "concluido"] = "pendente",
    icone: str = "",
) -> str:
    classe_extra = "" if estado == "pendente" else estado
    badge_html = ""
    if estado == "concluido":
        badge_html = (
            '<span class="modulo-card-badge" style="background:var(--ns-turquoise-soft);'
            'color:var(--ns-turquoise-dark);">Concluído</span>'
        )
    elif estado == "atual":
        badge_html = (
            '<span class="modulo-card-badge" style="background:var(--ns-turquoise);'
            'color:var(--ns-blue-dark);">Atual</span>'
        )

    icone_html = (
        f'<div style="font-size:1.5rem;line-height:1;margin:0.6rem 0 0.3rem 0;'
        f'color:var(--ns-turquoise-dark);">{icone}</div>'
        if icone else ""
    )

    return f"""
<div class="modulo-card {classe_extra}">
  {badge_html}
  <div class="modulo-card-numero">Módulo {numero}</div>
  {icone_html}
  <div class="modulo-card-titulo">{titulo}</div>
  <div class="modulo-card-descr">{descricao}</div>
</div>
"""


def grelha_modulos(modulos: list[dict], modulo_atual: str, concluidos: set[str]) -> None:
    cards_html = ""
    for m in modulos:
        if m["numero"] == modulo_atual:
            estado = "atual"
        elif m["numero"] in concluidos:
            estado = "concluido"
        else:
            estado = "pendente"
        cards_html += modulo_card(
            m["numero"], m["titulo"], m["descricao"],
            estado=estado, icone=m.get("icone", ""),
        )

    st.markdown(
        f"""
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
            gap:1rem;margin:1.5rem 0;">
  {cards_html}
</div>
        """,
        unsafe_allow_html=True,
    )


def callout(
    tipo: Literal["info", "aviso", "perigo", "sucesso"],
    titulo: str,
    corpo: str,
    icone: str = "",
) -> None:
    icone_html = f"{icone} " if icone else ""
    st.markdown(
        f"""
<div class="callout callout-{tipo}">
  <div class="callout-titulo">{icone_html}{titulo}</div>
  <div style="font-family:var(--font-body);color:var(--ns-grey);">{corpo}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def secao_titulo(titulo: str, eyebrow: str = "", subtitulo: str = "") -> None:
    """Título de secção Native Stride — eyebrow uppercase + Outfit display."""
    eyebrow_html = ""
    if eyebrow:
        eyebrow_html = f'<div class="ns-eyebrow">{eyebrow}</div>'
    sub_html = ""
    if subtitulo:
        sub_html = (
            f'<div style="font-family:var(--font-body);font-size:1.05rem;'
            f'color:var(--ns-grey);margin-top:0.5rem;line-height:1.55;font-weight:300;">'
            f"{subtitulo}</div>"
        )
    st.markdown(
        f"""
<div style="margin:2.5rem 0 1rem 0;">
  {eyebrow_html}
  <h2 style="margin:0;font-family:var(--font-display);font-weight:600;
             color:var(--ns-grey-dark);letter-spacing:-0.005em;">{titulo}</h2>
  {sub_html}
</div>
        """,
        unsafe_allow_html=True,
    )


# ─── Estado partilhado ─────────────────────────────────────────────


def init_session_state() -> None:
    if "modulos_concluidos" not in st.session_state:
        st.session_state["modulos_concluidos"] = set()
    if "modulo_atual_id" not in st.session_state:
        st.session_state["modulo_atual_id"] = "0"


def marcar_modulo_concluido(modulo_id: str) -> None:
    if "modulos_concluidos" not in st.session_state:
        st.session_state["modulos_concluidos"] = set()
    st.session_state["modulos_concluidos"].add(modulo_id)
