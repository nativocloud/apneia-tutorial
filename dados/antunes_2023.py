"""Dados estruturados extraídos do paper Antunes et al. 2023.

Antunes J, Órfão J, Rito J, Adónis C, Freire F. (2023).
Surgical treatment for obstructive sleep apnea: effect on sleep architecture.
European Archives of Oto-Rhino-Laryngology, 280:5059-5065.
DOI: 10.1007/s00405-023-08093-8
"""

POPULACAO = {
    "n_total": 76,
    "homens": 55,
    "mulheres": 21,
    "idade_mediana": 49.0,
    "idade_iqr": (41.0, 62.0),
    "imc_mediana": 27.3,
    "imc_iqr": (25.3, 29.3),
    "perimetro_pescoco_cm": 40.0,
    "ess_mediana": 7.0,
    "ahi_pre_op_mediana": 17.4,
    "ahi_pre_op_iqr": (11.3, 22.9),
}

GRAVIDADE_PRE_OP = {
    "Ligeira (5≤AHI<15)": 31,
    "Moderada (15≤AHI<30)": 37,
    "Grave (AHI≥30)": 8,
}

CIRURGIAS_REALIZADAS = {
    "Palatoplastia de suspensão": 76,
    "Cirurgia base da língua (coblation)": 10,
    "Cirurgia base da língua (radiofrequência)": 11,
    "Epiglotectomia parcial": 7,
}

# Tabela 2 — pré vs pós cirurgia (medianas)
PSG_PRE_POS = {
    "Variável": [
        "TST (min)",
        "Eficiência (%)",
        "N1 (min)",
        "N2 (min)",
        "N3 (min)",
        "REM (min)",
        "N1 (%)",
        "N2 (%)",
        "N3 (%)",
        "REM (%)",
        "Latência sono (min)",
        "Latência REM (min)",
        "Índice de despertares (n/h)",
        "AHI (n/h)",
    ],
    "Pré-operatório": [456.8, 91.3, 47.3, 233.7, 70.2, 84.6, 11.3, 50.8, 16.9, 18.7, 7.5, 93.0, 41.3, 17.4],
    "Pós-operatório": [423.8, 90.9, 47.5, 198.5, 83.9, 75.6, 11.2, 49.1, 18.9, 18.1, 7.0, 87.8, 37.4, 13.0],
    "p-value": [0.158, 0.353, 0.895, 0.421, 0.026, 0.350, 0.987, 0.171, 0.003, 0.968, 0.672, 0.588, 0.132, None],
    "Significativo": [False, False, False, False, True, False, False, False, True, False, False, False, False, False],
}

# Tabela 3 — responders vs non-responders
RESPONDERS_VS_NON = {
    "Variável": [
        "AHI (n/h)",
        "TST (min)",
        "Eficiência (%)",
        "N1 (min)",
        "N2 (min)",
        "N3 (min)",
        "REM (min)",
        "N1 (%)",
        "N2 (%)",
        "N3 (%)",
        "REM (%)",
    ],
    "Responders": [10.0, 423.8, 90.9, 46.0, 175.7, 87.2, 78.1, 10.4, 48.1, 21.2, 18.5],
    "Non-responders": [24.5, 423.0, 91.1, 53.7, 257.3, 65.6, 63.2, 13.8, 50.7, 15.9, 17.1],
    "p-value": [0.001, 0.504, 0.736, 0.026, 0.052, 0.029, 0.277, 0.026, 0.338, 0.019, 0.439],
    "Significativo": [True, False, False, True, False, True, False, True, False, True, False],
}

# Prevalência de perturbações da arquitetura do sono pré-op
PREVALENCIA_DISTURBIOS_PRE = {
    "≥1 fase anormal": 93.4,
    "N1 aumentado": 77.6,
    "N2 aumentado": 32.9,
    "N3 diminuído": 39.5,
    "REM diminuído": 28.9,
}

# Normalização das fases após cirurgia (% de pacientes)
NORMALIZACAO_POS_CIRURGIA = {
    "N1": 18.6,
    "N2": 44.0,
    "N3": 23.3,
    "REM": 63.6,
}

CITACAO_COMPLETA = (
    "Antunes J, Órfão J, Rito J, Adónis C, Freire F. "
    "Surgical treatment for obstructive sleep apnea: effect on sleep architecture. "
    "Eur Arch Otorhinolaryngol. 2023;280:5059–5065. "
    "doi: 10.1007/s00405-023-08093-8"
)
