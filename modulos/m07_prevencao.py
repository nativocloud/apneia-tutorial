"""Módulo 7 — Prevenção e estilo de vida."""

import streamlit as st

from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import recursos_externos
from components.ui import callout, hero, secao_titulo

RECURSOS_PREV = [
    {
        "titulo": "Krüger et al. 2026 — Smoking and OSA",
        "descricao": "Evidência populacional do impacto do tabaco na SAOS.",
        "url": "https://www.nature.com/articles/s41598-026-48908-2",
        "tipo": "paper",
    },
    {
        "titulo": "AASM — Behavioral and Lifestyle Treatments",
        "descricao": "Mudanças comportamentais com evidência para SAOS.",
        "url": "https://aasm.org/clinical-resources/practice-standards/",
        "tipo": "guia",
    },
    {
        "titulo": "Myofunctional Therapy for OSA — Systematic Review",
        "descricao": "Exercícios orofaríngeos: redução AHI ~50% em ligeira/moderada.",
        "url": "https://pubmed.ncbi.nlm.nih.gov/25940446/",
        "tipo": "paper",
    },
    {
        "titulo": "Linha SOS Tabaco (PT) — 808 208 888",
        "descricao": "Apoio gratuito à cessação tabágica.",
        "url": "https://www.dgs.pt/programa-nacional-para-a-prevencao-e-controlo-do-tabagismo.aspx",
        "tipo": "site",
    },
]


def render() -> None:
    breadcrumb("m07_prevencao", "Módulo 7 — Prevenção")

    hero(
        eyebrow="Módulo 7 · Prevenção",
        titulo="Prevenir e potenciar — o que pode fazer todos os dias",
        subtitulo=(
            "A cirurgia é o tratamento, mas o estilo de vida define se os "
            "resultados duram. Estes são os 7 pilares com mais evidência."
        ),
    )

    objetivos_aprendizagem("m07_prevencao")

    secao_titulo(
        eyebrow="Princípio",
        titulo="A SAOS responde ao estilo de vida",
        subtitulo="Não substitui tratamento, mas potencia-o significativamente.",
    )

    callout(
        tipo="info",
        icone="📊",
        titulo="O efeito do peso, em números",
        corpo=(
            "Em pacientes com SAOS e excesso de peso, <strong>uma perda de "
            "10% do peso corporal pode reduzir o AHI em ~25%</strong>. "
            "Inversamente, ganho de 10% pode aumentar AHI em ~30%. O peso "
            "é o fator de estilo de vida com maior impacto isolado."
        ),
    )

    # ─── Pilar 1: Peso ──────────────────────────────────────────────
    secao_titulo(
        eyebrow="Pilar 1",
        titulo="Peso e composição corporal",
    )

    st.markdown(
        """
        ### Por que importa
        - Tecido adiposo no pescoço e perifaríngeo **reduz o lúmen** da via aérea.
        - Gordura visceral abdominal **diminui o volume pulmonar** (CRF) — a
          via aérea torna-se mais colapsável.
        - Inflamação sistémica do tecido adiposo **agrava** a inflamação
          local da faringe.

        ### Metas práticas
        - **BMI alvo**: ideal 18,5-24,9 (paciente atual: 27,3 mediana no Antunes).
        - **Pescoço**: &lt;43cm (homens), &lt;40cm (mulheres).
        - **Cintura**: &lt;94cm (homens), &lt;80cm (mulheres) — saúde metabólica.

        ### Como
        - Défice calórico moderado (300-500 kcal/dia)
        - **Dieta mediterrânica** — evidência mais forte para SAOS
        - **Exercício combinado** (aeróbico + força) — mais eficaz que só aeróbico
        - **Cirurgia bariátrica** — em obesidade severa, pode resolver SAOS sem cirurgia ORL
        """
    )

    # ─── Pilar 2: Tabaco ───────────────────────────────────────────
    secao_titulo(
        eyebrow="Pilar 2",
        titulo="Cessação tabágica",
    )

    st.markdown(
        """
        ### Krüger et al. 2026 — a evidência

        Estudo populacional alemão (n=1.206) com polissonografias completas:
        - **Fumadores atuais**: OR 1,75 para AHI elevado.
        - **Ex-fumadores**: OR 1,76 (mantém-se elevado!).

        Mecanismos:
        - Inflamação crónica das vias aéreas
        - Edema da mucosa
        - Alteração dos reflexos neuromusculares faríngeos
        - Remodelação tecidual permanente

        ### Implicações
        - Parar de fumar é **essencial** mesmo se achar que "já é tarde".
        - O risco diminui mas não volta totalmente ao basal.
        - Apoio: **medicação** (vareniclina, nicotina substitutiva) + **comportamental**.
        - Linha SOS Tabaco em Portugal: **808 208 888** (gratuito).
        """
    )

    # ─── Pilar 3: Álcool e sedativos ──────────────────────────────
    secao_titulo(
        eyebrow="Pilar 3",
        titulo="Álcool e sedativos",
    )

    st.markdown(
        """
        ### O efeito direto

        - **Álcool** ao deitar **relaxa os músculos faríngeos** e suprime os
          reflexos protetores. Piora a SAOS mesmo em pessoas que normalmente
          não a têm.
        - **Benzodiazepinas** (diazepam, alprazolam, lorazepam) **reduzem o
          tónus muscular** e o limiar de despertar.

        ### Recomendações práticas

        | Substância | Recomendação |
        |---|---|
        | Álcool | Evitar **3 horas antes de deitar**. Se usar, máximo 1 unidade. |
        | Benzodiazepinas | Evitar para insónia em pacientes com SAOS. Rever com médico. |
        | Opióides | Cuidado redobrado — depressão respiratória. |
        | Antihistamínicos sedativos | Substituir por não-sedativos quando possível. |
        | Cannabis | Evidência mista — evitar ao deitar. |
        """
    )

    # ─── Pilar 4: Posição ─────────────────────────────────────────
    secao_titulo(
        eyebrow="Pilar 4",
        titulo="Posição de dormir",
    )

    st.markdown(
        """
        ### SAOS posicional

        Em ~30% dos pacientes, a SAOS é **substancialmente pior em decúbito
        dorsal** (deitado de costas). Em alguns casos, é **só** em supino.

        ### Como evitar dormir de costas

        - **Almofada de posicionamento** (bola de ténis nas costas no pijama)
        - **Cintos / dispositivos** específicos (Night Shift, Zzoma)
        - **Apps** com alarmes que detetam posição (Somnopose)
        - **Almofadas em cunha** que elevam o tronco 30°

        ### Dormir de lado vs dormir sentado

        - **Lado** (decúbito lateral): primeira escolha em SAOS.
        - **Cabeceira elevada 30°**: reduz colapso retroglossal.
        - **Decúbito ventral** (de barriga para baixo): dificulta a respiração — não.
        """
    )

    # ─── Pilar 5: Exercícios miofuncionais ─────────────────────
    secao_titulo(
        eyebrow="Pilar 5",
        titulo="Exercícios miofuncionais (orofaríngeos)",
    )

    st.markdown(
        """
        Conjunto de exercícios para **fortalecer músculos da língua e
        faringe** — semelhante a fisioterapia mas para a via aérea superior.

        ### Evidência

        Revisão sistemática: redução do AHI **~50% em SAOS ligeira-moderada**
        com prática diária de 30 min, durante 3 meses. Útil **complementarmente**
        ao tratamento principal.

        ### Exemplos de exercícios

        1. **Língua à frente**: empurrar a língua contra o palato 5s, repetir 20x.
        2. **Língua para trás**: sugar a língua contra o palato, manter 10s.
        3. **Sopro com lábios fechados**: bochechas inchadas, segurar 10s.
        4. **Respiração nasal forçada**: respirar só pelo nariz durante 5 min.
        5. **Cantar / tocar didgeridoo**: o didgeridoo tem evidência específica
           para SAOS.

        ### Como começar
        - **Fonoaudiólogo / terapeuta da fala** com formação em SAOS.
        - Aplicações (e.g., AirwayGym, MyAirway) com vídeos guiados.
        - Frequência: **diária**, 20-30 min, durante 3 meses para ver efeito.
        """
    )

    # ─── Pilar 6: Higiene do sono ──────────────────────────────
    secao_titulo(
        eyebrow="Pilar 6",
        titulo="Higiene do sono",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Fazer**
            - 🕐 Horários regulares (mesmo aos fins-de-semana)
            - 🌑 Quarto escuro, fresco (18-20°C)
            - 🛏️ Cama só para dormir e sexo
            - 🌅 Exposição solar matinal
            - 🏃 Exercício diário (mas não 3h antes de deitar)
            - 📓 Rotina relaxante 30-60 min antes
            """
        )
    with col2:
        st.markdown(
            """
            **Evitar**
            - 📱 Ecrãs 1h antes de deitar (luz azul)
            - ☕ Cafeína depois das 14h
            - 🍽️ Refeições pesadas 3h antes de deitar
            - 💤 Sestas longas depois das 15h
            - 😰 Ruminar problemas na cama (levantar e voltar)
            - 🍷 Álcool ao deitar
            """
        )

    # ─── Pilar 7: Saúde global ────────────────────────────────
    secao_titulo(
        eyebrow="Pilar 7",
        titulo="Co-morbilidades — controlar bem",
    )

    st.markdown(
        """
        SAOS, hipertensão, diabetes, obesidade e depressão **agravam-se
        mutuamente**. Tratar bem **uma** ajuda as **outras**.

        - **Hipertensão**: controlo rigoroso reduz risco cardiovascular.
        - **Diabetes**: controlo glicémico melhora microcirculação.
        - **Refluxo gastroesofágico**: agrava inflamação faríngea.
        - **Depressão**: pode mascarar/agravar fadiga; tratamento melhora adesão a CPAP.
        - **Hipotiroidismo**: deve ser excluído — pode mimetizar/agravar SAOS.
        """
    )

    callout(
        tipo="sucesso",
        icone="✅",
        titulo="Resumo: 5 ações com mais impacto",
        corpo=(
            "<ol>"
            "<li><strong>Perder peso</strong> se BMI &gt; 25 (efeito direto e dose-dependente)</li>"
            "<li><strong>Parar de fumar</strong> (Krüger 2026 — efeito persiste anos)</li>"
            "<li><strong>Sem álcool</strong> 3h antes de deitar</li>"
            "<li><strong>Dormir de lado</strong> ou com cabeceira elevada 30°</li>"
            "<li><strong>30 min/dia de exercício orofaríngeo</strong> durante 3 meses</li>"
            "</ol>"
        ),
    )

    recursos_externos(RECURSOS_PREV)

    perguntas = [
        Pergunta(
            id="m7_q1",
            enunciado=(
                "Em pacientes com SAOS e excesso de peso, uma perda de 10% do "
                "peso corporal reduz o AHI em aproximadamente:"
            ),
            opcoes=["5%", "25%", "50%", "75%"],
            correta=1,
            explicacao=(
                "**~25%**. O peso é o fator de estilo de vida com maior "
                "impacto isolado na SAOS."
            ),
        ),
        Pergunta(
            id="m7_q2",
            enunciado="Segundo Krüger 2026, quem parou de fumar há vários anos:",
            opcoes=[
                "Tem o mesmo risco de SAOS de quem nunca fumou",
                "Mantém risco aumentado, semelhante ao dos fumadores atuais",
                "Tem risco maior que os fumadores atuais",
                "Tem o risco reduzido para metade",
            ],
            correta=1,
            explicacao=(
                "OR 1.76 (ex-fumadores) vs OR 1.75 (atuais). O dano "
                "inflamatório e a remodelação tecidual persistem após cessação."
            ),
        ),
        Pergunta(
            id="m7_q3",
            enunciado="Porque é que o álcool ao deitar agrava a apneia do sono?",
            opcoes=[
                "Causa desidratação que estreita a faringe",
                "Relaxa os músculos faríngeos e suprime reflexos protetores",
                "Aumenta a frequência cardíaca",
                "Estimula o sistema nervoso simpático",
            ],
            correta=1,
            explicacao=(
                "O álcool **relaxa os músculos faríngeos** e suprime os "
                "reflexos protetores que normalmente abrem a via aérea durante "
                "uma obstrução."
            ),
        ),
        Pergunta(
            id="m7_q4",
            enunciado="Os exercícios miofuncionais para SAOS:",
            opcoes=[
                "Substituem completamente o CPAP",
                "Reduzem AHI ~50% em SAOS ligeira-moderada com 3 meses de prática",
                "Não têm evidência clínica",
                "Apenas funcionam em crianças",
            ],
            correta=1,
            explicacao=(
                "Revisão sistemática mostra **redução AHI ~50% em SAOS "
                "ligeira-moderada** com 30 min/dia durante 3 meses. Não "
                "substitui o tratamento principal mas é coadjuvante útil."
            ),
        ),
    ]

    resumo_takeaways("m07_prevencao")

    render_quiz(
        modulo_id="m07_prevencao",
        titulo="Prevenção e estilo de vida",
        perguntas=perguntas,
    )

    navegacao_botoes("m07_prevencao")
