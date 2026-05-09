"""Módulo 4 — Diagnóstico. Polissonografia, AHI, escalas, DISE."""

import streamlit as st

from components.diagramas import mallampati_imagem
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

RECURSOS_DIAG = [
    {
        "titulo": "AASM Scoring Manual (resumo público)",
        "descricao": "Critérios oficiais para classificar eventos respiratórios.",
        "url": "https://aasm.org/clinical-resources/scoring-manual/",
        "tipo": "guia",
    },
    {
        "titulo": "STOP-BANG online",
        "descricao": "Calculadora oficial do questionário de rastreio.",
        "url": "http://www.stopbang.ca/osa/screening.php",
        "tipo": "site",
    },
    {
        "titulo": "Epworth Sleepiness Scale (PT)",
        "descricao": "Versão portuguesa validada da escala de Epworth.",
        "url": "https://www.spp.pt/UserFiles/file/Anuario%20da%20SPP%202010/13%20-%20ESCALA%20DE%20EPWORTH%20DA%20SONOLENCIA%20-%20VERSAO%20PORTUGUESA.pdf",
        "tipo": "guia",
    },
    {
        "titulo": "Vito et al. 2014 — DISE European Position Paper",
        "descricao": "Consenso europeu sobre Drug-Induced Sleep Endoscopy.",
        "url": "https://link.springer.com/article/10.1007/s11325-014-0989-6",
        "tipo": "paper",
    },
]


def render() -> None:
    breadcrumb("m04_diagnostico", "Módulo 4 — Diagnóstico")

    hero(
        eyebrow="Módulo 4 · Diagnóstico",
        titulo="Como se diagnostica a SAOS",
        subtitulo=(
            "Do questionário de rastreio à polissonografia, passando pela "
            "DISE — o exame que orientou o seu plano cirúrgico."
        ),
    )

    objetivos_aprendizagem("m04_diagnostico")

    secao_titulo(
        eyebrow="Etapa 1",
        titulo="Rastreio — questionários simples",
        subtitulo=(
            "Antes de pedir um exame caro, usam-se questionários para estimar "
            "a probabilidade de SAOS."
        ),
    )

    st.markdown(
        """
        ### Escala de Epworth (ESS)

        Mede a **sonolência diurna** em 8 situações (ver TV, ler, andar de "
        "carro como passageiro, etc.). Cada item: 0 (nunca adormeço) → 3 (alta "
        "probabilidade de adormecer). Total: 0-24.
        """
    )

    termo_inline("ess")

    st.markdown(
        """
        ### STOP-BANG

        Questionário de **8 perguntas** (4+4) que combinam sintomas e fatores
        de risco. Cada resposta "sim" = 1 ponto.
        """
    )

    termo_inline("stop_bang")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **STOP** (sintomas)
            - **S**noring — Ressona alto?
            - **T**ired — Sente cansaço diurno?
            - **O**bserved — Já o viram parar de respirar?
            - **P**ressure — Tem hipertensão?
            """
        )
    with col2:
        st.markdown(
            """
            **BANG** (fatores de risco)
            - **B**MI — Índice de massa corporal &gt; 35?
            - **A**ge — Idade &gt; 50 anos?
            - **N**eck — Pescoço &gt; 40 cm?
            - **G**ender — Sexo masculino?
            """
        )

    callout(
        tipo="info",
        icone="🎯",
        titulo="Como interpretar o STOP-BANG",
        corpo=(
            "<strong>0-2</strong>: risco baixo · <strong>3-4</strong>: risco "
            "intermédio (considerar PSG) · <strong>5-8</strong>: risco "
            "elevado, especialmente para SAOS moderada-grave (PSG indicada)."
        ),
    )

    secao_titulo(
        eyebrow="Etapa 2",
        titulo="Avaliação clínica — Mallampati",
        subtitulo=(
            "Exame físico simples: o paciente abre a boca e o médico avalia "
            "a visualização das estruturas posteriores."
        ),
    )

    mallampati_imagem()

    st.markdown(
        """
        | Grau | Vê-se | Interpretação |
        |---|---|---|
        | **I** | Palato mole, pilares amigdalinos, úvula completa | Boa via aérea |
        | **II** | Palato mole, parte da úvula | Aceitável |
        | **III** | Apenas a base da úvula | Risco aumentado de SAOS |
        | **IV** | Só palato duro | Risco muito aumentado, via aérea difícil |
        """
    )

    secao_titulo(
        eyebrow="Etapa 3",
        titulo="Polissonografia — o exame de referência",
    )

    termo_inline("psg")

    st.markdown(
        """
        ### Os 4 níveis de polissonografia

        | Nível | Onde | O que regista | Quando se usa |
        |---|---|---|---|
        | **I** | Laboratório com técnico | EEG completo + tudo | SAOS complexa, dúvidas, suspeita de outros distúrbios |
        | **II** | Laboratório sem técnico | Igual ao I, sem técnico presente | **Usado no Antunes 2023** |
        | **III** | Casa ou hospital | Fluxo + esforço + SpO₂ + ECG (sem EEG) | Suspeita clara de SAOS sem comorbilidades |
        | **IV** | Casa | Apenas SpO₂ + frequência cardíaca | Triagem |

        ### O que se mede

        Numa polissonografia nível I/II, registam-se simultaneamente:
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Sinais neurofisiológicos**
            - 🧠 EEG — ondas cerebrais (4 canais)
            - 👁️ EOG — movimentos oculares (2 canais)
            - 💪 EMG — tónus muscular (queixo + tibiais)
            """
        )
    with col2:
        st.markdown(
            """
            **Sinais respiratórios e cardíacos**
            - 🌬️ Cânula nasal — fluxo respiratório
            - 📈 Bandas torácica/abdominal — esforço
            - 🩸 Oxímetro — SpO₂
            - ❤️ ECG — ritmo cardíaco
            - 🔊 Microfone — ronco
            - 🛏️ Sensor de posição
            """
        )

    secao_titulo(
        eyebrow="Métricas",
        titulo="Os números que vai ouvir",
    )

    termo_inline("ahi")
    termo_inline("odi")
    termo_inline("spo2")

    st.markdown(
        """
        ### Classificação de gravidade (AASM)

        | AHI | Categoria |
        |---|---|
        | &lt; 5 | Normal |
        | 5 – 14 | **Ligeira** |
        | 15 – 29 | **Moderada** |
        | ≥ 30 | **Grave** |

        ⚡ **No paper Antunes 2023**: 40,8% ligeira, 48,7% moderada, 10,5% grave
        (n = 76).
        """
    )

    secao_titulo(
        eyebrow="Etapa 4",
        titulo="DISE — escolher a cirurgia certa",
        subtitulo=(
            "Se o paciente é candidato a cirurgia, o passo seguinte é "
            "identificar exatamente onde a via aérea colapsa."
        ),
    )

    termo_inline("dise")

    st.markdown(
        """
        ### Como se faz a DISE

        1. Paciente em decúbito dorsal (deitado de costas) no bloco operatório.
        2. **Sedação leve com propofol** em perfusão controlada.
        3. **BIS (índice biespectral)** monitoriza profundidade da sedação
           (alvo: 50-70 — equivalente a sono N2).
        4. Quando o paciente começa a roncar/ter eventos, introduz-se um
           **endoscópio flexível** pela narina.
        5. Cirurgião grava 2-3 ciclos de obstrução-respiração por nível.

        ### Classificação VOTE — onde colapsa

        Para cada nível, classifica-se:
        - **Padrão**: AP (anteroposterior), lateral, concêntrico
        - **Grau**: 0 (sem colapso), 1 (≤50%), 2 (50-75%), 3 (≥75% — significativo)

        | Letra | Nível | Cirurgia correspondente |
        |---|---|---|
        | **V** — Velum | Palato mole | Palatoplastia |
        | **O** — Orofaríngea (paredes laterais) | Paredes laterais da orofaringe | Palatoplastia lateral / expansão |
        | **T** — Tongue | Base da língua | Cirurgia base da língua, MMA |
        | **E** — Epiglottis | Epiglote | Epiglotectomia parcial |
        """
    )

    callout(
        tipo="sucesso",
        titulo="Porque a DISE é fundamental antes da cirurgia",
        corpo=(
            "É a DISE que permite à equipa cirúrgica escolher a combinação "
            "certa: se o colapso é predominantemente <strong>V + O</strong> "
            "(palato e paredes laterais), indica-se palatoplastia + "
            "amigdalectomia. Se for na base da língua, a abordagem é "
            "diferente. <strong>Sem DISE, a escolha cirúrgica seria às cegas.</strong>"
        ),
    )

    recursos_externos(RECURSOS_DIAG)

    perguntas = [
        Pergunta(
            id="m4_q1",
            enunciado="Qual o exame de referência (gold standard) para diagnosticar SAOS?",
            opcoes=[
                "Radiografia da via aérea",
                "Polissonografia (nível I ou II)",
                "Endoscopia nasal acordado",
                "Análise do sangue noturno",
            ],
            correta=1,
            explicacao=(
                "A **polissonografia** é o gold standard. Nível I (com técnico) "
                "ou II (sem técnico) são os mais completos."
            ),
        ),
        Pergunta(
            id="m4_q2",
            enunciado="Qual é o AHI que classifica a SAOS como 'moderada' segundo a AASM?",
            opcoes=["1-4", "5-14", "15-29", "≥30"],
            correta=2,
            explicacao=(
                "**15-29** = moderada. <5 normal · 5-14 ligeira · 15-29 "
                "moderada · ≥30 grave. O AHI mediano no paper Antunes "
                "(17,4) é moderada."
            ),
        ),
        Pergunta(
            id="m4_q3",
            enunciado="Para que serve a DISE (drug-induced sleep endoscopy)?",
            opcoes=[
                "Confirmar o diagnóstico de SAOS",
                "Identificar onde a via aérea colapsa, para escolher a cirurgia certa",
                "Tratar a apneia em si",
                "Substituir a polissonografia",
            ],
            correta=1,
            explicacao=(
                "DISE não diagnostica SAOS (isso é a polissonografia). "
                "DISE serve para **mapear o nível e o padrão de colapso** — "
                "fundamental para escolher o tipo certo de cirurgia."
            ),
        ),
        Pergunta(
            id="m4_q4",
            enunciado="Na classificação VOTE, a letra 'V' refere-se a:",
            opcoes=[
                "Vias aéreas globais",
                "Velum (palato mole)",
                "Vagus (nervo)",
                "Vestíbulo nasal",
            ],
            correta=1,
            explicacao=(
                "**V — Velum** = palato mole. As 4 letras são V (palato), "
                "O (paredes laterais orofaríngeas), T (base da língua), "
                "E (epiglote)."
            ),
        ),
    ]

    resumo_takeaways("m04_diagnostico")

    render_quiz(
        modulo_id="m04_diagnostico",
        titulo="Diagnóstico",
        perguntas=perguntas,
    )

    navegacao_botoes("m04_diagnostico")
