"""Módulo 2 — Como dormimos. Fases do sono e arquitetura."""

import streamlit as st

from components.diagramas import hipnograma_inline, hipnograma_real
from components.glossario import termo_inline
from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import recursos_externos
from components.ui import callout, hero, secao_titulo

RECURSOS_SONO = [
    {
        "titulo": "Sleep Foundation — Stages of Sleep",
        "descricao": "Explicação acessível das 4 fases do sono.",
        "url": "https://www.sleepfoundation.org/stages-of-sleep",
        "tipo": "site",
    },
    {
        "titulo": "AASM — Two Process Model of Sleep",
        "descricao": "Como o corpo regula o sono e a vigília.",
        "url": "https://aasm.org/clinical-resources/practice-standards/",
        "tipo": "guia",
    },
    {
        "titulo": "Antunes et al. 2023 — Tabela 2 (PSG pré vs pós cirurgia)",
        "descricao": "Dados quantitativos das fases do sono em SAOS.",
        "url": "https://link.springer.com/article/10.1007/s00405-023-08093-8",
        "tipo": "paper",
    },
]


def render() -> None:
    breadcrumb("m02_sono", "Módulo 2 — Como dormimos")

    hero(
        eyebrow="Módulo 2 · O sono",
        titulo="Como dormimos — e porque a apneia 'estraga' o sono",
        subtitulo=(
            "O sono não é um estado uniforme: alterna entre 4 fases ao longo "
            "da noite. Cada fase tem uma função específica. A SAOS impede que "
            "o cérebro chegue às fases mais reparadoras."
        ),
    )

    objetivos_aprendizagem("m02_sono")

    secao_titulo(
        eyebrow="Fundamentos",
        titulo="O sono não é 'estar desligado'",
    )

    st.markdown(
        """
        Durante o sono, o cérebro **alterna entre 4 fases** que se repetem em
        ciclos de **~90 minutos**. Cada ciclo tem mais ou menos as mesmas
        proporções, mas:

        - Nas **primeiras horas** da noite, predomina o sono profundo (N3).
        - Nas **últimas horas**, predomina o sono REM (sonhos).

        A divisão tradicional separa **sono NREM** (Não-REM) em N1, N2, N3, e
        sono **REM** (Rapid Eye Movement) à parte.
        """
    )

    termo_inline("fases_sono")

    secao_titulo(
        eyebrow="As 4 fases",
        titulo="Cada fase tem a sua função",
    )

    fases = [
        {
            "fase": "N1",
            "duracao": "~5%",
            "cor": "#fcd34d",
            "titulo": "Adormecer",
            "descr": (
                "Transição da vigília para o sono. Pode acordar facilmente. "
                "Normal: ~5% do tempo total de sono."
            ),
            "papel": "Início do desligar — mas pouco restaurador.",
        },
        {
            "fase": "N2",
            "duracao": "~45-55%",
            "cor": "#93c5fd",
            "titulo": "Sono ligeiro",
            "descr": (
                "A maior parte do sono. Ondas K e fusos do sono no EEG. "
                "Já não acorda com sons baixos."
            ),
            "papel": "Consolidação de memória e regulação emocional.",
        },
        {
            "fase": "N3",
            "duracao": "~15-25%",
            "cor": "#34d399",
            "titulo": "Sono profundo / SWS",
            "descr": (
                "Slow Wave Sleep. Ondas lentas (delta) no EEG. Difícil acordar. "
                "É **a fase mais restauradora fisicamente**."
            ),
            "papel": (
                "Reparação tecidular, libertação de hormona de crescimento, "
                "limpeza de produtos metabólicos do cérebro (sistema glinfático)."
            ),
        },
        {
            "fase": "REM",
            "duracao": "~20-25%",
            "cor": "#c084fc",
            "titulo": "Sono REM (sonhos)",
            "descr": (
                "Movimento rápido dos olhos. Atividade cerebral semelhante à "
                "vigília mas com **paralisia muscular** completa (atonia)."
            ),
            "papel": (
                "**Consolidação da memória** declarativa e emocional. "
                "Aprendizagem. Saúde mental."
            ),
        },
    ]

    for f in fases:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown(
                f"""
<div style="background:{f['cor']};padding:1rem;border-radius:12px;text-align:center;">
  <div style="font-size:1.6rem;font-weight:700;color:white;">{f['fase']}</div>
  <div style="font-size:0.75rem;color:white;opacity:0.9;">{f['duracao']}</div>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(f"**{f['titulo']}**")
            st.markdown(f"{f['descr']}")
            st.caption(f"🎯 **Função**: {f['papel']}")

    secao_titulo(
        eyebrow="Visualização",
        titulo="O hipnograma — desenho do sono ao longo da noite",
        subtitulo=(
            "Os técnicos do sono representam as fases num gráfico chamado "
            "hipnograma. É a 'fotografia' do que se passou durante a noite."
        ),
    )

    hipnograma_real()

    st.markdown(
        """
        ### Como ler um hipnograma

        - **Eixo Y**: as fases (Wake no topo, N3 em baixo, REM separado).
        - **Eixo X**: o tempo (horas a fio, da meia-noite às ~7h).
        - **Curva**: cada vez que o cérebro muda de fase, a curva move-se.
        - **Idealmente**: descidas longas a N3 nas primeiras 2-3h, depois
          períodos de REM cada vez maiores.
        """
    )

    secao_titulo(
        eyebrow="O efeito da SAOS",
        titulo="Sono normal vs sono fragmentado",
        subtitulo=(
            "Em SAOS, cada apneia provoca um micro-despertar. O sono nunca "
            "fica profundo o suficiente. Compare visualmente:"
        ),
    )

    tab1, tab2 = st.tabs(["⚠ Com SAOS", "✓ Após tratamento"])
    with tab1:
        hipnograma_inline("antes")
        st.caption(
            "Fragmentação típica: incursões frequentes a wake (micro-despertares), "
            "pouco N3, REM reduzido."
        )
    with tab2:
        hipnograma_inline("depois")
        st.caption(
            "Sono consolidado: ciclos NREM/REM regulares, períodos longos "
            "em N3 e REM."
        )

    callout(
        tipo="info",
        icone="📊",
        titulo="O que o paper Antunes 2023 mostrou",
        corpo=(
            "Após cirurgia da via aérea superior, <strong>o tempo em N3 "
            "aumentou de 16,9% para 18,9%</strong> (p = 0.003 — significativo). "
            "Isto pode parecer pouco, mas representa <strong>~13 minutos extra "
            "de sono profundo restaurador por noite</strong>. Multiplicado por "
            "365 noites por ano, dá &gt;78 horas anuais de N3 a mais."
        ),
    )

    secao_titulo(
        eyebrow="Porquê",
        titulo="Porque é grave perder N3 e REM",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Perder N3 (sono profundo)**
            - 🧠 Acumulação de produtos metabólicos no cérebro
            - 💪 Menos libertação de hormona de crescimento
            - 🦠 Sistema imunitário menos eficiente
            - ❤️ Maior risco cardiovascular
            - 🔋 Sensação de "nunca estar descansado"
            """
        )
    with col2:
        st.markdown(
            """
            **Perder REM**
            - 📚 Pior consolidação de memória
            - 🎭 Pior regulação emocional
            - 😔 Maior risco de depressão e ansiedade
            - 🎓 Menor capacidade de aprendizagem
            - 🧘 Estado de espírito instável
            """
        )

    callout(
        tipo="aviso",
        titulo="Implicação prática",
        corpo=(
            "Quando alguém com SAOS diz que 'dormiu 8 horas', está a referir-se "
            "ao tempo na cama. Mas o <strong>sono útil</strong> (sobretudo N3 "
            "e REM) pode ser apenas metade disso. Daí a fadiga diurna, mesmo "
            "depois de noites longas."
        ),
    )

    recursos_externos(RECURSOS_SONO)

    perguntas = [
        Pergunta(
            id="m2_q1",
            enunciado="Qual fase do sono é considerada 'sono profundo' (slow wave sleep)?",
            opcoes=["N1", "N2", "N3", "REM"],
            correta=2,
            explicacao=(
                "**N3** (também chamada SWS — Slow Wave Sleep) é a fase mais "
                "profunda. Ondas delta no EEG, libertação de hormona de "
                "crescimento, limpeza glinfática do cérebro."
            ),
        ),
        Pergunta(
            id="m2_q2",
            enunciado="Quanto tempo dura aproximadamente um ciclo de sono?",
            opcoes=["~30 min", "~60 min", "~90 min", "~120 min"],
            correta=2,
            explicacao=(
                "Cada ciclo de sono dura **~90 minutos**. Numa noite de 8h, "
                "passamos por 4-5 ciclos. Os primeiros têm mais N3, os últimos "
                "mais REM."
            ),
        ),
        Pergunta(
            id="m2_q3",
            enunciado=(
                "No paper Antunes 2023, qual fase do sono mostrou aumento "
                "estatisticamente significativo após cirurgia?"
            ),
            opcoes=["N1", "N2", "N3", "REM"],
            correta=2,
            explicacao=(
                "**N3** aumentou de 16,9% para 18,9% (p = 0.003). Esta é uma "
                "mudança clinicamente relevante porque N3 é a fase mais "
                "restauradora."
            ),
        ),
        Pergunta(
            id="m2_q4",
            enunciado="Em sono REM, o que acontece aos músculos do corpo?",
            opcoes=[
                "Tensão máxima — corpo prepara-se para acordar",
                "Atonia — paralisia muscular quase completa",
                "Espasmos rítmicos",
                "Relaxamento parcial, semelhante a N2",
            ],
            correta=1,
            explicacao=(
                "Em REM o corpo está em **atonia** (paralisia) — exceto "
                "diafragma e músculos oculares. Isto explica porque a SAOS "
                "tende a ser pior em REM (a faringe perde tónus)."
            ),
        ),
    ]

    resumo_takeaways("m02_sono")

    render_quiz(modulo_id="m02_sono", titulo="Como dormimos", perguntas=perguntas)

    navegacao_botoes("m02_sono")
