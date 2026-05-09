"""Módulo 3 — O que é a SAOS. Fisiopatologia, sintomas, fatores de risco."""

import streamlit as st

from components.diagramas import (
    animacao_colapso_sequencial,
    animacao_colapso_via_aerea,
)
from components.glossario import termo_inline
from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import RECURSOS_SAOS, recursos_externos, video_nhlbi_apneia
from components.ui import callout, hero, secao_titulo


def render() -> None:
    breadcrumb("m03_saos", "Módulo 3 — O que é a SAOS")

    hero(
        eyebrow="Módulo 3 · A doença",
        titulo="Síndrome de Apneia Obstrutiva do Sono — fisiopatologia",
        subtitulo=(
            "O que falha mecanicamente, quem está em risco, e que sintomas "
            "procurar. Inclui dados de 4 papers recentes (Antunes 2023, "
            "Kim 2026, Krüger 2026, Hartenbaum 2026)."
        ),
    )

    objetivos_aprendizagem("m03_saos")

    secao_titulo(
        eyebrow="Definição",
        titulo="O que é, em termos médicos",
    )

    st.markdown(
        """
        **SAOS = Síndrome de Apneia Obstrutiva do Sono.**

        É um distúrbio do sono caracterizado por **episódios repetidos de
        obstrução parcial ou completa da via aérea superior** durante o sono,
        que provocam **redução ou interrupção do fluxo de ar**, apesar do
        esforço respiratório continuar.

        Não confundir com:
        - **Apneia central**: o cérebro deixa de enviar o sinal para respirar.
          Não há esforço respiratório. (Mais raro, outras causas.)
        - **Apneia mista**: combinação de obstrutiva e central.
        """
    )

    callout(
        tipo="info",
        icone="🔑",
        titulo="A palavra-chave é OBSTRUTIVA",
        corpo=(
            "A SAOS é um problema <strong>mecânico</strong> da via aérea "
            "superior. O cérebro está a mandar respirar, os músculos do peito "
            "estão a fazer força — mas o ar não passa porque há um colapso de "
            "tecidos moles algures entre o palato e a base da língua."
        ),
    )

    secao_titulo(
        eyebrow="Mecanismo",
        titulo="O que acontece em cada episódio",
        subtitulo="Veja o ciclo das 4 fases:",
    )

    tab1, tab2 = st.tabs(["📊 Comparação", "▶️ Sequência"])
    with tab1:
        animacao_colapso_via_aerea()
    with tab2:
        animacao_colapso_sequencial()

    st.markdown(
        """
        ### Tipos de eventos respiratórios

        Numa polissonografia, identificam-se 3 tipos de eventos:

        | Evento | O que é | Critério |
        |---|---|---|
        | **Apneia obstrutiva** | Bloqueio total do fluxo | Redução ≥90% por ≥10s, com esforço |
        | **Hipopneia** | Bloqueio parcial | Redução ≥30% por ≥10s + dessaturação ≥3% ou despertar |
        | **RERA** | Despertar relacionado com esforço | Aumento de esforço sem queda do fluxo, mas com despertar |
        """
    )

    termo_inline("ahi")

    secao_titulo(
        eyebrow="Vídeo educativo",
        titulo="Animação NHLBI / NIH",
    )

    with st.expander("📺 Ver vídeo do NHLBI sobre SAOS"):
        video_nhlbi_apneia()

    secao_titulo(
        eyebrow="Variantes",
        titulo="Nem toda a SAOS é igual",
    )

    st.markdown(
        """
        ### REM-OSA — apneia que predomina em REM

        Em alguns pacientes, os eventos concentram-se quase todos durante o
        **sono REM**. Como em REM os músculos têm atonia (paralisia normal),
        a faringe perde tónus mais ainda — e colapsa mais.

        **Importância clínica** *(Kim 2026)*:
        - Apesar de o **AHI total** poder parecer baixo, os eventos em REM
          duram mais e são associados a maior dessaturação.
        - **Mais comum em mulheres** (papel hormonal sobre o tónus muscular).
        - Associado a:
          - Hipertensão "non-dipping" (que não desce à noite)
          - Aterosclerose subclínica
          - Resistência à insulina
          - Défices cognitivos
        - O CPAP padrão pode ser **menos eficaz** em REM-OSA.
        """
    )

    callout(
        tipo="aviso",
        titulo="Não se descarte por ter AHI 'baixo'",
        corpo=(
            "Um AHI total de 8 (categoria 'ligeira') pode esconder eventos "
            "REM intensos com impacto cardiovascular significativo. Pergunte "
            "à sua médica qual o seu <strong>AHI durante REM</strong>, "
            "não apenas o AHI total."
        ),
    )

    secao_titulo(
        eyebrow="Sintomas",
        titulo="Como se manifesta",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **De noite (parceiro reporta)**
            - 🔊 Ronco alto e irregular
            - 😶 Pausas respiratórias visíveis
            - 😤 Sons de "engasgar" / engasgo
            - 🛏️ Inquietação
            - 🚽 Despertares para urinar (nocturia)
            - 💦 Sudação noturna
            """
        )
    with col2:
        st.markdown(
            """
            **De dia (paciente sente)**
            - 😴 Sonolência diurna excessiva
            - 🤕 Dor de cabeça matinal
            - 🍽️ Boca seca ao acordar
            - 😵 Cansaço persistente
            - 🧠 Dificuldade de concentração
            - 😡 Irritabilidade, baixa libido
            """
        )

    secao_titulo(
        eyebrow="Quem está em risco",
        titulo="Fatores de risco",
    )

    st.markdown(
        """
        Fatores associados a maior probabilidade de SAOS *(literatura combinada)*:
        """
    )

    fatores = [
        ("⚖️ Excesso de peso (BMI ≥ 30)", "Tecido adiposo perifaríngeo reduz o lúmen da via aérea."),
        ("👴 Idade ≥ 40 anos", "Tónus muscular faríngeo diminui com a idade."),
        ("👨 Sexo masculino", "Anatomia da via aérea + influências hormonais."),
        ("📏 Pescoço grosso (>43cm H, >40cm M)", "Indicador de gordura cervical."),
        ("👃 Obstrução nasal crónica", "Septo desviado, cornetos hipertrofiados, alergia."),
        ("👄 Mallampati III ou IV", "Visualização limitada do palato — via aérea pequena."),
        ("🦷 Retrognatia / micrognatia", "Mandíbula recuada — base da língua mais posterior."),
        ("🚬 Tabagismo (atual ou passado)", "Krüger 2026: OR ≈ 1.75 para AHI elevado."),
        ("🍷 Álcool ao deitar", "Relaxa os músculos faríngeos."),
        ("💊 Sedativos (benzodiazepinas)", "Reduzem o tónus muscular."),
        ("🧬 História familiar", "Componente genético na anatomia."),
        ("🩺 Hipertensão, diabetes", "Bidirecional — SAOS causa, mas também co-existe."),
    ]

    for fator, explicacao in fatores:
        with st.container(border=True):
            col1, col2 = st.columns([2, 5])
            with col1:
                st.markdown(f"**{fator}**")
            with col2:
                st.caption(explicacao)

    callout(
        tipo="info",
        icone="🚬",
        titulo="O tabaco — efeito que persiste depois de parar",
        corpo=(
            "Krüger et al. (2026, n=1.206) mostraram que <strong>fumadores "
            "atuais</strong> têm AHI mais elevado (OR 1.75) — esperado. Mas "
            "também os <strong>ex-fumadores</strong> mantêm risco aumentado "
            "(OR 1.76), mesmo após cessação. O dano inflamatório das vias "
            "aéreas e a remodelação tecidual <em>persistem</em>. Razão a mais "
            "para nunca começar."
        ),
    )

    secao_titulo(
        eyebrow="Consequências",
        titulo="Porque tratar a SAOS",
    )

    st.markdown(
        """
        SAOS não tratada está associada a aumento substancial de risco para:
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **Cardiovascular**
            - Hipertensão resistente
            - Enfarte do miocárdio
            - Acidente vascular cerebral
            - Fibrilhação auricular
            - Insuficiência cardíaca
            """
        )
    with col2:
        st.markdown(
            """
            **Metabólico/Cognitivo**
            - Diabetes tipo 2
            - Resistência à insulina
            - Défices de memória/atenção
            - Maior risco de demência
            - Depressão / ansiedade
            """
        )
    with col3:
        st.markdown(
            """
            **Outros**
            - Acidentes (auto, trabalho)
            - Disfunção erétil
            - Glaucoma de tensão normal
            - Doença renal crónica
            - Mortalidade global ↑
            """
        )

    callout(
        tipo="info",
        icone="🚛",
        titulo="Hartenbaum 2026 — SAOS e segurança rodoviária",
        corpo=(
            "A FMCSA (EUA) <strong>desqualifica condutores</strong> que "
            "reportam adormecer ao volante ou tiveram acidente associado a "
            "sonolência. Em Portugal, a SAOS não tratada também é critério "
            "de <strong>inaptidão temporária</strong> para licenças "
            "profissionais. Tratar é, literalmente, salvar vidas no trânsito."
        ),
    )

    recursos_externos(RECURSOS_SAOS)

    perguntas = [
        Pergunta(
            id="m3_q1",
            enunciado="Qual a diferença entre apneia obstrutiva e apneia central?",
            opcoes=[
                "Não há diferença, são sinónimos",
                "Obstrutiva: bloqueio mecânico com esforço; Central: cérebro não envia sinal, sem esforço",
                "Obstrutiva é em adultos, central é em crianças",
                "Obstrutiva ocorre em REM, central em NREM",
            ],
            correta=1,
            explicacao=(
                "**Obstrutiva**: bloqueio mecânico (colapso da via aérea) com "
                "esforço respiratório a continuar. **Central**: o cérebro deixa "
                "de enviar o sinal, sem esforço. A SAOS é a forma obstrutiva."
            ),
        ),
        Pergunta(
            id="m3_q2",
            enunciado="Porque é que a apneia tende a ser pior durante o sono REM?",
            opcoes=[
                "Em REM o cérebro está mais ativo e respira mais rápido",
                "Em REM os músculos têm atonia (paralisia) e a faringe perde tónus",
                "Em REM a tensão arterial cai e bloqueia os vasos da garganta",
                "Em REM o paciente tende a dormir de boca aberta",
            ],
            correta=1,
            explicacao=(
                "Em REM o corpo está em **atonia muscular**. A faringe perde "
                "tónus e colapsa mais facilmente — daí a importância do "
                "AHI durante REM, e a existência da variante REM-OSA."
            ),
        ),
        Pergunta(
            id="m3_q3",
            enunciado=(
                "Segundo Krüger et al. 2026, ex-fumadores que pararam há anos "
                "têm risco de SAOS:"
            ),
            opcoes=[
                "Igual ao de quem nunca fumou",
                "Apenas ligeiramente aumentado",
                "Aumentado de forma semelhante ao dos fumadores atuais",
                "Diminuído (porque o pulmão recupera)",
            ],
            correta=2,
            explicacao=(
                "Ex-fumadores tinham OR 1.76 (vs OR 1.75 dos fumadores atuais). "
                "O dano inflamatório das vias aéreas e a remodelação tecidual "
                "persistem após cessação."
            ),
        ),
        Pergunta(
            id="m3_q4",
            enunciado="Qual destes NÃO é um sintoma típico de SAOS?",
            opcoes=[
                "Ronco alto e pausas respiratórias",
                "Sonolência diurna excessiva",
                "Dor de cabeça matinal",
                "Visão dupla intermitente",
            ],
            correta=3,
            explicacao=(
                "**Visão dupla** não é sintoma de SAOS. Os outros 3 são "
                "clássicos: ronco, sonolência e cefaleia matinal."
            ),
        ),
    ]

    resumo_takeaways("m03_saos")

    render_quiz(
        modulo_id="m03_saos",
        titulo="O que é a SAOS",
        perguntas=perguntas,
    )

    navegacao_botoes("m03_saos")
