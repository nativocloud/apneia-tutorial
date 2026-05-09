# Apneia do Sono — Tutorial educativo

Tutorial interativo sobre **Síndrome de Apneia Obstrutiva do Sono (SAOS)**
e o **tratamento cirúrgico multinível**, em 9 módulos com cerca de 75
minutos de duração total.

Construído em Streamlit, fundamentado em literatura científica recente
(Antunes et al. 2023, Kim 2026, Krüger 2026, Hartenbaum 2026).

## Conteúdo

| Módulo | Tópico | Duração |
|---|---|---|
| 0 | Comece aqui — visão geral | 5 min |
| 1 | Anatomia das vias aéreas | 8 min |
| 2 | Como dormimos (fases do sono) | 6 min |
| 3 | O que é a SAOS (fisiopatologia) | 10 min |
| 4 | Diagnóstico (PSG, AHI, DISE) | 8 min |
| 5 | Tratamentos disponíveis | 10 min |
| 6 | Plano cirúrgico multinível | 12 min |
| 7 | Prevenção e estilo de vida | 8 min |
| 8 | Pós-operatório e seguimento | 10 min |

## Recursos

- 🖼️ Imagens **OpenStax 2022** (CC BY 4.0) — anatomia moderna em cores
- 📷 Fotografias clínicas reais (Wikimedia, licenças abertas)
- 🎬 Animações SVG do colapso da via aérea e ronco
- 📊 Gráficos Plotly interativos com dados reais (Antunes 2023)
- 📺 Vídeo NHLBI/NIH embebido
- 🌐 Visualizador 3D BodyParts3D (iframe)
- 📖 Glossário com 22 termos clínicos
- 🧠 Quizzes em cada módulo com pontuação

## Correr localmente

```bash
# Com uv (recomendado)
uv run streamlit run app.py

# Com pip
pip install -r requirements.txt
streamlit run app.py
```

A app abre em `http://localhost:8501`.

## Deploy

Compatível com **Streamlit Community Cloud** (gratuito):
1. Push do código para um repositório GitHub
2. Em [share.streamlit.io](https://share.streamlit.io), conectar GitHub e
   selecionar o repo + branch + `app.py`
3. Deploy em ~3 minutos

## Estrutura

```
apneia/
├── app.py                    # entry point Streamlit
├── components/               # UI, navegação, quiz, glossário
├── modulos/                  # 9 módulos do tutorial
├── dados/                    # dados estruturados (Antunes 2023)
├── assets/
│   ├── imagens/              # OpenStax + fotos clínicas
│   └── brand/                # logos
├── papers/                   # PDFs científicos de referência
├── .streamlit/config.toml    # tema Native Stride
├── requirements.txt          # deps para Streamlit Cloud
└── pyproject.toml            # deps para uv
```

## Fontes científicas

- **Antunes J, Órfão J, Rito J, Adónis C, Freire F.** (2023).
  *Surgical treatment for obstructive sleep apnea: effect on sleep architecture.*
  Eur Arch Otorhinolaryngol 280:5059-5065.
  [DOI](https://doi.org/10.1007/s00405-023-08093-8)
- **Kim SW.** (2026). *REM-OSA: Clinical Characteristics and Cardiovascular,
  Cognitive, Neurobehavioral, and Metabolic Implications.* Curr Sleep Med Rep 12:8.
- **Krüger M et al.** (2026). *Breathing bad: increased risk for OSA in current
  and former smokers.* Sci Rep 16:13382.
- **Hartenbaum NP.** (2026). *Obstructive Sleep Apnea in Commercial Trucking.*
  Curr Sleep Med Rep 12:19.

Guidelines: AASM 2023, ICSD-3-TR 2023, FIPAT *Terminologia Anatomica* 2.ª ed. (2019).

## Licença e aviso

Tutorial **educativo**. Não substitui consulta médica. As decisões clínicas
devem ser tomadas com a equipa cirúrgica de otorrinolaringologia, com base no
caso individual de cada paciente.
