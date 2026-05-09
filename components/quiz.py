"""Componente de quiz reutilizável para aferir compreensão de cada módulo.

Uso típico num módulo:

    from components.quiz import Pergunta, render_quiz

    perguntas = [
        Pergunta(
            id="m1_q1",
            enunciado="Onde estão localizados os cornetos nasais?",
            opcoes=["Na garganta", "Dentro das fossas nasais", "No palato"],
            correta=1,
            explicacao="Os cornetos são saliências dentro das fossas nasais...",
        ),
    ]

    render_quiz(modulo_id="modulo_1", titulo="Anatomia básica", perguntas=perguntas)
"""

from dataclasses import dataclass
from typing import Literal

import streamlit as st


@dataclass
class Pergunta:
    id: str
    enunciado: str
    opcoes: list[str]
    correta: int  # índice da opção correta (0-based)
    explicacao: str
    tipo: Literal["mc", "vf"] = "mc"  # multiple choice ou verdadeiro/falso


def _state_key(modulo_id: str, sufixo: str) -> str:
    return f"quiz__{modulo_id}__{sufixo}"


def render_quiz(modulo_id: str, titulo: str, perguntas: list[Pergunta]) -> None:
    """Renderiza um quiz interativo com feedback imediato e pontuação final."""
    st.divider()
    st.subheader(f"🧠 Quiz — {titulo}")
    st.caption(
        f"{len(perguntas)} perguntas. Responda à sua frente — verá explicações depois de submeter."
    )

    submetido_key = _state_key(modulo_id, "submetido")
    respostas_key = _state_key(modulo_id, "respostas")

    if submetido_key not in st.session_state:
        st.session_state[submetido_key] = False
    if respostas_key not in st.session_state:
        st.session_state[respostas_key] = {}

    submetido = st.session_state[submetido_key]

    with st.form(key=f"form_{modulo_id}"):
        respostas_atuais: dict[str, int | None] = {}
        for i, p in enumerate(perguntas, start=1):
            st.markdown(f"**{i}. {p.enunciado}**")
            escolha = st.radio(
                label=f"Pergunta {i}",
                options=list(range(len(p.opcoes))),
                format_func=lambda idx, opcoes=p.opcoes: opcoes[idx],
                key=f"radio_{modulo_id}_{p.id}",
                index=None,
                label_visibility="collapsed",
            )
            respostas_atuais[p.id] = escolha
            st.write("")

        submit = st.form_submit_button(
            "Submeter respostas" if not submetido else "Re-submeter",
            type="primary",
        )
        if submit:
            st.session_state[respostas_key] = respostas_atuais
            st.session_state[submetido_key] = True
            if "modulos_concluidos" not in st.session_state:
                st.session_state["modulos_concluidos"] = set()
            st.session_state["modulos_concluidos"].add(modulo_id)
            st.rerun()

    if submetido:
        respostas = st.session_state[respostas_key]
        certas = 0
        total = len(perguntas)

        for i, p in enumerate(perguntas, start=1):
            resposta_dada = respostas.get(p.id)
            with st.container(border=True):
                if resposta_dada is None:
                    st.warning(f"**{i}.** Não respondida.")
                    st.caption(f"Resposta correta: **{p.opcoes[p.correta]}**")
                    st.info(p.explicacao)
                elif resposta_dada == p.correta:
                    certas += 1
                    st.success(f"**{i}. ✔ Correto** — {p.opcoes[p.correta]}")
                    st.caption(p.explicacao)
                else:
                    st.error(
                        f"**{i}. ✗ Incorreto** — escolheu *{p.opcoes[resposta_dada]}*. "
                        f"A resposta correta é **{p.opcoes[p.correta]}**."
                    )
                    st.info(p.explicacao)

        pct = certas / total * 100
        if pct >= 80:
            cor, msg = "🟢", "Excelente compreensão. Pode avançar para o próximo módulo."
        elif pct >= 60:
            cor, msg = "🟡", "Boa base. Vale a pena reler os pontos errados antes de avançar."
        else:
            cor, msg = "🔴", "Sugiro reler o módulo. Os conceitos vão ser usados nos seguintes."

        st.divider()
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Pontuação", f"{certas}/{total}", f"{pct:.0f}%")
        with col2:
            st.markdown(f"### {cor} {msg}")

        if st.button("Recomeçar quiz", key=f"reset_{modulo_id}"):
            st.session_state[submetido_key] = False
            st.session_state[respostas_key] = {}
            st.rerun()
