"""Módulo 6 — O seu plano cirúrgico. Núcleo do tutorial com dados Antunes 2023."""

import streamlit as st

from components.glossario import termo_inline
from components.graficos import (
    ahi_antes_depois,
    disturbios_pre_op,
    fases_sono_barras_pre_pos,
    gravidade_pre_op_pizza,
    normalizacao_fases_pos,
    responders_vs_non_radar,
)
from components.navegacao import (
    breadcrumb,
    navegacao_botoes,
    objetivos_aprendizagem,
    resumo_takeaways,
)
from components.quiz import Pergunta, render_quiz
from components.recursos import fotografia_clinica, recursos_externos
from components.ui import callout, hero, secao_titulo

RECURSOS_PLANO = [
    {
        "titulo": "Antunes et al. 2023 — paper-âncora",
        "descricao": "Surgical treatment for OSA: effect on sleep architecture. Springer.",
        "url": "https://link.springer.com/article/10.1007/s00405-023-08093-8",
        "tipo": "paper",
    },
    {
        "titulo": "Vicini et al. 2015 — Barbed Reposition Pharyngoplasty",
        "descricao": "A técnica usada na palatoplastia de suspensão.",
        "url": "https://link.springer.com/article/10.1007/s00405-015-3628-3",
        "tipo": "paper",
    },
    {
        "titulo": "AAO-HNS — Patient resources OSA surgery",
        "descricao": "Recursos da American Academy of Otolaryngology.",
        "url": "https://www.entnet.org/resource/sleep-apnea-and-snoring/",
        "tipo": "site",
    },
]


def render() -> None:
    breadcrumb("m06_plano", "Módulo 6 — Plano cirúrgico")

    hero(
        eyebrow="Módulo 6 · Plano cirúrgico",
        titulo="A cirurgia multinível para SAOS — explicada a fundo",
        subtitulo=(
            "As 5 intervenções típicas (septoplastia, microcirurgia "
            "endonasal, turbinoplastia, palatoplastia e amigdalectomia), "
            "fundamentadas em dados reais do paper Antunes et al. 2023."
        ),
    )

    objetivos_aprendizagem("m06_plano")

    secao_titulo(
        eyebrow="Resumo executivo",
        titulo="Os 5 atos cirúrgicos",
    )

    st.markdown(
        """
        | # | Cirurgia | Atua em |
        |---|---|---|
        | 1 | Septoplastia | Septo nasal |
        | 2 | Microcirurgia endonasal bilateral | Cornetos, fossas nasais |
        | 3 | Turbinoplastia / turbinectomia bilateral | Cornetos inferiores |
        | 4 | Palatoplastia para roncopatia | Palato mole, paredes laterais |
        | 5 | Amigdalectomia | Amígdalas palatinas |

        Esta é uma **cirurgia multinível**: três intervenções no nível nasal
        (1+2+3) combinadas com duas intervenções na orofaringe (4+5). É a
        abordagem usada quando a DISE mostra colapso em mais do que um nível
        anatómico.
        """
    )

    callout(
        tipo="info",
        icone="📋",
        titulo="Codificação dos procedimentos",
        corpo=(
            "Em alguns sistemas de saúde, a turbinoplastia (#3) é codificada "
            "<strong>de forma independente</strong>; noutros é considerada "
            "<strong>parte integrante</strong> da microcirurgia endonasal (#2). "
            "Em qualquer caso, a ação cirúrgica é a mesma: reduzir os cornetos "
            "para alargar os meatos."
        ),
    )

    # ─── A coorte do Antunes 2023 ─────────────────────────────────────
    secao_titulo(
        eyebrow="A evidência",
        titulo="A coorte do Antunes et al. 2023",
        subtitulo=(
            "Estudo retrospetivo de 76 adultos submetidos a cirurgia da via "
            "aérea superior para SAOS — base científica que fundamenta a "
            "expectativa de resultado."
        ),
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pacientes", "76", help="55 homens + 21 mulheres")
    with col2:
        st.metric("Idade mediana", "49 anos", help="IQR 41-62")
    with col3:
        st.metric("AHI pré-op", "17.4", help="IQR 11.3-22.9 — moderada")

    st.plotly_chart(gravidade_pre_op_pizza(), use_container_width=True)

    st.plotly_chart(disturbios_pre_op(), use_container_width=True)

    st.markdown(
        """
        **Antes da cirurgia**, 93,4% dos pacientes tinham distribuição anormal
        de pelo menos uma fase do sono. **Mais de 3 em cada 4 dormiam
        demasiado em N1** (sono ligeiro) e quase **40% tinham N3 reduzido**
        (sono profundo restaurador).
        """
    )

    # ─── Resultados ───────────────────────────────────────────────────
    secao_titulo(
        eyebrow="Resultados",
        titulo="O que mudou após cirurgia",
    )

    st.plotly_chart(ahi_antes_depois(), use_container_width=True)

    st.plotly_chart(fases_sono_barras_pre_pos(), use_container_width=True)

    callout(
        tipo="sucesso",
        icone="📊",
        titulo="A grande história — N3 aumentou de forma significativa",
        corpo=(
            "<strong>Tempo em N3 (sono profundo) subiu de 16,9% para 18,9%</strong> "
            "(p = 0.003). Isto representa <strong>~13 minutos extra de sono "
            "profundo restaurador por noite</strong>. Em 365 noites/ano, "
            "&gt;78 horas anuais a mais de N3 — com benefícios cardiovasculares "
            "e cognitivos a longo prazo."
        ),
    )

    st.plotly_chart(normalizacao_fases_pos(), use_container_width=True)

    st.markdown(
        """
        **Como ler este gráfico**: percentagem de pacientes que tinham fase
        anormal antes e que **normalizou** após cirurgia.

        - **REM** foi a fase com **maior taxa de normalização** (63,6%).
        - **N2** seguiu (44,0%).
        - N3 e N1 também tiveram normalizações em proporção significativa.
        """
    )

    # ─── Responders vs Non-responders ─────────────────────────────────
    secao_titulo(
        eyebrow="Realismo",
        titulo="Nem todos respondem igualmente",
        subtitulo=(
            "Critério Sher 1996: 'responder' = redução AHI ≥50% E AHI pós-op &lt;20."
        ),
    )

    termo_inline("ahi_50_responder")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Responders", "75%", "AHI mediano: 10.0")
    with col2:
        st.metric("Non-responders", "25%", "AHI mediano: 24.5", delta_color="inverse")

    st.plotly_chart(responders_vs_non_radar(), use_container_width=True)

    st.markdown(
        """
        **A diferença é clara** entre responders e non-responders:
        - Responders mantêm **menos N1** (10,4%) e **mais N3** (21,2%).
        - Non-responders ficam **presos em N1/N2** com pouco N3.

        Se for non-responder, a estratégia habitual é **CPAP de resgate** —
        muitas vezes mais bem tolerado depois da cirurgia, porque a anatomia
        está melhor (pressões mais baixas necessárias).
        """
    )

    # ─── Cada cirurgia em detalhe ─────────────────────────────────────
    secao_titulo(
        eyebrow="As 5 cirurgias",
        titulo="O que vai acontecer, ato a ato",
    )

    cirurgias = [
        {
            "n": "1",
            "nome": "Septoplastia",
            "termo": "septoplastia",
            "tempo": "30-45 min",
            "anestesia": "Geral",
            "descr": (
                "Acesso por dentro da narina (sem cicatriz visível). O cirurgião "
                "remove ou recoloca as porções desviadas de cartilagem/osso, "
                "preservando a estrutura de suporte. Tampão nasal nas primeiras "
                "24-48h."
            ),
        },
        {
            "n": "2+3",
            "nome": "Microcirurgia endonasal + turbinoplastia bilateral",
            "termo": "turbinectomia",
            "tempo": "20-30 min",
            "anestesia": "Geral (mesma sessão)",
            "descr": (
                "Redução dos cornetos inferiores com radiofrequência ou "
                "microdebridador. Preserva mucosa e função humidificadora. "
                "Faz-se em conjunto com a septoplastia."
            ),
        },
        {
            "n": "4",
            "nome": "Palatoplastia (provavelmente Vicini barbed)",
            "termo": "palatoplastia",
            "tempo": "30-60 min",
            "anestesia": "Geral",
            "descr": (
                "Reposicionamento do palato mole e parede lateral da faringe "
                "com suturas farpadas (sem nós) — técnica descrita por "
                "Vicini 2015 e usada no Antunes 2023. Recuperação: dor "
                "moderada 7-10 dias."
            ),
        },
        {
            "n": "5",
            "nome": "Amigdalectomia por Sluder",
            "termo": "amigdalectomia",
            "tempo": "15-25 min",
            "anestesia": "Geral",
            "descr": (
                "Remoção das amígdalas palatinas com amigdalótomo de Sluder "
                "(técnica clássica, dissecção rápida). Mesma sessão que a "
                "palatoplastia. Recuperação: dor de garganta significativa 7-14 "
                "dias, ouvidos doridos por reflexo."
            ),
        },
    ]

    for c in cirurgias:
        with st.expander(f"**{c['n']}. {c['nome']}** · ⏱️ {c['tempo']} · 💉 {c['anestesia']}"):
            st.markdown(c["descr"])
            termo_inline(c["termo"])

    # ─── Fotografia clínica complementar ─────────────────────────────
    secao_titulo(
        eyebrow="O que é uma amigdalectomia",
        titulo="Fotografia clínica",
    )

    fotografia_clinica(
        ficheiro="foto_tonsilectomia.jpg",
        legenda="Amigdalectomia por coblation — visualização intra-operatória",
        fonte="Wikimedia Commons (CC BY-SA)",
        aviso=(
            "Fotografia clínica de cirurgia. Pode parecer impressionante, mas "
            "é um procedimento de rotina, com a equipa cirúrgica controla "
            "rigorosamente a hemorragia."
        ),
    )

    # ─── Riscos ───────────────────────────────────────────────────────
    secao_titulo(
        eyebrow="Realismo",
        titulo="Riscos e complicações possíveis",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Comuns (esperados)**
            - Dor pós-operatória (gere-se com analgésicos)
            - Inchaço da garganta 3-5 dias
            - Crostas e hemorragia ligeira nasal
            - Voz "abafada" 1-2 semanas
            - Dificuldade temporária a engolir
            """
        )
    with col2:
        st.markdown(
            """
            **Raros mas importantes**
            - Hemorragia significativa (1-3% das amigdalectomias)
            - Insuficiência velofaríngea (regurgitação nasal de líquidos)
            - Alteração permanente da voz
            - Estenose nasofaríngea
            - Reação adversa à anestesia geral
            """
        )

    callout(
        tipo="aviso",
        titulo="Procurar ajuda urgente se",
        corpo=(
            "<ul>"
            "<li>Hemorragia profusa pela boca/nariz nos primeiros 14 dias</li>"
            "<li>Febre &gt;38.5°C que não cede</li>"
            "<li>Falta de ar significativa</li>"
            "<li>Dor que não melhora com analgesia</li>"
            "<li>Sinais de desidratação (incapaz de beber)</li>"
            "</ul>"
            "<strong>Linha SOS do hospital onde foi operado — peça o contacto na consulta pré-operatória.</strong>"
        ),
    )

    # ─── Perguntas para a equipa cirúrgica ────────────────────────────
    secao_titulo(
        eyebrow="Preparação",
        titulo="O que perguntar na consulta pré-operatória",
    )

    st.markdown(
        """
        1. **Que técnica de palatoplastia será usada?** (Vicini barbed, UPPP,
           expansão esfincteriana, ou outra?)
        2. **Qual o grau de Brodsky** das minhas amígdalas?
        3. A **base da língua** foi avaliada na DISE? Qual o grau de colapso?
        4. **Qual a expectativa realista** de redução do AHI no meu caso?
        5. Que **plano B** existe se for non-responder?
        6. **Quando faço a polissonografia de controlo** após a cirurgia?
        7. **Quanto tempo de incapacidade** real para o trabalho?
        8. Existe alternativa à anestesia geral para algum dos atos?
        9. Posso continuar a **medicação habitual** até ao dia da cirurgia?
        10. **Quem contactar** em caso de complicação no pós-operatório?
        """
    )

    recursos_externos(RECURSOS_PLANO)

    perguntas = [
        Pergunta(
            id="m6_q1",
            enunciado=(
                "No paper Antunes 2023, qual foi a redução mediana do AHI após cirurgia?"
            ),
            opcoes=[
                "De 17.4 para 5.0 (~70% redução)",
                "De 17.4 para 13.0 (~25% redução)",
                "De 17.4 para 0 (resolução completa)",
                "Não houve redução estatisticamente significativa",
            ],
            correta=1,
            explicacao=(
                "AHI mediano caiu de **17.4 para 13.0** (~25%). A redução não "
                "foi estatisticamente significativa no grupo total, MAS 75% dos "
                "pacientes foram responders (≥50% redução E AHI &lt;20)."
            ),
        ),
        Pergunta(
            id="m6_q2",
            enunciado=(
                "Que mudança na arquitetura do sono foi estatisticamente "
                "significativa após cirurgia?"
            ),
            opcoes=[
                "Aumento do sono N1",
                "Aumento do tempo total de sono",
                "Aumento do sono N3 (de 16.9% para 18.9%, p=0.003)",
                "Aumento do REM",
            ],
            correta=2,
            explicacao=(
                "**N3 (sono profundo)** subiu significativamente (p=0.003). "
                "É a fase mais restauradora — implica benefícios cardiovasculares "
                "e cognitivos a longo prazo."
            ),
        ),
        Pergunta(
            id="m6_q3",
            enunciado=(
                "Os 'non-responders' à cirurgia (25% dos casos) têm tipicamente:"
            ),
            opcoes=[
                "AHI pós-op normal",
                "AHI pós-op alto (mediana 24.5) e mais tempo em N1",
                "Resolução completa dos sintomas",
                "Necessidade de reverter a cirurgia",
            ],
            correta=1,
            explicacao=(
                "Non-responders mantêm AHI elevado (mediana 24.5) e ficam "
                "presos em sono ligeiro (N1/N2) com pouco N3. Estratégia "
                "habitual: CPAP de resgate."
            ),
        ),
        Pergunta(
            id="m6_q4",
            enunciado=(
                "Numa cirurgia multinível para SAOS, a turbinoplastia bilateral "
                "é frequentemente:"
            ),
            opcoes=[
                "Feita numa cirurgia separada noutra data",
                "Realizada na mesma sessão da microcirurgia endonasal",
                "Substituída por medicação tópica",
                "Adiada para depois da palatoplastia cicatrizar",
            ],
            correta=1,
            explicacao=(
                "A redução dos cornetos é tecnicamente parte da microcirurgia "
                "endonasal e <strong>realiza-se na mesma sessão</strong>, "
                "minimizando exposições cirúrgicas e custos para o paciente."
            ),
        ),
    ]

    resumo_takeaways("m06_plano")

    render_quiz(
        modulo_id="m06_plano",
        titulo="O seu plano cirúrgico",
        perguntas=perguntas,
    )

    navegacao_botoes("m06_plano")
