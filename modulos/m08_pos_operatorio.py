"""Módulo 8 — Pós-operatório e seguimento."""

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

RECURSOS_POS = [
    {
        "titulo": "AAO-HNS — Tonsillectomy Recovery",
        "descricao": "Guia oficial da American Academy of Otolaryngology.",
        "url": "https://www.entnet.org/resource/tonsillectomy/",
        "tipo": "guia",
    },
    {
        "titulo": "Mayo Clinic — Septoplasty Recovery",
        "descricao": "Recuperação típica e sinais de alerta.",
        "url": "https://www.mayoclinic.org/tests-procedures/septoplasty/about/pac-20384670",
        "tipo": "site",
    },
    {
        "titulo": "Antunes 2023 — Avaliação de seguimento",
        "descricao": "Polissonografia de controlo e responder vs non-responder.",
        "url": "https://link.springer.com/article/10.1007/s00405-023-08093-8",
        "tipo": "paper",
    },
]


def render() -> None:
    breadcrumb("m08_pos_op", "Módulo 8 — Pós-operatório")

    hero(
        eyebrow="Módulo 8 · Pós-operatório",
        titulo="Os 90 dias após a cirurgia — e o que vem depois",
        subtitulo=(
            "Calendário detalhado de recuperação, sinais de alerta, "
            "polissonografia de controlo e seguimento de longo prazo."
        ),
    )

    objetivos_aprendizagem("m08_pos_op")

    secao_titulo(
        eyebrow="Antes",
        titulo="Preparação na semana anterior",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Logística**
            - 🛒 Comprar **gelados, gelatina, sopas frias, iogurtes**
            - 💊 Confirmar **prescrições de analgesia** (paracetamol, AINE, opióide leve se prescrito)
            - 🛏️ Preparar **cama elevada** (cabeceira a 30°)
            - 🧊 **Bolsas de gelo** para o pescoço
            - 🚗 Combinar **boleia** para o regresso a casa (não pode conduzir)
            """
        )
    with col2:
        st.markdown(
            """
            **Médico**
            - ⏸️ **Suspender anticoagulantes/antiagregantes** se indicado
              (não suspender por iniciativa própria — confirmar com a equipa)
            - 🚭 **Não fumar** pelo menos 2 semanas antes
            - 🍷 **Sem álcool** 48h antes
            - 💧 **Hidratação adequada** dias antes
            - 🍴 **Jejum 8h** pré-cirurgia (anestesia geral)
            """
        )

    secao_titulo(
        eyebrow="Dia 0",
        titulo="O dia da cirurgia",
    )

    st.markdown(
        """
        ### Sequência típica

        1. **Chegada ao hospital**: 1-2h antes da cirurgia
        2. **Avaliação anestésica**: confirmação de sinais vitais, ECG, último briefing
        3. **Cirurgia**: 90-120 min totais (todos os atos juntos)
        4. **Recobro**: 1-2h em sala de recuperação pós-anestésica
        5. **Internamento**: 1 dia (alta no dia seguinte)
        6. **Casa**: regresso com prescrição e marcação de revisão

        ### O que vai sentir nas primeiras horas

        - Dor de garganta significativa (já com analgesia)
        - Voz "abafada" ou diferente
        - Algum ranger no nariz / sangue residual
        - Náusea pós-anestésica (ondansetron ajuda)
        - Sonolência da anestesia
        """
    )

    callout(
        tipo="info",
        icone="🏥",
        titulo="Internamento típico",
        corpo=(
            "Cirurgia multinível para SAOS implica habitualmente "
            "<strong>1 dia de internamento</strong>, com equipa cirúrgica "
            "completa (cirurgião principal + ajudante + instrumentista + "
            "anestesista). Confirme com o seu seguro de saúde os termos "
            "exatos da cobertura (copagamentos, plafond, equipa coberta)."
        ),
    )

    secao_titulo(
        eyebrow="Calendário",
        titulo="Os 90 dias pós-operatório",
    )

    fases_recup = [
        {
            "periodo": "Dias 1-3",
            "cor": "#dc2626",
            "titulo": "Pico de dor",
            "descr": (
                "Dor de garganta intensa, sobretudo a engolir. Cuide-se com "
                "analgésicos pautados (não 'à medida da dor')."
            ),
            "cuidados": [
                "Líquidos frios e gelados (anestesia local)",
                "Analgesia regular: paracetamol + AINE alternados",
                "Hidratação 2L+ por dia",
                "Cabeça elevada para dormir",
                "Sem esforço físico, sem inclinar para a frente",
            ],
        },
        {
            "periodo": "Dias 4-7",
            "cor": "#d97706",
            "titulo": "Crostas",
            "descr": (
                "Forma-se uma crosta esbranquiçada no leito amigdaliano "
                "(normal, não é infeção). A dor pode até **aumentar** ao 5º-7º "
                "dia quando as crostas começam a soltar-se."
            ),
            "cuidados": [
                "Continuar analgesia regular",
                "Comida mole — purés, ovos mexidos, peixe cozido",
                "Bochechos com soro fisiológico (não enxaguante alcoólico)",
                "Atenção a sinais de hemorragia",
            ],
        },
        {
            "periodo": "Dias 7-14",
            "cor": "#ca8a04",
            "titulo": "Recuperação progressiva",
            "descr": (
                "A dor diminui gradualmente. Voz volta ao normal. Reintrodução "
                "progressiva de alimentos sólidos."
            ),
            "cuidados": [
                "Reintroduzir sólidos macios",
                "Atividade leve — caminhadas curtas",
                "Sem esforço, sem desporto, sem voar",
                "Ainda atento a hemorragia (pico de risco entre dias 5-10)",
            ],
        },
        {
            "periodo": "Semanas 3-6",
            "cor": "#65a30d",
            "titulo": "Cicatrização",
            "descr": (
                "Tecido cicatricial forma-se. Voz pode soar ligeiramente "
                "diferente algumas semanas. Retoma de atividade normal."
            ),
            "cuidados": [
                "Retomar alimentação normal",
                "Voltar ao trabalho (típico: 2-3 semanas para sedentário)",
                "Exercício físico ligeiro a partir de 3 semanas",
                "Voltar ao desporto pleno aos 30-45 dias",
            ],
        },
        {
            "periodo": "Mês 2-3",
            "cor": "#0891b2",
            "titulo": "Adaptação final",
            "descr": (
                "A nova anatomia estabiliza. O efeito completo da cirurgia "
                "pode demorar até 3 meses para se manifestar."
            ),
            "cuidados": [
                "Vida normal sem restrições",
                "Continuar bons hábitos do Módulo 7",
                "Avaliar subjetivamente: melhor sono? menos sonolência? menos ronco?",
            ],
        },
    ]

    for f in fases_recup:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown(
                f"""
<div style="background:{f['cor']};padding:1rem;border-radius:12px;text-align:center;">
  <div style="font-size:0.8rem;color:white;font-weight:600;">{f['periodo']}</div>
  <div style="font-size:1.1rem;color:white;font-weight:700;margin-top:0.2rem;">
    {f['titulo']}
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(f["descr"])
            st.markdown("**Cuidados:**")
            for c in f["cuidados"]:
                st.markdown(f"- {c}")

    secao_titulo(
        eyebrow="Alarmes",
        titulo="Sinais de alerta — quando ligar / ir ao SU",
    )

    callout(
        tipo="perigo",
        icone="🚨",
        titulo="Procurar ajuda urgente (Serviço de Urgência) se:",
        corpo=(
            "<ul>"
            "<li><strong>Hemorragia significativa</strong> pela boca ou nariz "
            "(sangue vermelho vivo, contínuo, &gt;1 colher de sopa)</li>"
            "<li><strong>Febre &gt;38.5°C</strong> que não cede com antipirético</li>"
            "<li><strong>Falta de ar</strong> ou dificuldade respiratória nova</li>"
            "<li><strong>Dor incontrolável</strong> apesar de analgesia</li>"
            "<li><strong>Sinais de desidratação</strong>: incapaz de beber líquidos &gt;12h, "
            "muito pouca urina, tonturas ao levantar</li>"
            "<li><strong>Vómitos persistentes</strong> com sangue</li>"
            "</ul>"
            "<strong>Hospital onde foi operado</strong>: peça o número de SOS "
            "na consulta pré-op."
        ),
    )

    callout(
        tipo="aviso",
        titulo="Contactar a equipa cirúrgica (não-urgente)",
        corpo=(
            "<ul>"
            "<li>Hemorragias pequenas mas repetidas</li>"
            "<li>Dor que aumenta após o 7º dia (pode ser infeção)</li>"
            "<li>Voz nasalada que persiste (regurgitação nasal)</li>"
            "<li>Mau hálito persistente além de 3 semanas</li>"
            "<li>Dúvidas sobre medicação ou alimentação</li>"
            "</ul>"
        ),
    )

    secao_titulo(
        eyebrow="Avaliação",
        titulo="Polissonografia de controlo",
    )

    st.markdown(
        """
        ### Quando

        Tipicamente **3-6 meses pós-cirurgia**, para avaliar:
        - **AHI** atual vs pré-cirurgia (responder ou non-responder?)
        - **Arquitetura do sono** (mais N3, menos N1?)
        - **Necessidade de tratamento adicional** (CPAP de resgate?)

        ### O que pode acontecer

        | Resultado | O que significa | Próximo passo |
        |---|---|---|
        | **Responder** (≥50% redução, AHI &lt;20) | Cirurgia funcionou | Manter, reavaliar anualmente |
        | **Non-responder** | Resultado abaixo do esperado | **CPAP** ou cirurgia adicional |
        | **AHI normal** (&lt;5) | Excelente — resolução completa | Vigilância, focar prevenção |
        """
    )

    callout(
        tipo="info",
        icone="🎯",
        titulo="Sobre os 25% non-responders",
        corpo=(
            "Se for non-responder, <strong>não é falha sua nem da equipa</strong>. "
            "A SAOS multinível é complexa, e mesmo com DISE pode haver colapso "
            "em locais não previstos. <strong>O CPAP de resgate</strong> é "
            "frequentemente <em>melhor tolerado depois</em> da cirurgia, porque "
            "a anatomia melhorou — pressões mais baixas são suficientes."
        ),
    )

    secao_titulo(
        eyebrow="Longo prazo",
        titulo="Seguimento ao longo dos anos",
    )

    st.markdown(
        """
        ### Anual

        - **Polissonografia** se sintomas voltarem
        - **Avaliação cardiovascular**: tensão, lípidos, glicemia
        - **Peso e perímetro do pescoço** — controlo de fatores de risco
        - **Questionário de Epworth** — sonolência subjetiva

        ### Quando recorrer de novo à equipa

        - **Recidiva** de sintomas (ronco volta, fadiga aumenta)
        - **Ganho de peso significativo** (5+ kg)
        - **Eventos cardiovasculares** novos
        - **Dúvidas** sobre tratamento adicional
        """
    )

    callout(
        tipo="sucesso",
        icone="🎓",
        titulo="Concluiu o tutorial",
        corpo=(
            "Da introdução ao seguimento de longo prazo. Está agora preparado "
            "para uma <strong>conversa informada com a sua equipa cirúrgica</strong>, "
            "com perguntas concretas e expectativas realistas. "
            "<strong>Boa sorte com a cirurgia.</strong>"
        ),
    )

    recursos_externos(RECURSOS_POS)

    perguntas = [
        Pergunta(
            id="m8_q1",
            enunciado="Em que período a dor pós-amigdalectomia tende a ser pior?",
            opcoes=[
                "Imediatamente após a cirurgia (dia 0)",
                "Dias 5-7 (quando as crostas se soltam)",
                "Mês 2-3 (durante a cicatrização final)",
                "Não há picos — é constante",
            ],
            correta=1,
            explicacao=(
                "A dor pode **piorar entre os dias 5-7** quando as crostas "
                "começam a soltar-se. Isto é normal mas frequentemente "
                "surpreende os pacientes. Manter analgesia regular, não 'à medida'."
            ),
        ),
        Pergunta(
            id="m8_q2",
            enunciado="Qual destes é um sinal que justifica IDA AO SU urgente?",
            opcoes=[
                "Voz ligeiramente abafada nos primeiros 5 dias",
                "Crostas brancas no fundo da garganta",
                "Hemorragia significativa pela boca",
                "Mau hálito",
            ],
            correta=2,
            explicacao=(
                "**Hemorragia significativa** (sangue vivo, contínuo) pode "
                "ser uma emergência cirúrgica. Voz abafada, crostas e mau "
                "hálito são todos esperados e não-urgentes."
            ),
        ),
        Pergunta(
            id="m8_q3",
            enunciado="Quando se faz tipicamente a polissonografia de controlo após cirurgia?",
            opcoes=[
                "1 semana",
                "1 mês",
                "3-6 meses",
                "1 ano",
            ],
            correta=2,
            explicacao=(
                "**3-6 meses** é o intervalo típico — dá tempo à anatomia "
                "para estabilizar e ao paciente para retomar vida normal."
            ),
        ),
        Pergunta(
            id="m8_q4",
            enunciado="Se for 'non-responder' à cirurgia (25% no Antunes 2023), o passo seguinte habitual é:",
            opcoes=[
                "Reverter a cirurgia",
                "Aceitar o resultado e não fazer mais nada",
                "Considerar CPAP de resgate (frequentemente melhor tolerado depois)",
                "Cirurgia bariátrica imediata",
            ],
            correta=2,
            explicacao=(
                "**CPAP de resgate**. Curiosamente, é frequentemente melhor "
                "tolerado pós-cirurgia, porque pressões mais baixas são "
                "suficientes (anatomia melhorou)."
            ),
        ),
    ]

    resumo_takeaways("m08_pos_op")

    render_quiz(
        modulo_id="m08_pos_op",
        titulo="Pós-operatório e seguimento",
        perguntas=perguntas,
    )

    navegacao_botoes("m08_pos_op")
