"""Módulo 5 — Tratamentos disponíveis. CPAP, aparelhos, cirurgia, estilo de vida."""

import streamlit as st

from components.glossario import termo_inline
from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import fotografia_clinica, recursos_externos
from components.ui import callout, hero, secao_titulo

RECURSOS_TRAT = [
    {
        "titulo": "AASM — CPAP Treatment Guidelines",
        "descricao": "Diretrizes clínicas oficiais para uso de CPAP.",
        "url": "https://aasm.org/clinical-resources/practice-standards/",
        "tipo": "guia",
    },
    {
        "titulo": "MAD vs CPAP — Cochrane Review",
        "descricao": "Revisão sistemática comparando aparelhos orais e CPAP.",
        "url": "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD004435/full",
        "tipo": "paper",
    },
    {
        "titulo": "Antunes 2023 — Resultados cirúrgicos",
        "descricao": "Paper-âncora do tutorial. Efeito da cirurgia na arquitetura do sono.",
        "url": "https://link.springer.com/article/10.1007/s00405-023-08093-8",
        "tipo": "paper",
    },
]


def render() -> None:
    breadcrumb("m05_tratamentos", "Módulo 5 — Tratamentos")

    hero(
        eyebrow="Módulo 5 · Tratamentos",
        titulo="O que existe para tratar a SAOS",
        subtitulo=(
            "Do CPAP (primeira linha) à cirurgia. Vamos ver as opções, "
            "indicações, vantagens e limites — para entender em que situações "
            "se opta pela abordagem cirúrgica multinível."
        ),
    )

    objetivos_aprendizagem("m05_tratamentos")

    secao_titulo(
        eyebrow="Princípio",
        titulo="A escada terapêutica",
        subtitulo="O algoritmo do paper Antunes 2023:",
    )

    st.markdown(
        """
```
                    Diagnóstico de SAOS
                          │
                          ▼
                  Discutir CPAP
                  ┌───────┴───────┐
                  │               │
                  ▼               ▼
              CPAP aceite    CPAP recusado
              ou tolerado    ou intolerado
                  │               │
                  ▼               ▼
                Avaliação    Alternativas:
                de sucesso   • Aparelhos orais
                             • Mudanças estilo vida
                             • Cirurgia (se DISE indicar)
                             • Estimulação hipoglossa
```
        """
    )

    secao_titulo(
        eyebrow="Primeira linha",
        titulo="CPAP — Continuous Positive Airway Pressure",
    )

    termo_inline("cpap")

    st.markdown(
        """
        ### Como funciona

        Uma **bomba de ar** envia ar pressurizado por uma máscara (nasal ou
        facial) que o paciente usa durante o sono. A pressão (5-15 cmH₂O)
        funciona como um **suporte pneumático** — empurra os tecidos moles
        para fora do caminho do ar.

        Variantes:
        - **CPAP fixo** — pressão constante toda a noite.
        - **APAP / Auto-CPAP** — ajusta automaticamente conforme necessidade.
        - **BiPAP** — duas pressões (maior na inspiração, menor na expiração).
          Para casos complexos ou intolerância ao CPAP fixo.
        """
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        fotografia_clinica(
            ficheiro="ilu_cpap.png",
            legenda="Paciente em uso de CPAP — máscara nasal",
            fonte="Wikimedia Commons (CC BY)",
        )
    with col2:
        st.markdown(
            """
            **Vantagens**
            - 🥇 Mais eficaz (gold standard)
            - ✅ Reversível, não invasivo
            - 📈 Reduz AHI em &gt;90%
            - ❤️ Reduz risco cardiovascular

            **Limitações**
            - 😬 Adesão baixa (30-50%)
            - 🌬️ Sensação de "ar a soprar"
            - 😴 Difícil dormir com máscara
            - 💧 Boca seca, irritação
            - 🔌 Dependência do equipamento
            """
        )

    callout(
        tipo="aviso",
        icone="⚠️",
        titulo="O problema da adesão",
        corpo=(
            "Apesar de eficaz, <strong>30-50% dos pacientes não usam CPAP "
            "o suficiente</strong> (definido como ≥4 horas/noite, 70% das "
            "noites). Quando o CPAP não é tolerado ou recusado, a cirurgia "
            "torna-se uma alternativa — foi o seu caso."
        ),
    )

    secao_titulo(
        eyebrow="Segunda linha",
        titulo="Aparelhos orais (MAD)",
    )

    st.markdown(
        """
        **Mandibular Advancement Device (MAD)** — aparelho dentário que **avança
        a mandíbula** alguns milímetros durante o sono, puxando a base da
        língua e abrindo a via aérea retrolingual.

        **Quando se usa**:
        - SAOS ligeira a moderada
        - Pacientes que recusam CPAP
        - Anatomia adequada (boa dentição)

        **Limites**:
        - Menos eficaz que CPAP em SAOS grave
        - Pode causar dor temporomandibular
        - Pode mover dentes a longo prazo
        - Custos (200-1500€) e ajustes periódicos
        """
    )

    secao_titulo(
        eyebrow="Estilo de vida",
        titulo="Mudanças que fazem diferença",
        subtitulo="Não são 'tratamento' isolado, mas potenciam todos os outros.",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Alta evidência**
            - ⚖️ **Perder peso** — em obesos, 10% de redução pode descer AHI 25%
            - 🍷 **Reduzir álcool** ao deitar
            - 💊 **Evitar sedativos** (benzos) à noite
            - 🚭 **Cessação tabágica** (Krüger 2026)
            """
        )
    with col2:
        st.markdown(
            """
            **Casos selecionados**
            - 🛏️ **Terapia posicional** — se SAOS é só em supino
            - 🏃 **Exercício aeróbico regular** — reduz AHI mesmo sem perda de peso
            - 👅 **Exercícios miofuncionais** — fortalecem músculos faríngeos
            - 🌙 **Higiene do sono** — horários, ambiente
            """
        )

    secao_titulo(
        eyebrow="Cirurgia",
        titulo="Quando é indicada cirurgia",
    )

    st.markdown(
        """
        A **cirurgia da via aérea superior** é considerada quando:

        1. **CPAP falha** ou é mal tolerado/recusado.
        2. **DISE identifica nível claro de colapso** anatómico.
        3. Paciente é **adequado anatomicamente** (BMI ≤ 30 idealmente, sem
           comorbilidades graves).
        4. Há **expectativa realista** sobre os resultados.

        ### Tipos de cirurgia (do superficial ao radical)

        | Cirurgia | Foco | Indicação |
        |---|---|---|
        | **Septoplastia + turbinoplastia** | Nariz | Obstrução nasal |
        | **Palatoplastia (UPPP, Vicini, lateral)** | Palato | Colapso V/O |
        | **Amigdalectomia** | Amígdalas | Brodsky III/IV |
        | **Cirurgia base da língua (radiofrequência, coblation)** | Língua | Colapso T |
        | **Epiglotectomia parcial** | Epiglote | Colapso E |
        | **Avanço maxilo-mandibular (MMA)** | Esqueleto | SAOS grave, falha de outras cirurgias |
        | **Estimulação hipoglossa (Inspire)** | Nervo | Não responde a CPAP, paciente magro |
        """
    )

    callout(
        tipo="info",
        icone="🔑",
        titulo="A cirurgia multinível",
        corpo=(
            "Combina <strong>intervenções em múltiplos níveis</strong>: nariz "
            "(septoplastia + turbinoplastia + microcirurgia endonasal) + "
            "orofaringe (palatoplastia + amigdalectomia). É a abordagem do "
            "paper Antunes 2023 — combinar níveis quando a DISE mostra "
            "colapso multinível."
        ),
    )

    secao_titulo(
        eyebrow="Resultados típicos",
        titulo="Quão eficaz é cada tratamento",
    )

    st.markdown(
        """
        | Tratamento | Redução típica do AHI | Adesão | Reversível? |
        |---|---|---|---|
        | **CPAP** | &gt;90% | 30-50% | ✅ Sim |
        | **Aparelho oral (MAD)** | 50-60% | ~70% | ✅ Sim |
        | **Cirurgia multinível** | 50-70% | n/a | ⚠️ Permanente |
        | **MMA** | &gt;80% | n/a | ⚠️ Permanente |
        | **Estimulação hipoglossa** | 60-70% | ~85% | ⚠️ Implante |
        | **Estilo de vida (perda 10% peso)** | ~25% | Variável | ✅ Sim |

        ⚡ No paper Antunes 2023: **75% dos pacientes foram 'responders'**
        após cirurgia multinível, com AHI mediano a descer de 17,4 para 13,0.
        """
    )

    recursos_externos(RECURSOS_TRAT)

    perguntas = [
        Pergunta(
            id="m5_q1",
            enunciado="Qual o tratamento de primeira linha para SAOS moderada-grave?",
            opcoes=["Aparelho oral", "Cirurgia", "CPAP", "Perda de peso"],
            correta=2,
            explicacao=(
                "**CPAP** é gold standard — reduz AHI &gt;90% e tem evidência "
                "robusta. A cirurgia é alternativa quando CPAP falha ou é "
                "recusado."
            ),
        ),
        Pergunta(
            id="m5_q2",
            enunciado="Qual a principal limitação do CPAP?",
            opcoes=[
                "Custo do equipamento",
                "Adesão baixa (apenas 30-50% dos pacientes o usam suficientemente)",
                "Não é eficaz em SAOS moderada",
                "Tem muitos efeitos secundários graves",
            ],
            correta=1,
            explicacao=(
                "A **adesão** é o ponto fraco do CPAP. Apesar de eficaz, "
                "muitos pacientes não conseguem usar máscara durante o sono. "
                "Daí existirem alternativas (aparelhos orais, cirurgia)."
            ),
        ),
        Pergunta(
            id="m5_q3",
            enunciado="Que cirurgia atua na base da língua?",
            opcoes=[
                "Septoplastia",
                "Palatoplastia",
                "Cirurgia da base da língua (radiofrequência ou coblation)",
                "Amigdalectomia",
            ],
            correta=2,
            explicacao=(
                "**Cirurgia da base da língua** (radiofrequência, coblation, "
                "ou avanço do genioglosso) é específica para colapso ao nível "
                "T (tongue) na DISE."
            ),
        ),
        Pergunta(
            id="m5_q4",
            enunciado=(
                "No paper Antunes 2023, qual a percentagem de pacientes "
                "considerados 'responders' à cirurgia?"
            ),
            opcoes=["25%", "50%", "75%", "100%"],
            correta=2,
            explicacao=(
                "**75%** foram responders (≥50% redução do AHI E AHI &lt;20). "
                "Os 25% non-responders mantiveram AHI elevado e geralmente "
                "precisam de CPAP de resgate."
            ),
        ),
    ]

    resumo_takeaways("m05_tratamentos")

    render_quiz(
        modulo_id="m05_tratamentos",
        titulo="Tratamentos disponíveis",
        perguntas=perguntas,
    )

    navegacao_botoes("m05_tratamentos")
