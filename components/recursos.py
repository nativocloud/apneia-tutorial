"""Componentes para integrar recursos online open-source.

- Visualizador 3D anatómico (Anatomography iframe)
- Vídeos educativos credenciados (NHLBI, MedlinePlus)
- Secção 'Recursos externos' por módulo
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "imagens"


def visualizador_3d_via_aerea() -> None:
    """Embebe o Anatomography (BodyParts3D) com a via aérea destacada."""
    st.markdown(
        "**🌐 Modelo 3D interativo da via aérea** — pode rodar, dar zoom e "
        "explorar com o rato. Carregamento pode demorar alguns segundos."
    )
    iframe = """
<iframe src="https://lifesciencedb.jp/bp3d/?lng=en&style=Z9Z9Z9,FFFFFFFF&cgi=FMA63375,FMA59660,FMA55060&disp_mode=2"
        width="100%" height="500" frameborder="0" style="border-radius:8px;border:1px solid #e2e8f0;">
</iframe>
"""
    components.html(iframe, height=520)
    st.caption(
        "Fonte: BodyParts3D / Anatomography — Database Center for Life Science (Japão). "
        "Licença CC BY-SA 2.1 JP."
    )


def video_nhlbi_apneia() -> None:
    """Vídeo NHLBI (NIH) sobre apneia obstrutiva do sono — domínio público.

    'Living with and Managing Sleep Apnea' — canal oficial NHLBI.
    Mostra um paciente real (Jim) que fez polissonografia e foi diagnosticado
    com SAOS grave; explica o tratamento e impacto na vida.
    """
    st.markdown(
        "**📺 NHLBI — *Living with and Managing Sleep Apnea*** "
        "Vídeo oficial do canal NHLBI (NIH) com depoimento real de um paciente "
        "que foi diagnosticado e iniciou tratamento."
    )
    try:
        st.video("https://www.youtube.com/watch?v=DRzaGc_Z4No")
    except Exception:
        st.warning(
            "O vídeo embebido pode não estar disponível. "
            "[Abrir no YouTube](https://www.youtube.com/watch?v=DRzaGc_Z4No)"
        )
    st.caption(
        "Fonte: National Heart, Lung, and Blood Institute (NHLBI / NIH). "
        "US Government — domínio público. "
        "Se não carregar, pode aceder diretamente: "
        "[YouTube — NHLBI Sleep Apnea](https://www.youtube.com/watch?v=DRzaGc_Z4No)"
    )


def fotografia_clinica(
    ficheiro: str,
    legenda: str,
    fonte: str,
    aviso: str = "",
) -> None:
    """Renderiza uma fotografia clínica com badge identificador, legenda e fonte.

    O badge "📷 Fotografia clínica" distingue de ilustrações didáticas.
    """
    st.markdown(
        '<div style="display:inline-block;background:#fee2e2;color:#991b1b;'
        'padding:0.2rem 0.6rem;border-radius:4px;font-size:0.75rem;'
        'font-weight:600;margin-bottom:0.4rem;">📷 Fotografia clínica</div>',
        unsafe_allow_html=True,
    )
    st.image(
        str(ASSETS / ficheiro),
        caption=f"{legenda} · {fonte}",
        width=620,
    )
    if aviso:
        st.caption(f"⚠️ {aviso}")


def recursos_externos(recursos: list[dict]) -> None:
    """Lista de recursos externos no fim de um módulo.

    Cada recurso é dict com: titulo, descricao, url, tipo (video/site/3d/paper)
    """
    st.markdown(
        '<div style="font-size:0.8rem;font-weight:600;color:#2563eb;'
        'text-transform:uppercase;letter-spacing:0.08em;margin-top:1.5rem;">'
        "Para aprofundar"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "### 🌐 Recursos externos"
    )

    icones = {
        "video": "📺",
        "site": "🌐",
        "3d": "🎲",
        "paper": "📄",
        "guia": "📚",
    }

    for r in recursos:
        icone = icones.get(r.get("tipo", "site"), "🔗")
        st.markdown(
            f"- {icone} **[{r['titulo']}]({r['url']})** — {r['descricao']}"
        )


# ─── Conjuntos de recursos por tema ───────────────────────────────────


RECURSOS_ANATOMIA = [
    {
        "titulo": "OpenStax — Anatomy & Physiology (Cap. 22: Sistema Respiratório)",
        "descricao": "Livro free e completo, com imagens em alta resolução. CC BY 4.0.",
        "url": "https://openstax.org/books/anatomy-and-physiology-2e/pages/22-introduction",
        "tipo": "guia",
    },
    {
        "titulo": "TeachMeAnatomy — Pharynx",
        "descricao": "Anatomia da faringe explicada com diagramas a cor.",
        "url": "https://teachmeanatomy.info/neck/viscera/pharynx/",
        "tipo": "site",
    },
    {
        "titulo": "BodyParts3D / Anatomography (Japão)",
        "descricao": "Modelos 3D interativos da via aérea superior. CC BY-SA 2.1 JP.",
        "url": "https://lifesciencedb.jp/bp3d/",
        "tipo": "3d",
    },
    {
        "titulo": "Z-Anatomy",
        "descricao": "Atlas anatómico 3D open-source completo. GPL.",
        "url": "https://www.z-anatomy.com/",
        "tipo": "3d",
    },
    {
        "titulo": "AnatomyTOOL — Open 3D Man",
        "descricao": (
            "Projeto académico holandês/belga. Modelo 3D em construção. "
            "Foco atual em esqueleto/músculos (via aérea limitada). CC BY-SA."
        ),
        "url": "https://anatomytool.org/open3dmodel",
        "tipo": "3d",
    },
    {
        "titulo": "OpenAnatomy (Brigham/Harvard)",
        "descricao": (
            "Atlases derivados de imagens médicas reais. "
            "Atualmente: cérebro, ouvido, joelho, fígado, abdómen, tórax. "
            "Sem atlas dedicado à via aérea superior."
        ),
        "url": "https://www.openanatomy.org/",
        "tipo": "3d",
    },
]

RECURSOS_SAOS = [
    {
        "titulo": "NHLBI — Sleep Apnea (NIH)",
        "descricao": "Página oficial do NIH sobre SAOS. Domínio público.",
        "url": "https://www.nhlbi.nih.gov/health/sleep-apnea",
        "tipo": "site",
    },
    {
        "titulo": "AASM Sleep Education",
        "descricao": "Site da American Academy of Sleep Medicine para pacientes.",
        "url": "https://sleepeducation.org/sleep-disorders/sleep-apnea/",
        "tipo": "site",
    },
    {
        "titulo": "MedlinePlus — Sleep Apnea (NLM/NIH)",
        "descricao": "Vídeos animados e texto fácil de ler. Domínio público.",
        "url": "https://medlineplus.gov/sleepapnea.html",
        "tipo": "video",
    },
    {
        "titulo": "Antunes et al. 2023 (paper-âncora deste tutorial)",
        "descricao": "Surgical treatment for OSA: effect on sleep architecture.",
        "url": "https://link.springer.com/article/10.1007/s00405-023-08093-8",
        "tipo": "paper",
    },
]
