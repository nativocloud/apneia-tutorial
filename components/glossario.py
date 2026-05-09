"""Glossário de termos médicos — fonte única e componentes UI.

Filosofia: cada termo médico é definido uma vez, em linguagem acessível, e
pode ser referenciado em qualquer módulo. Aparece como expander inline com
ícone 📖 e cor consistente.
"""

from dataclasses import dataclass

import streamlit as st


@dataclass
class Termo:
    nome: str
    definicao: str
    detalhe: str = ""
    sinonimos: list[str] | None = None
    categoria: str = "Geral"


GLOSSARIO: dict[str, Termo] = {
    # ─── Anatomia ─────────────────────────────────────────────────────
    "cornetos": Termo(
        nome="Cornetos nasais (turbinas / conchas nasais)",
        definicao=(
            "Três 'prateleiras' horizontais de mucosa em cada fossa nasal "
            "(superior, médio, inferior). Aquecem, humidificam e filtram o ar inspirado."
        ),
        detalhe=(
            "São constituídos por osso revestido por mucosa muito vascularizada. "
            "O **corneto inferior** é o maior — é o que mais frequentemente bloqueia "
            "a passagem do ar quando hipertrofiado."
        ),
        sinonimos=["turbinas", "conchas nasais", "turbinates", "nasal conchae"],
        categoria="Anatomia",
    ),
    "meatos": Termo(
        nome="Meatos nasais",
        definicao=(
            "Os **espaços de ar entre os cornetos**. É por aqui que o ar passa. "
            "Cada fossa nasal tem 3: superior, médio e inferior."
        ),
        detalhe=(
            "Quando os cornetos incham (rinite, alergia), os meatos fecham — daí "
            "a sensação de 'nariz tapado'. A turbinoplastia abre os meatos reduzindo "
            "o tamanho dos cornetos."
        ),
        sinonimos=["meatuses", "nasal meatuses"],
        categoria="Anatomia",
    ),
    "septo": Termo(
        nome="Septo nasal",
        definicao=(
            "A **parede vertical** de osso (atrás) e cartilagem (à frente) que **separa "
            "as duas fossas nasais**."
        ),
        detalhe=(
            "Idealmente é reto. Quando desviado (muito comum, até 80% da população), "
            "uma narina trabalha mais que a outra, gera turbulência e força respiração "
            "bucal. A **septoplastia** corrige o desvio sem cicatriz visível."
        ),
        sinonimos=["nasal septum"],
        categoria="Anatomia",
    ),
    "palato_mole": Termo(
        nome="Palato mole",
        definicao=(
            "A parte **flexível** do céu da boca — atrás do palato duro (osso). "
            "É músculo + tecido conjuntivo, sem osso."
        ),
        detalhe=(
            "Por ser flexível, **vibra** com a passagem do ar (causa o ronco) e em "
            "casos mais graves **colapsa** contra a parede da faringe (causa apneia). "
            "É alvo da palatoplastia."
        ),
        sinonimos=["soft palate", "véu palatino"],
        categoria="Anatomia",
    ),
    "uvula": Termo(
        nome="Úvula",
        definicao="A 'campainha' que pendura no fim do palato mole.",
        detalhe=(
            "Em SAOS comporta-se como um pêndulo no caminho do ar. Quando alongada/"
            "edemaciada, contribui para o ronco e o colapso. Algumas técnicas de "
            "palatoplastia removem ou reposicionam parcialmente a úvula."
        ),
        sinonimos=["uvula", "campainha"],
        categoria="Anatomia",
    ),
    "amigdalas": Termo(
        nome="Amígdalas (palatinas)",
        definicao=(
            "Duas massas de **tecido linfoide** nas paredes laterais da garganta, "
            "atrás dos pilares amigdalinos."
        ),
        detalhe=(
            "Em adultos raramente têm função imune relevante. Quando hipertrofiadas "
            "(graus III-IV de Brodsky), são obstáculos físicos na orofaringe — "
            "alvo da **amigdalectomia**."
        ),
        sinonimos=["palatine tonsils"],
        categoria="Anatomia",
    ),
    "epiglote": Termo(
        nome="Epiglote",
        definicao=(
            "Cartilagem em forma de pétala que **fecha a entrada da laringe** "
            "quando engolimos, para a comida não ir aos pulmões."
        ),
        detalhe=(
            "Em alguns pacientes pode colapsar para trás durante o sono, "
            "agravando a apneia. Em ~9% dos casos do paper Antunes 2023, foi feita "
            "epiglotectomia parcial."
        ),
        sinonimos=["epiglottis"],
        categoria="Anatomia",
    ),
    "faringe": Termo(
        nome="Faringe",
        definicao="O tubo muscular que vai do fundo do nariz à entrada do esófago.",
        detalhe=(
            "Divide-se em 3 zonas: **nasofaringe** (atrás do nariz), **orofaringe** "
            "(atrás da boca — onde estão amígdalas, palato, úvula) e **laringofaringe** "
            "(atrás da laringe). A SAOS afeta principalmente a orofaringe."
        ),
        sinonimos=["pharynx"],
        categoria="Anatomia",
    ),
    # ─── Cirurgias ────────────────────────────────────────────────────
    "turbinectomia": Termo(
        nome="Turbinectomia / Turbinoplastia",
        definicao=(
            "Cirurgia de **redução dos cornetos** nasais (geralmente o inferior) "
            "para alargar os meatos e melhorar a passagem do ar."
        ),
        detalhe=(
            "**Turbinoplastia** = redução conservadora (preserva mucosa e osso). "
            "**Turbinectomia** = remoção mais agressiva. Hoje prefere-se a turbinoplastia "
            "por preservar a função humidificadora e aquecedora do ar — turbinectomia "
            "radical pode causar 'síndrome do nariz vazio'."
        ),
        sinonimos=["turbinoplasty", "turbinectomy"],
        categoria="Cirurgia",
    ),
    "septoplastia": Termo(
        nome="Septoplastia",
        definicao=(
            "Cirurgia de **correção do septo nasal desviado**. Acesso por dentro "
            "da narina (sem cicatriz visível)."
        ),
        detalhe=(
            "O cirurgião remove ou recoloca as porções desviadas de cartilagem/osso, "
            "preservando a estrutura de suporte. Recuperação típica: 1-2 semanas com "
            "tampão nasal nos primeiros dias."
        ),
        sinonimos=["septoplasty"],
        categoria="Cirurgia",
    ),
    "palatoplastia": Termo(
        nome="Palatoplastia (para roncopatia)",
        definicao=(
            "Cirurgia que **remodela o palato mole e a parede lateral da faringe** "
            "para os tornar mais firmes e alargar a via aérea."
        ),
        detalhe=(
            "Várias técnicas: **UPPP clássica** (remove tecido), **palatoplastia "
            "lateral / Vicini barbed** (reposiciona com suturas farpadas — usada no "
            "paper Antunes 2023), **expansão esfincteriana**. Cada uma tem perfis "
            "diferentes de risco e recuperação."
        ),
        sinonimos=["palatoplasty", "UPPP", "barbed reposition pharyngoplasty"],
        categoria="Cirurgia",
    ),
    "amigdalectomia": Termo(
        nome="Amigdalectomia",
        definicao="Cirurgia de **remoção das amígdalas palatinas**.",
        detalhe=(
            "**'Por Sluder'** é a técnica clássica com amigdalótomo (rápida, sob "
            "anestesia geral). Outras técnicas: dissecção fria, eletrocirurgia, "
            "coblation. Recuperação típica: 7-14 dias com dor de garganta significativa."
        ),
        sinonimos=["tonsillectomy"],
        categoria="Cirurgia",
    ),
    # ─── Diagnóstico ──────────────────────────────────────────────────
    "psg": Termo(
        nome="Polissonografia (PSG)",
        definicao=(
            "**Exame de referência** para diagnóstico de SAOS. Mede ondas cerebrais "
            "(EEG), movimentos oculares, tónus muscular, fluxo respiratório, esforço "
            "respiratório, oxigenação e ECG durante uma noite de sono."
        ),
        detalhe=(
            "Existem 4 níveis: nível I (laboratório com técnico), nível II (laboratório "
            "sem técnico — usado no Antunes 2023), nível III (em casa, parâmetros "
            "respiratórios + SpO₂), nível IV (apenas SpO₂)."
        ),
        sinonimos=["polysomnography", "estudo do sono"],
        categoria="Diagnóstico",
    ),
    "ahi": Termo(
        nome="AHI — Apnea-Hypopnea Index",
        definicao=(
            "**Número de apneias + hipopneias por hora de sono**. É a métrica "
            "principal de gravidade da SAOS."
        ),
        detalhe=(
            "Classificação (AASM): **<5** normal · **5-15** ligeira · **15-30** moderada · "
            "**≥30** grave. No paper Antunes 2023, AHI mediano pré-op = 17.4 (moderada), "
            "pós-op = 13.0."
        ),
        sinonimos=["AHI", "índice de apneia-hipopneia", "IAH"],
        categoria="Diagnóstico",
    ),
    "odi": Termo(
        nome="ODI — Oxygen Desaturation Index",
        definicao=(
            "Número de **dessaturações de oxigénio ≥3% (ou ≥4%) por hora de sono**. "
            "Indicador da carga hipoxémica da SAOS."
        ),
        sinonimos=["ODI", "índice de dessaturação"],
        categoria="Diagnóstico",
    ),
    "spo2": Termo(
        nome="SpO₂ — Saturação periférica de oxigénio",
        definicao=(
            "Percentagem de hemoglobina ligada a oxigénio, medida no dedo (oxímetro). "
            "Normal: 95-100%. Em apneias pode cair para 80% ou menos."
        ),
        sinonimos=["SpO2"],
        categoria="Diagnóstico",
    ),
    "dise": Termo(
        nome="DISE — Drug-Induced Sleep Endoscopy",
        definicao=(
            "**Endoscopia da via aérea com o paciente sob sedação leve** (que mimetiza "
            "o sono). Permite ver onde a via aérea colapsa — fundamental para escolher "
            "a cirurgia certa."
        ),
        detalhe=(
            "É feita no bloco operatório com propofol em perfusão controlada por bispectral "
            "(BIS 50-70). O cirurgião grava o vídeo e classifica o colapso por nível "
            "anatómico (escala VOTE)."
        ),
        sinonimos=["drug-induced sleep endoscopy"],
        categoria="Diagnóstico",
    ),
    "ess": Termo(
        nome="ESS — Epworth Sleepiness Scale",
        definicao=(
            "Questionário de 8 perguntas que avalia a **sonolência diurna**. "
            "Pontuação 0-24."
        ),
        detalhe=(
            "**0-10** normal · **11-12** sonolência ligeira · **13-15** moderada · "
            "**16-24** grave. Não diagnostica SAOS sozinha — é um indicador de "
            "sintomas diurnos."
        ),
        sinonimos=["Epworth"],
        categoria="Diagnóstico",
    ),
    "stop_bang": Termo(
        nome="STOP-BANG",
        definicao=(
            "Questionário de **rastreio** de SAOS com 8 perguntas (Snoring, Tiredness, "
            "Observed apnea, blood Pressure, BMI, Age, Neck circumference, Gender)."
        ),
        detalhe=(
            "Pontuação ≥3 sugere risco intermédio; ≥5 risco elevado. Útil em medicina "
            "geral antes de pedir polissonografia."
        ),
        categoria="Diagnóstico",
    ),
    # ─── Tratamentos ──────────────────────────────────────────────────
    "cpap": Termo(
        nome="CPAP — Continuous Positive Airway Pressure",
        definicao=(
            "**Tratamento de primeira linha para SAOS**. Máquina que insufla ar "
            "ligeiramente pressurizado por máscara (nasal ou facial), mantendo a "
            "via aérea aberta durante o sono."
        ),
        detalhe=(
            "Pressões típicas: 5-15 cmH₂O. Adesão é o ponto fraco — apenas 30-50% "
            "dos pacientes usam o suficiente (≥4h/noite, 70% dos dias). Quando o "
            "CPAP falha ou é mal tolerado, considera-se a cirurgia."
        ),
        sinonimos=["CPAP", "continuous positive airway pressure"],
        categoria="Tratamento",
    ),
    "ahi_50_responder": Termo(
        nome="Responder vs Non-responder cirúrgico",
        definicao=(
            "**Responder**: paciente com **redução ≥50% do AHI E AHI pós-op <20** "
            "(critério Sher 1996, ainda muito usado)."
        ),
        detalhe=(
            "No paper Antunes 2023: 75% foram responders. Non-responders mantêm "
            "AHI alto e geralmente precisam de CPAP de resgate."
        ),
        categoria="Tratamento",
    ),
    # ─── Fases do sono ────────────────────────────────────────────────
    "fases_sono": Termo(
        nome="Fases do sono (N1, N2, N3, REM)",
        definicao=(
            "O sono divide-se em 4 fases que se alternam ao longo da noite em "
            "ciclos de ~90 minutos."
        ),
        detalhe=(
            "**N1** (5%) sono superficial, transição da vigília. "
            "**N2** (45-55%) sono ligeiro, a maior parte. "
            "**N3** (15-25%) sono profundo / SWS — restaurador físico. "
            "**REM** (20-25%) sonhos, consolidação da memória. "
            "Em SAOS, N3 e REM ficam reduzidos pelas micro-despertares."
        ),
        sinonimos=["sleep stages", "arquitetura do sono"],
        categoria="Sono",
    ),
}


def termo_inline(chave: str) -> None:
    """Renderiza um termo do glossário como expander inline.

    Uso:
        st.markdown("Vamos falar de cornetos.")
        termo_inline("cornetos")
    """
    t = GLOSSARIO.get(chave)
    if not t:
        st.error(f"Termo não encontrado no glossário: '{chave}'")
        return

    with st.expander(f"📖 **{t.nome}** — clique para definição"):
        st.markdown(f"**{t.definicao}**")
        if t.detalhe:
            st.markdown(t.detalhe)
        if t.sinonimos:
            st.caption(f"Também conhecido como: *{', '.join(t.sinonimos)}*")


def lista_termos(categoria: str | None = None) -> None:
    """Renderiza uma lista de termos, opcionalmente filtrada por categoria."""
    termos = list(GLOSSARIO.values())
    if categoria:
        termos = [t for t in termos if t.categoria == categoria]

    for t in termos:
        with st.container(border=True):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(
                    f"<span style='display:inline-block;background:#dbeafe;color:#1e40af;"
                    f"padding:0.15rem 0.5rem;border-radius:4px;font-size:0.7rem;"
                    f"font-weight:600;'>{t.categoria}</span>",
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(f"**{t.nome}**")
                st.markdown(t.definicao)
                if t.detalhe:
                    with st.expander("Detalhe"):
                        st.markdown(t.detalhe)


def pagina_glossario_completa() -> None:
    """Página de glossário completo, agrupada por categoria."""
    categorias = sorted({t.categoria for t in GLOSSARIO.values()})

    tabs = st.tabs(categorias)
    for tab, cat in zip(tabs, categorias, strict=False):
        with tab:
            lista_termos(categoria=cat)
