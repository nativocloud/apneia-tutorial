"""Gráficos Plotly com dados reais do paper Antunes 2023."""

import pandas as pd
import plotly.graph_objects as go
from dados.antunes_2023 import (
    GRAVIDADE_PRE_OP,
    NORMALIZACAO_POS_CIRURGIA,
    PREVALENCIA_DISTURBIOS_PRE,
    PSG_PRE_POS,
    RESPONDERS_VS_NON,
)


def gravidade_pre_op_pizza() -> go.Figure:
    fig = go.Figure(
        go.Pie(
            labels=list(GRAVIDADE_PRE_OP.keys()),
            values=list(GRAVIDADE_PRE_OP.values()),
            hole=0.45,
            marker=dict(colors=["#7fc97f", "#fdc086", "#e76f51"]),
            textinfo="label+percent",
            textposition="outside",
        )
    )
    fig.update_layout(
        title="Gravidade da SAOS — coorte Antunes 2023 (n=76)",
        showlegend=False,
        height=400,
    )
    return fig


def fases_sono_barras_pre_pos() -> go.Figure:
    df = pd.DataFrame(PSG_PRE_POS)
    fases = df[df["Variável"].isin(["N1 (%)", "N2 (%)", "N3 (%)", "REM (%)"])]

    fig = go.Figure()
    fig.add_bar(
        x=fases["Variável"],
        y=fases["Pré-operatório"],
        name="Pré-operatório",
        marker_color="#cc4444",
        text=[f"{v:.1f}%" for v in fases["Pré-operatório"]],
        textposition="outside",
    )
    fig.add_bar(
        x=fases["Variável"],
        y=fases["Pós-operatório"],
        name="Pós-operatório",
        marker_color="#449944",
        text=[f"{v:.1f}%" for v in fases["Pós-operatório"]],
        textposition="outside",
    )
    fig.update_layout(
        title="Distribuição das fases do sono (mediana, % do TST)",
        yaxis_title="% do tempo total de sono",
        barmode="group",
        height=420,
        annotations=[
            dict(
                x="N3 (%)",
                y=22,
                text="p = 0.003 ★",
                showarrow=False,
                font=dict(color="#449944", size=13, family="monospace"),
            )
        ],
    )
    return fig


def ahi_antes_depois() -> go.Figure:
    fig = go.Figure(
        go.Bar(
            x=["Pré-operatório", "Pós-operatório"],
            y=[17.4, 13.0],
            marker_color=["#cc4444", "#449944"],
            text=["AHI 17.4", "AHI 13.0"],
            textposition="outside",
        )
    )
    fig.update_layout(
        title="AHI mediano antes vs depois da cirurgia",
        yaxis_title="Eventos por hora",
        yaxis_range=[0, 22],
        height=380,
        shapes=[
            dict(
                type="line", x0=-0.5, x1=1.5, y0=5, y1=5,
                line=dict(color="green", dash="dot"),
            ),
            dict(
                type="line", x0=-0.5, x1=1.5, y0=15, y1=15,
                line=dict(color="orange", dash="dot"),
            ),
            dict(
                type="line", x0=-0.5, x1=1.5, y0=30, y1=30,
                line=dict(color="red", dash="dot"),
            ),
        ],
        annotations=[
            dict(x=1.5, y=5, text="normal", showarrow=False, font=dict(size=10, color="green")),
            dict(x=1.5, y=15, text="moderada", showarrow=False, font=dict(size=10, color="orange")),
        ],
    )
    return fig


def normalizacao_fases_pos() -> go.Figure:
    fig = go.Figure(
        go.Bar(
            x=list(NORMALIZACAO_POS_CIRURGIA.keys()),
            y=list(NORMALIZACAO_POS_CIRURGIA.values()),
            marker_color="#5b8def",
            text=[f"{v}%" for v in NORMALIZACAO_POS_CIRURGIA.values()],
            textposition="outside",
        )
    )
    fig.update_layout(
        title="% de pacientes com normalização da fase de sono após cirurgia",
        yaxis_title="% pacientes",
        yaxis_range=[0, 75],
        height=380,
    )
    return fig


def disturbios_pre_op() -> go.Figure:
    fig = go.Figure(
        go.Bar(
            x=list(PREVALENCIA_DISTURBIOS_PRE.values()),
            y=list(PREVALENCIA_DISTURBIOS_PRE.keys()),
            orientation="h",
            marker_color="#cc4444",
            text=[f"{v}%" for v in PREVALENCIA_DISTURBIOS_PRE.values()],
            textposition="outside",
        )
    )
    fig.update_layout(
        title="Prevalência de perturbações do sono pré-cirurgia (n=76)",
        xaxis_title="% pacientes",
        xaxis_range=[0, 105],
        height=350,
    )
    return fig


def responders_vs_non_radar() -> go.Figure:
    df = pd.DataFrame(RESPONDERS_VS_NON)
    fases_pct = df[df["Variável"].isin(["N1 (%)", "N2 (%)", "N3 (%)", "REM (%)"])].copy()

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=fases_pct["Responders"].tolist() + [fases_pct["Responders"].iloc[0]],
            theta=fases_pct["Variável"].tolist() + [fases_pct["Variável"].iloc[0]],
            fill="toself",
            name="Responders (75% pacientes)",
            line_color="#449944",
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=fases_pct["Non-responders"].tolist() + [fases_pct["Non-responders"].iloc[0]],
            theta=fases_pct["Variável"].tolist() + [fases_pct["Variável"].iloc[0]],
            fill="toself",
            name="Non-responders (25%)",
            line_color="#cc4444",
        )
    )
    fig.update_layout(
        title="Responders vs Non-responders — perfil de fases do sono (%)",
        polar=dict(radialaxis=dict(visible=True, range=[0, 55])),
        height=460,
    )
    return fig
