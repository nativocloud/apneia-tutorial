"""Módulo 1 — Anatomia das vias aéreas superiores.

Cobre: nariz (septo, cornetos, fossas), faringe (palato mole, úvula, amígdalas,
base da língua), laringe (epiglote). Imagens OpenStax 2022 (CC BY 4.0),
fotografias clínicas reais, glossário inline, e visualizador 3D.
"""

import streamlit as st

from components.diagramas import (
    animacao_colapso_sequencial,
    animacao_colapso_via_aerea,
    animacao_vibracao_palato,
    cornetos_detalhe,
    divisoes_faringe,
    via_aerea_sagital_completa,
    via_aerea_simplificada,
)
from components.glossario import termo_inline
from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import (
    RECURSOS_ANATOMIA,
    fotografia_clinica,
    recursos_externos,
    visualizador_3d_via_aerea,
)
from components.ui import callout, hero, secao_titulo


def render() -> None:
    breadcrumb("m01_anatomia", "Módulo 1 — Anatomia")

    hero(
        eyebrow="Módulo 1 · Anatomia",
        titulo="Onde fica o quê — as estruturas envolvidas",
        subtitulo=(
            "Antes de discutir septoplastia, palatoplastia e amigdalectomia, "
            "vamos identificar cada estrutura. Inclui ilustrações modernas, "
            "fotografias clínicas reais e modelo 3D interativo."
        ),
    )

    objetivos_aprendizagem("m01_anatomia")

    # ─── Visão simplificada ───────────────────────────────────────────
    secao_titulo(
        eyebrow="Vista geral",
        titulo="Comece pelo simples — o caminho do ar",
        subtitulo="As 8 estruturas que vamos discutir, identificadas numa única imagem.",
    )

    via_aerea_simplificada()

    # ─── Vista anatómica completa ─────────────────────────────────────
    secao_titulo(
        eyebrow="Detalhe",
        titulo="A vista anatómica completa",
        subtitulo=(
            "Corte longitudinal (sagital) — como se cortasse a cabeça ao meio "
            "e olhasse para dentro. Use o expander para ver a tradução de cada termo."
        ),
    )

    via_aerea_sagital_completa()

    callout(
        tipo="info",
        icone="🎯",
        titulo="O essencial desta imagem",
        corpo=(
            "Siga o ar a partir do nariz: passa entre os <strong>cornetos</strong>, "
            "por baixo do <strong>palato duro</strong>, atrás do palato mole, "
            "atravessa a <strong>orofaringe</strong> (onde estão amígdalas e úvula), "
            "passa pela <strong>epiglote</strong> e desce pela <strong>traqueia</strong> "
            "até aos pulmões. <strong>Em SAOS, o colapso ocorre algures entre o palato "
            "mole e a base da língua</strong>."
        ),
    )

    # ─── Glossário rápido dos 4 termos-chave ──────────────────────────
    secao_titulo(
        eyebrow="Conceitos-chave",
        titulo="Antes de avançar — 4 termos que vai ouvir várias vezes",
        subtitulo="Cada termo abre para uma definição rápida + detalhe clínico.",
    )

    termo_inline("cornetos")
    termo_inline("meatos")
    termo_inline("septo")
    termo_inline("faringe")

    # ─── Zoom no nariz e cornetos ─────────────────────────────────────
    secao_titulo(
        eyebrow="Zoom 1",
        titulo="O nariz e os cornetos",
        subtitulo="As 3 'prateleiras' que aquecem, humidificam e filtram o ar.",
    )

    cornetos_detalhe()

    callout(
        tipo="info",
        icone="💡",
        titulo="Porque há 3 cornetos?",
        corpo=(
            "Para aumentar a <strong>superfície de contacto</strong> entre o ar "
            "e a mucosa num espaço pequeno. A mucosa é vascularizada e funciona "
            "como um <strong>radiador biológico</strong>: aquece o ar a 32-34°C, "
            "humidifica até 95% e filtra partículas. Quando os cornetos incham "
            "(rinite, alergia), bloqueiam os meatos — daí o 'nariz tapado' e a "
            "respiração bucal."
        ),
    )

    # Fotografia clínica real — endoscopia nasal
    st.markdown("#### 📷 O que se vê numa endoscopia nasal real")

    col1, col2 = st.columns([3, 2])
    with col1:
        fotografia_clinica(
            ficheiro="foto_endoscopia_nasal.jpg",
            legenda="Endoscopia nasal — vista da cavidade nasal direita por endoscópio rígido",
            fonte="Wikimedia Commons (CC BY-SA)",
            aviso=(
                "Fotografia clínica real. Pode parecer estranha à primeira vista — "
                "esta é a perspetiva que o cirurgião vê durante a DISE."
            ),
        )
    with col2:
        st.markdown(
            """
            **Como ler a imagem:**
            - O **rosa-claro à direita** é o **septo nasal**.
            - O **rosa mais escuro à esquerda** é a parede lateral (corneto).
            - O **espaço escuro entre os dois** é o meato — por onde o ar passa.
            - As **setas vermelhas** marcam um achado patológico (recirculação
              através do óstio do seio maxilar).
            """
        )

    # ─── Cirurgia: turbinectomia explicada ────────────────────────────
    secao_titulo(
        eyebrow="Cirurgia · cornetos",
        titulo="O que é a turbinectomia",
    )

    termo_inline("turbinectomia")

    st.markdown(
        """
        Numa cirurgia multinível para SAOS, a **redução dos cornetos inferiores**
        dos dois lados é frequentemente associada à microcirurgia endonasal.
        Hoje a tendência é fazer **turbinoplastia conservadora** (com
        radiofrequência ou microdebridador) em vez de remoção radical, para
        preservar a função humidificadora e aquecedora do ar.
        """
    )

    # ─── Faringe e divisões ───────────────────────────────────────────
    secao_titulo(
        eyebrow="Zoom 2",
        titulo="A faringe e os seus 3 andares",
    )

    divisoes_faringe()

    st.markdown(
        """
        ### Que cirurgia atua em que andar?

        | Andar | Estruturas | Cirurgia (no seu caso) |
        |---|---|---|
        | 🟢 **Nasofaringe** | Adenoides, trompa de Eustáquio | — |
        | 🟦 **Orofaringe** | Palato mole, úvula, amígdalas, base da língua | ✅ Palatoplastia + Amigdalectomia |
        | 🟪 **Laringofaringe** | Epiglote, entrada da laringe | — |
        """
    )

    # ─── Animações ────────────────────────────────────────────────────
    secao_titulo(
        eyebrow="Em movimento",
        titulo="Como funciona uma apneia — quatro fases",
        subtitulo=(
            "Comparação lado a lado das 4 fases, ou veja em sequência animada."
        ),
    )

    tab1, tab2 = st.tabs(["📊 Comparação lado a lado", "▶️ Sequência animada"])
    with tab1:
        animacao_colapso_via_aerea()
    with tab2:
        animacao_colapso_sequencial()

    secao_titulo(
        eyebrow="Em movimento",
        titulo="Como nasce o ronco",
        subtitulo="Animação em câmara lenta da vibração do palato mole.",
    )

    animacao_vibracao_palato()

    # ─── Visualizador 3D ──────────────────────────────────────────────
    secao_titulo(
        eyebrow="Exploração 3D",
        titulo="Visualizador anatómico interactivo",
        subtitulo=(
            "Modelo 3D open-source que pode rodar e explorar com o rato. "
            "Útil para ver a relação espacial entre as estruturas."
        ),
    )

    with st.expander("🌐 Abrir visualizador 3D (carrega externo)"):
        visualizador_3d_via_aerea()

    # ─── Tabela-resumo ────────────────────────────────────────────────
    secao_titulo(
        eyebrow="Resumo",
        titulo="Que cirurgia toca em quê",
    )

    st.markdown(
        """
        | Estrutura | Procedimento típico |
        |---|---|
        | Septo nasal | Septoplastia |
        | Cornetos | Microcirurgia endonasal / turbinoplastia |
        | Palato mole + úvula | Palatoplastia para roncopatia |
        | Amígdalas | Amigdalectomia |
        | Base da língua (se indicada) | Cirurgia base da língua |
        | Epiglote (se indicada) | Epiglotectomia parcial |

        Numa **cirurgia multinível** para SAOS, várias destas intervenções
        podem ser combinadas na mesma sessão, conforme o resultado da DISE.
        """
    )

    callout(
        tipo="aviso",
        titulo="Falar com a equipa cirúrgica",
        corpo=(
            "<strong>Confirme a técnica de cada cirurgia:</strong> turbinoplastia "
            "conservadora vs turbinectomia clássica; técnica de palatoplastia (Vicini "
            "barbed, UPPP, expansão esfincteriana); grau de Brodsky das amígdalas; "
            "se a base da língua foi avaliada na DISE."
        ),
    )

    # ─── Recursos externos ────────────────────────────────────────────
    recursos_externos(RECURSOS_ANATOMIA)

    # ─── Resumo takeaways ─────────────────────────────────────────────
    resumo_takeaways("m01_anatomia")

    # ─── Quiz ─────────────────────────────────────────────────────────
    perguntas = [
        Pergunta(
            id="m1_q1",
            enunciado="Quantos cornetos existem em cada fossa nasal?",
            opcoes=["Um", "Dois", "Três", "Quatro"],
            correta=2,
            explicacao=(
                "Três: superior, médio e inferior. O **inferior** é o maior e o "
                "que mais frequentemente causa obstrução."
            ),
        ),
        Pergunta(
            id="m1_q2",
            enunciado="O que são os meatos nasais?",
            opcoes=[
                "Outra palavra para cornetos",
                "Os espaços de ar entre os cornetos",
                "As narinas externas",
                "As cavidades dos seios paranasais",
            ],
            correta=1,
            explicacao=(
                "Os **meatos** são os espaços de ar **entre** os cornetos — é por "
                "aqui que o ar realmente passa. Quando os cornetos incham, os meatos "
                "fecham."
            ),
        ),
        Pergunta(
            id="m1_q3",
            enunciado="O que é a turbinectomia?",
            opcoes=[
                "Remoção das amígdalas",
                "Cirurgia ao palato mole",
                "Redução dos cornetos nasais para alargar os meatos",
                "Inserção de um aparelho oral",
            ],
            correta=2,
            explicacao=(
                "**Turbinectomia / turbinoplastia** = redução dos cornetos. Hoje "
                "prefere-se a forma conservadora (turbinoplastia) que preserva a "
                "mucosa e a função humidificadora."
            ),
        ),
        Pergunta(
            id="m1_q4",
            enunciado=(
                "Em qual divisão da faringe atuam a palatoplastia e a "
                "amigdalectomia?"
            ),
            opcoes=[
                "Nasofaringe (atrás do nariz)",
                "Orofaringe (atrás da boca)",
                "Laringofaringe (atrás da laringe)",
                "Esófago",
            ],
            correta=1,
            explicacao=(
                "**Orofaringe** — é onde estão o palato mole, a úvula e as amígdalas "
                "palatinas."
            ),
        ),
        Pergunta(
            id="m1_q5",
            enunciado="Porque é que o palato mole é relevante na apneia e no ronco?",
            opcoes=[
                "Porque produz saliva durante o sono",
                "Porque é flexível e vibra/colapsa com a passagem do ar",
                "Porque tem músculos respiratórios próprios",
                "Porque liga diretamente aos pulmões",
            ],
            correta=1,
            explicacao=(
                "É músculo + tecido sem suporte ósseo. **Vibra** (ronco) e em casos "
                "graves **colapsa** contra a parede da faringe (apneia)."
            ),
        ),
        Pergunta(
            id="m1_q6",
            enunciado="Para que serve o septo nasal?",
            opcoes=[
                "Filtra bactérias do ar",
                "Separa as duas fossas nasais",
                "Produz muco",
                "Aquece o ar antes de entrar nos pulmões",
            ],
            correta=1,
            explicacao=(
                "É a **parede vertical** (osso atrás, cartilagem à frente) que "
                "divide o nariz em duas fossas. Quando desviado, gera turbulência "
                "e força respiração bucal."
            ),
        ),
    ]

    render_quiz(modulo_id="m01_anatomia", titulo="Anatomia das vias aéreas", perguntas=perguntas)

    navegacao_botoes("m01_anatomia")
