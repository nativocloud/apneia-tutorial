"""Navegação entre módulos: metadata, breadcrumb, botões anterior/próximo."""

import streamlit as st


# Lista canónica de módulos com metadata e-learning completa.
# Mantida em sintonia com app.py
ORDEM_MODULOS: list[dict] = [
    {
        "id": "m00_intro",
        "label": "0. Comece aqui",
        "titulo": "Comece aqui",
        "icone": "🧭",
        "tempo_min": 5,
        "descricao": "Visão geral, motivação e roadmap.",
        "prerequisitos": [],
        "objetivos": [
            "Compreender o que é a apneia obstrutiva do sono em uma frase",
            "Saber porque importa tratar (consequências sistémicas)",
            "Conhecer a estrutura do tutorial (9 módulos)",
        ],
        "takeaways": [
            "A SAOS é um problema mecânico da via aérea superior, não dos pulmões.",
            "Cada apneia provoca queda de O₂ + pico de adrenalina + fragmentação do sono.",
            "Tratar a SAOS reduz risco cardiovascular, cognitivo e metabólico.",
        ],
    },
    {
        "id": "m01_anatomia",
        "label": "1. Anatomia das vias aéreas",
        "titulo": "Anatomia das vias aéreas",
        "icone": "🫁",
        "tempo_min": 8,
        "descricao": "Cornetos, septo, palato, amígdalas — onde fica o quê.",
        "prerequisitos": ["m00_intro"],
        "objetivos": [
            "Identificar as 8 estruturas-chave da via aérea superior",
            "Distinguir cornetos vs meatos vs septo nasal",
            "Mapear cada cirurgia à estrutura sobre que atua",
        ],
        "takeaways": [
            "Há 3 cornetos por fossa nasal — o inferior é o que mais bloqueia.",
            "Os meatos são os espaços entre os cornetos — por aí passa o ar.",
            "A orofaringe é o nível onde a palatoplastia e amigdalectomia atuam.",
            "O palato mole vibra (ronco) e colapsa (apneia) por não ter osso.",
        ],
    },
    {
        "id": "m02_sono",
        "label": "2. Como dormimos",
        "titulo": "Como dormimos",
        "icone": "🌙",
        "tempo_min": 6,
        "descricao": "Fases do sono N1, N2, N3 e REM. Porque importam.",
        "prerequisitos": ["m00_intro"],
        "objetivos": [
            "Distinguir as 4 fases do sono (N1, N2, N3, REM)",
            "Compreender a função restauradora de cada fase",
            "Ler um hipnograma e identificar sono fragmentado",
        ],
        "takeaways": [
            "N3 (sono profundo) = restauração física + limpeza glinfática.",
            "REM = consolidação de memória + regulação emocional.",
            "SAOS impede o cérebro de chegar a N3/REM — fragmentação.",
            "Antunes 2023: cirurgia aumentou N3 de 16,9% para 18,9% (p=0.003).",
        ],
    },
    {
        "id": "m03_saos",
        "label": "3. O que é a SAOS",
        "titulo": "O que é a SAOS",
        "icone": "🩺",
        "tempo_min": 10,
        "descricao": "Fisiopatologia, sintomas e fatores de risco.",
        "prerequisitos": ["m01_anatomia", "m02_sono"],
        "objetivos": [
            "Distinguir apneia obstrutiva, central e mista",
            "Compreender os 3 tipos de eventos (apneia, hipopneia, RERA)",
            "Reconhecer fatores de risco e variantes (REM-OSA)",
        ],
        "takeaways": [
            "SAOS é mecânica: cérebro manda respirar, mas a via aérea bloqueia.",
            "REM-OSA pode ter AHI total baixo mas alto impacto cardiovascular.",
            "Tabaco aumenta risco — efeito persiste em ex-fumadores (Krüger 2026).",
            "12+ fatores de risco conhecidos — peso e idade são os principais.",
        ],
    },
    {
        "id": "m04_diagnostico",
        "label": "4. Diagnóstico",
        "titulo": "Diagnóstico",
        "icone": "📊",
        "tempo_min": 8,
        "descricao": "Polissonografia, AHI, escalas, DISE — os exames.",
        "prerequisitos": ["m03_saos"],
        "objetivos": [
            "Conhecer o caminho diagnóstico (rastreio → PSG → DISE)",
            "Interpretar AHI, ODI e classificação de gravidade AASM",
            "Compreender a classificação VOTE da DISE",
        ],
        "takeaways": [
            "AHI ≥15 = SAOS moderada · AHI ≥30 = grave (AASM 2023).",
            "Polissonografia é o exame de referência (níveis I-IV).",
            "DISE mapeia onde a via aérea colapsa — VOTE: Velum, Orofaringe, Tongue, Epiglote.",
            "Sem DISE, escolher cirurgia seria às cegas.",
        ],
    },
    {
        "id": "m05_tratamentos",
        "label": "5. Tratamentos disponíveis",
        "titulo": "Tratamentos disponíveis",
        "icone": "💊",
        "tempo_min": 10,
        "descricao": "CPAP, aparelhos orais, cirurgia, estilo de vida.",
        "prerequisitos": ["m04_diagnostico"],
        "objetivos": [
            "Conhecer todas as opções terapêuticas para SAOS",
            "Compreender vantagens e limites do CPAP (gold standard)",
            "Saber quando se considera cirurgia",
        ],
        "takeaways": [
            "CPAP é primeira linha (>90% redução AHI) mas adesão é fraca (30-50%).",
            "Aparelhos orais (MAD) — alternativa em SAOS ligeira-moderada.",
            "Cirurgia indicada quando CPAP falha ou DISE mostra alvo claro.",
            "Antunes 2023: 75% responders à cirurgia multinível.",
        ],
    },
    {
        "id": "m06_plano",
        "label": "6. Plano cirúrgico multinível",
        "titulo": "Plano cirúrgico multinível",
        "icone": "🔬",
        "tempo_min": 12,
        "descricao": "As 5 intervenções com dados reais do Antunes 2023.",
        "prerequisitos": ["m05_tratamentos"],
        "objetivos": [
            "Conhecer as 5 intervenções da cirurgia multinível",
            "Interpretar os resultados quantitativos do Antunes 2023",
            "Identificar perfil responder vs non-responder",
            "Listar perguntas concretas para a consulta pré-operatória",
        ],
        "takeaways": [
            "Cirurgia multinível: 3 atos nasais + 2 atos orofaríngeos.",
            "AHI mediano cai de 17,4 para 13,0; N3 sobe de 16,9% para 18,9%.",
            "75% responders (AHI cai ≥50%); 25% non-responders precisam CPAP.",
            "Riscos comuns são geríveis; raros mas importantes a conhecer.",
        ],
    },
    {
        "id": "m07_prevencao",
        "label": "7. Prevenção e estilo de vida",
        "titulo": "Prevenção e estilo de vida",
        "icone": "🏃",
        "tempo_min": 8,
        "descricao": "Peso, álcool, tabaco, posição, exercícios.",
        "prerequisitos": ["m03_saos"],
        "objetivos": [
            "Identificar os 7 pilares de prevenção/coadjuvância",
            "Compreender o impacto quantitativo de cada pilar",
            "Aplicar 5 ações concretas no dia-a-dia",
        ],
        "takeaways": [
            "Perder 10% do peso reduz AHI em ~25%.",
            "Álcool ao deitar e benzodiazepinas pioram SAOS.",
            "Exercícios miofuncionais reduzem AHI ~50% em SAOS ligeira-moderada.",
            "Higiene do sono potencia qualquer tratamento.",
        ],
    },
    {
        "id": "m08_pos_op",
        "label": "8. Pós-operatório",
        "titulo": "Pós-operatório e seguimento",
        "icone": "🩹",
        "tempo_min": 10,
        "descricao": "Os 90 dias pós-cirurgia e seguimento de longo prazo.",
        "prerequisitos": ["m06_plano"],
        "objetivos": [
            "Saber o que esperar nos primeiros 7-90 dias",
            "Reconhecer sinais de alerta (SU vs telefonema)",
            "Compreender quando fazer polissonografia de controlo",
            "Antecipar cenários (responder, non-responder)",
        ],
        "takeaways": [
            "Pico de dor entre dias 5-7 (quando crostas se soltam).",
            "Sinais SU: hemorragia, febre alta, falta de ar.",
            "PSG de controlo: 3-6 meses pós-cirurgia.",
            "Non-responders: CPAP de resgate frequentemente bem tolerado.",
        ],
    },
]


def metadata(modulo_id: str) -> dict | None:
    """Devolve a metadata de um módulo pelo id."""
    return next((m for m in ORDEM_MODULOS if m["id"] == modulo_id), None)


def breadcrumb(modulo_id: str, titulo: str) -> None:
    """Header fixo no topo: breadcrumb + módulo atual + progresso visível."""
    concluidos = st.session_state.get("modulos_concluidos", set())
    n_concluidos = len(concluidos)
    total = len(ORDEM_MODULOS)
    pct = int(n_concluidos / total * 100) if total else 0

    # Encontrar índice do módulo atual
    idx = next(
        (i for i, m in enumerate(ORDEM_MODULOS) if m["id"] == modulo_id),
        None,
    )
    posicao = f"{idx} de {total - 1}" if idx is not None else ""

    st.markdown(
        f"""
<div style="background:white;border:1px solid #E2E4E6;border-radius:12px;
            padding:0.75rem 1.25rem;margin-bottom:1.5rem;
            font-family:'IBM Plex Sans',sans-serif;
            display:flex;justify-content:space-between;align-items:center;
            flex-wrap:wrap;gap:0.75rem;">
  <div>
    <div style="font-size:11px;font-weight:500;color:#73787A;
                text-transform:uppercase;letter-spacing:0.18em;">
      🌙 Apneia do Sono — Tutorial
    </div>
    <div style="font-family:'Outfit',sans-serif;font-size:1rem;
                font-weight:600;color:#252728;margin-top:0.15rem;">
      {titulo} {f"· {posicao}" if posicao else ""}
    </div>
  </div>
  <div style="text-align:right;min-width:160px;">
    <div style="font-size:11px;color:#73787A;margin-bottom:0.25rem;">
      Progresso · {n_concluidos}/{total} ({pct}%)
    </div>
    <div style="background:#E2E4E6;border-radius:999px;height:6px;
                width:160px;overflow:hidden;">
      <div style="background:linear-gradient(90deg,#2CF4E5,#00D3C8,#0EAA9F);
                  height:100%;border-radius:999px;width:{pct}%;
                  transition:width 0.4s ease;"></div>
    </div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def navegacao_botoes(modulo_id_atual: str) -> None:
    """Botões 'Anterior' e 'Próximo' no fim de cada módulo."""
    idx = next(
        (i for i, m in enumerate(ORDEM_MODULOS) if m["id"] == modulo_id_atual),
        None,
    )
    if idx is None:
        return

    anterior = ORDEM_MODULOS[idx - 1] if idx > 0 else None
    proximo = ORDEM_MODULOS[idx + 1] if idx < len(ORDEM_MODULOS) - 1 else None

    col_a, col_b = st.columns(2)

    with col_a:
        if anterior:
            if st.button(
                f"← {anterior['icone']} {anterior['titulo']}",
                use_container_width=True,
                key=f"nav_prev_{modulo_id_atual}",
                help=f"Ir para o módulo anterior",
            ):
                _navegar_para(anterior["label"])
        else:
            st.markdown('<div style="height:54px;"></div>', unsafe_allow_html=True)

    with col_b:
        if proximo:
            if st.button(
                f"{proximo['icone']} {proximo['titulo']} →",
                type="primary",
                use_container_width=True,
                key=f"nav_next_{modulo_id_atual}",
                help=f"Ir para o próximo módulo",
            ):
                _navegar_para(proximo["label"])
        else:
            st.markdown(
                '<div style="padding:1rem;background:#E6FAF8;border-radius:12px;'
                'text-align:center;color:#0EAA9F;font-weight:500;'
                'font-family:\'IBM Plex Sans\',sans-serif;">'
                "🎉 Concluiu o último módulo do tutorial."
                "</div>",
                unsafe_allow_html=True,
            )


def _navegar_para(label: str) -> None:
    st.session_state["nav_target"] = label
    st.rerun()


# ─── Componentes e-learning ────────────────────────────────────────


def objetivos_aprendizagem(modulo_id: str) -> None:
    """Box visível no topo de cada módulo: objetivos + tempo + pré-req."""
    m = metadata(modulo_id)
    if not m:
        return

    # Pré-requisitos legíveis
    prereq_html = ""
    if m["prerequisitos"]:
        nomes = []
        for prereq_id in m["prerequisitos"]:
            prereq_meta = metadata(prereq_id)
            if prereq_meta:
                nomes.append(f"{prereq_meta['icone']} {prereq_meta['titulo']}")
        prereq_html = (
            '<div style="margin-top:0.5rem;font-size:0.85rem;color:#73787A;">'
            f"<strong>Pré-requisitos recomendados:</strong> {' · '.join(nomes)}"
            "</div>"
        )

    objetivos_li = "".join(
        f'<li style="margin-bottom:0.35rem;">{o}</li>' for o in m["objetivos"]
    )

    st.markdown(
        f"""
<div style="background:#E6FAF8;border-left:3px solid #0EAA9F;
            border-radius:12px;padding:1.25rem 1.5rem;margin:1.5rem 0;
            font-family:'IBM Plex Sans',sans-serif;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;
              margin-bottom:0.75rem;">
    <div style="font-size:11px;font-weight:500;color:#0EAA9F;
                text-transform:uppercase;letter-spacing:0.18em;">
      🎯 Objetivos de aprendizagem
    </div>
    <div style="background:white;padding:0.25rem 0.7rem;border-radius:999px;
                font-size:0.75rem;color:#252728;font-weight:500;
                border:1px solid #E2E4E6;">
      ⏱️ {m['tempo_min']} min
    </div>
  </div>
  <div style="color:#252728;font-size:0.95rem;">
    No fim deste módulo vai conseguir:
    <ul style="margin:0.5rem 0 0 1.25rem;padding:0;color:#3E4244;">
      {objetivos_li}
    </ul>
  </div>
  {prereq_html}
</div>
        """,
        unsafe_allow_html=True,
    )


def resumo_takeaways(modulo_id: str) -> None:
    """Box de resumo / key takeaways antes do quiz."""
    m = metadata(modulo_id)
    if not m:
        return

    items_html = "".join(
        f'<li style="margin-bottom:0.5rem;padding-left:0.5rem;">{t}</li>'
        for t in m["takeaways"]
    )

    st.markdown(
        f"""
<div style="background:white;border:2px solid #00D3C8;border-radius:16px;
            padding:1.5rem 1.75rem;margin:2rem 0 1.5rem 0;
            font-family:'IBM Plex Sans',sans-serif;">
  <div style="font-size:11px;font-weight:500;color:#0EAA9F;
              text-transform:uppercase;letter-spacing:0.18em;
              margin-bottom:0.5rem;">
    📝 O essencial deste módulo
  </div>
  <h3 style="font-family:'Outfit',sans-serif;font-weight:600;
             color:#252728;margin:0 0 0.75rem 0;font-size:1.25rem;">
    Para levar consigo
  </h3>
  <ul style="margin:0;padding-left:1.25rem;color:#3E4244;font-size:0.95rem;
             line-height:1.55;">
    {items_html}
  </ul>
</div>
        """,
        unsafe_allow_html=True,
    )
