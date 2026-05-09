"""Renderização de imagens anatómicas (modernas) + animações SVG.

Imagens: OpenStax Anatomy & Physiology (2013, revisão 2022, CC BY 4.0) e
NIH/Wikimedia (domínio público). Todas baixadas para assets/imagens/ para
funcionar offline.

OpenStax é a fonte de referência usada em ensino universitário moderno.
A nomenclatura segue a Terminologia Anatómica Internacional (FIPAT 2019).

SVG inline (animações, hipnogramas) usa st.components.v1.html para renderização
robusta (st.markdown sanitiza demasiado).
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "imagens"


def via_aerea_simplificada() -> None:
    """Vista simplificada para iniciantes — boa imagem moderna do NIH."""
    st.image(
        str(ASSETS / "illu_head_neck.jpg"),
        caption=(
            "Vista lateral simplificada da via aérea superior. "
            "Fonte: NIH SeniorHealth (Wikimedia Commons, domínio público)."
        ),
        width=620,
    )

    with st.expander("📖 Tradução dos termos"):
        st.markdown(
            """
| Termo | Em português |
|---|---|
| *Nasal Cavity* | Cavidade nasal (onde estão os cornetos) |
| *Palate* | Palato (duro à frente, mole atrás) |
| *Oral Cavity* | Cavidade oral (boca) |
| *Tongue* | Língua |
| *Pharynx* | Faringe (a "garganta") |
| *Epiglottis* | Epiglote |
| *Larynx* | Laringe (cordas vocais) |
| *Esophagus* | Esófago |
            """
        )


def via_aerea_sagital_completa() -> None:
    """Vista anatómica completa moderna em cor (OpenStax 2303, CC BY 4.0)."""
    st.image(
        str(ASSETS / "openstax_2303_via_aerea.jpg"),
        caption=(
            "Anatomia detalhada em corte sagital: nariz, faringe, boca e laringe. "
            "Fonte: OpenStax Anatomy & Physiology (2022), CC BY 4.0. "
            "Nomenclatura segundo Terminologia Anatómica Internacional (FIPAT 2019)."
        ),
        width=620,
    )

    with st.expander("📖 Tradução completa dos termos da imagem"):
        st.markdown(
            """
| Termo (inglês) | Em português | O que é |
|---|---|---|
| *Frontal sinus* | Seio frontal | Cavidade de ar no osso frontal |
| *Sphenoidal sinus* | Seio esfenoidal | Cavidade de ar no osso esfenoide |
| *Ethmoid bone* | Osso etmoide | Onde se inserem os cornetos sup./médio |
| *Olfactory epithelium* | Epitélio olfativo | O que dá o sentido do cheiro |
| *Nasal conchae* | Cornetos / Conchas nasais | As 3 "prateleiras" no nariz |
| *Nasal meatuses* | Meatos nasais | Espaços de ar **entre** os cornetos |
| *Nasal vestibule* | Vestíbulo nasal | Logo à entrada da narina |
| *Nostril* | Narina | A entrada visível |
| *Hard palate* | Palato duro | Parte óssea do céu da boca |
| *Soft palate* | Palato mole | Parte mole — vibra no ronco |
| *Uvula* | Úvula | A "campainha" ao fundo |
| *Pharyngeal tonsil* | Tonsila faríngea / Adenoides | Linfoide na nasofaringe |
| *Palatine tonsil* | Amígdala palatina | **As que serão removidas** |
| *Lingual tonsil* | Amígdala lingual | Na base da língua |
| *Tongue* | Língua | (a base, atrás, pode obstruir) |
| *Opening of auditory tube* | Abertura da trompa de Eustáquio | Liga ao ouvido médio |
| *Nasopharynx* | Nasofaringe | Atrás do nariz |
| *Oropharynx* | **Orofaringe** | **Atrás da boca — alvo da palatoplastia** |
| *Laryngopharynx* | Laringofaringe | Atrás da laringe |
| *Epiglottis* | Epiglote | Tampa da laringe |
| *Hyoid bone* | Osso hioide | Suporta a língua e laringe |
| *Vestibular fold* / *Vocal fold* | Pregas vestibulares / vocais | Cordas vocais |
| *Thyroid cartilage* | Cartilagem tiroide | "Pomo de Adão" |
| *Cricoid cartilage* | Cartilagem cricoide | Anel logo abaixo |
| *Trachea* | Traqueia | Tubo até aos pulmões |
| *Esophagus* | Esófago | Tubo digestivo |
            """
        )


def cornetos_detalhe() -> None:
    """Detalhe dos 3 cornetos nasais (OpenStax 731, CC BY 4.0)."""
    st.image(
        str(ASSETS / "openstax_731_cavidade_nasal.jpg"),
        caption=(
            "Os 3 cornetos nasais (conchas nasais superior, média e inferior) "
            "vistos de dentro. Fonte: OpenStax (2022), CC BY 4.0."
        ),
        width=620,
    )

    with st.expander("📖 O que está na imagem"):
        st.markdown(
            """
A imagem mostra um corte do crânio com a parede lateral da cavidade nasal direita.
Os 3 cornetos formam uma "estante" horizontal:

| Termo (inglês) | Em português | Notas |
|---|---|---|
| *Superior nasal concha* | Corneto superior | O mais pequeno, no topo |
| *Middle nasal concha* | Corneto médio | No meio |
| *Inferior nasal concha* | Corneto inferior | **O maior — o que mais frequentemente bloqueia** |
| *Ethmoid bone* | Osso etmoide | De onde nascem o sup. e o médio |
| *Sphenoidal sinus* | Seio esfenoidal | Cavidade óssea atrás do nariz |

⚡ **Os meatos** (espaços de ar entre os cornetos) são onde o ar passa.
Quando os cornetos incham, os meatos fecham — daí a sensação de "nariz tapado".
A **turbinoplastia** reduz o corneto inferior preservando a função.
            """
        )


def divisoes_faringe() -> None:
    """As 3 divisões da faringe (OpenStax 2305, CC BY 4.0) — moderna em cor."""
    st.image(
        str(ASSETS / "openstax_2305_faringe_divisoes.jpg"),
        caption=(
            "As 3 divisões da faringe: nasofaringe (verde), orofaringe (ciano), "
            "laringofaringe (magenta). Fonte: OpenStax (2022), CC BY 4.0."
        ),
        width=620,
    )

    st.markdown(
        """
A **faringe** ('garganta') é o tubo muscular do fundo do nariz à entrada do
esófago. Divide-se em 3 zonas:

- 🟢 **Nasofaringe** — atrás do nariz. Aqui ficam as **adenoides** e a entrada
  das trompas de Eustáquio.
- 🟦 **Orofaringe** — atrás da boca. Aqui ficam as **amígdalas palatinas**, o
  **palato mole** e a **úvula**. **É o nível onde a sua palatoplastia atua.**
- 🟪 **Laringofaringe** — atrás e abaixo da laringe. Conecta-se ao esófago.
        """
    )


def hipnograma_real() -> None:
    """Hipnograma genérico ilustrando ciclos do sono."""
    st.image(
        str(ASSETS / "hypnogram.svg"),
        caption=(
            "Hipnograma típico de uma noite. Cada subida é um período REM "
            "(~90 min), as descidas mais profundas são N3 (sono restaurador). "
            "Wikimedia Commons."
        ),
        width=620,
    )


def mallampati_imagem() -> None:
    """Classificação de Mallampati."""
    st.image(
        str(ASSETS / "mallampati.svg"),
        caption=(
            "Classificação de Mallampati — graus I a IV. Graus III/IV "
            "associam-se a maior risco de SAOS e via aérea difícil. "
            "Wikimedia Commons."
        ),
        width=620,
    )


# ─── ANIMAÇÕES SVG ─────────────────────────────────────────────────────────


def _painel_via_aerea(estado: str) -> str:
    """Devolve um <svg> com a via aérea numa de 4 fases. Não é animado."""
    if estado == "aberta":
        cor_fundo = "#e8f5e8"
        titulo = "1. AR PASSA"
        cor_titulo = "#2d8a2d"
        spo2 = "98%"
        spo2_cor = "#2d8a2d"
        descr = "Via aérea aberta. Respiração normal."
        # palato e língua em posição relaxada
        palato_y = 145
        lingua_y = 215
        seta = True
        seta_opacidade = "1"
    elif estado == "estreitando":
        cor_fundo = "#fff8e0"
        titulo = "2. ESTREITA"
        cor_titulo = "#cc8800"
        spo2 = "94%"
        spo2_cor = "#cc8800"
        descr = "Músculos relaxam. Palato e língua avançam."
        palato_y = 170
        lingua_y = 195
        seta = True
        seta_opacidade = "0.5"
    elif estado == "colapso":
        cor_fundo = "#fde0e0"
        titulo = "3. COLAPSO — APNEIA"
        cor_titulo = "#cc0000"
        spo2 = "85%"
        spo2_cor = "#cc0000"
        descr = "Via aérea fecha. NÃO PASSA AR. SpO₂ desce."
        palato_y = 200
        lingua_y = 200
        seta = False
        seta_opacidade = "0"
    else:  # despertar
        cor_fundo = "#fff0e0"
        titulo = "4. MICRO-DESPERTAR"
        cor_titulo = "#dd6622"
        spo2 = "90%↑"
        spo2_cor = "#dd6622"
        descr = "Cérebro acorda 1-3s, reabre via aérea, volta a dormir."
        palato_y = 150
        lingua_y = 220
        seta = True
        seta_opacidade = "1"

    seta_svg = ""
    if seta:
        seta_svg = (
            f'<line x1="120" y1="180" x2="195" y2="180" stroke="#3399ff" '
            f'stroke-width="5" opacity="{seta_opacidade}" marker-end="url(#ar_arrow)"/>'
        )

    return f"""
<svg viewBox="0 0 280 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;">
  <defs>
    <marker id="ar_arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="#3399ff"/>
    </marker>
  </defs>

  <!-- Fundo colorido -->
  <rect width="280" height="320" fill="{cor_fundo}"/>

  <!-- Título do estado -->
  <rect x="0" y="0" width="280" height="32" fill="{cor_titulo}"/>
  <text x="140" y="22" font-size="14" font-weight="bold" fill="white" text-anchor="middle"
        font-family="sans-serif">
    {titulo}
  </text>

  <!-- Contorno facial (vista lateral) -->
  <path d="M 60,55 Q 60,45 75,45 L 240,45 Q 260,45 260,65 L 260,290 L 60,290 Z"
        fill="white" stroke="#666" stroke-width="1.5"/>

  <!-- Palato duro (osso) -->
  <rect x="85" y="100" width="115" height="10" fill="#d4b890" stroke="#8b6f47"/>
  <text x="142" y="95" font-size="9" fill="#666" text-anchor="middle" font-family="sans-serif">
    palato duro
  </text>

  <!-- Palato mole + úvula (posição depende do estado) -->
  <path d="M 200,110 Q 215,{palato_y - 25} 210,{palato_y - 5} L 205,{palato_y + 5} L 200,{palato_y - 5} Q 195,{palato_y - 25} 195,110 Z"
        fill="#ffaaaa" stroke="#992222" stroke-width="1.2"/>
  <text x="220" y="135" font-size="9" fill="#666" font-family="sans-serif">palato mole</text>

  <!-- Língua -->
  <path d="M 60,290 Q 130,{lingua_y - 30} 200,{lingua_y - 20} Q 230,{lingua_y - 15} 260,290 Z"
        fill="#e08080" stroke="#aa3333" stroke-width="1.2"/>
  <text x="120" y="270" font-size="10" fill="white" font-family="sans-serif" font-weight="bold">
    língua
  </text>

  <!-- Indicador de fluxo de ar -->
  <text x="60" y="170" font-size="11" font-weight="bold" fill="#3399ff" font-family="sans-serif">
    AR:
  </text>
  {seta_svg}

  <!-- SpO2 -->
  <rect x="200" y="50" width="55" height="32" rx="4" fill="white" stroke="{spo2_cor}" stroke-width="2"/>
  <text x="227" y="65" font-size="9" fill="#666" text-anchor="middle" font-family="sans-serif">SpO₂</text>
  <text x="227" y="78" font-size="14" font-weight="bold" fill="{spo2_cor}" text-anchor="middle"
        font-family="monospace">
    {spo2}
  </text>

  <!-- Descrição -->
  <foreignObject x="10" y="295" width="260" height="20">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:10px;color:#222;text-align:center;font-family:sans-serif;">
      {descr}
    </div>
  </foreignObject>
</svg>
"""


def animacao_colapso_via_aerea() -> None:
    """4 painéis comparativos lado a lado — fases do ciclo de apneia."""
    p1 = _painel_via_aerea("aberta")
    p2 = _painel_via_aerea("estreitando")
    p3 = _painel_via_aerea("colapso")
    p4 = _painel_via_aerea("despertar")

    html = f"""
<div style="font-family:sans-serif;">
  <div style="text-align:center;font-weight:bold;font-size:15px;margin-bottom:8px;color:#222;">
    Ciclo de uma apneia obstrutiva (≈ 30 segundos no total)
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;">
    <div>{p1}</div>
    <div>{p2}</div>
    <div>{p3}</div>
    <div>{p4}</div>
  </div>
  <div style="margin-top:10px;padding:10px;background:#f5f5f5;border-left:4px solid #5b8def;font-size:13px;color:#222;">
    🔁 <strong>Em SAOS grave este ciclo repete-se 30+ vezes por hora</strong>,
    toda a noite. Cada micro-despertar é tão breve que o paciente <em>não se
    lembra de acordar</em> — mas o sono nunca chega à fase profunda (N3).
  </div>
</div>
"""
    components.html(html, height=440)


def animacao_colapso_sequencial() -> None:
    """Animação sequencial lenta: 4 fases mostradas uma de cada vez (4s cada)."""
    fase1 = _painel_via_aerea("aberta")
    fase2 = _painel_via_aerea("estreitando")
    fase3 = _painel_via_aerea("colapso")
    fase4 = _painel_via_aerea("despertar")

    html = f"""
<div style="font-family:sans-serif;text-align:center;">
  <div style="font-weight:bold;font-size:14px;margin-bottom:8px;color:#222;">
    Veja o ciclo passo a passo (cada fase dura 4s — ciclo total 16s)
  </div>
  <div style="position:relative;width:300px;height:340px;margin:0 auto;">
    <div style="position:absolute;top:0;left:0;animation: fade1 16s infinite;">{fase1}</div>
    <div style="position:absolute;top:0;left:0;animation: fade2 16s infinite;">{fase2}</div>
    <div style="position:absolute;top:0;left:0;animation: fade3 16s infinite;">{fase3}</div>
    <div style="position:absolute;top:0;left:0;animation: fade4 16s infinite;">{fase4}</div>
  </div>
</div>
<style>
  @keyframes fade1 {{
    0%,22% {{ opacity:1; }} 25%,100% {{ opacity:0; }}
  }}
  @keyframes fade2 {{
    0%,22% {{ opacity:0; }} 25%,47% {{ opacity:1; }} 50%,100% {{ opacity:0; }}
  }}
  @keyframes fade3 {{
    0%,47% {{ opacity:0; }} 50%,72% {{ opacity:1; }} 75%,100% {{ opacity:0; }}
  }}
  @keyframes fade4 {{
    0%,72% {{ opacity:0; }} 75%,97% {{ opacity:1; }} 100% {{ opacity:0; }}
  }}
</style>
"""
    components.html(html, height=400)


def animacao_vibracao_palato() -> None:
    """Vibração lenta e visível do palato mole — câmara lenta para fins didáticos."""
    svg = """
<div style="font-family:sans-serif;">
  <div style="text-align:center;font-weight:bold;font-size:15px;margin-bottom:8px;color:#222;">
    Como nasce o ronco — vibração do palato mole (câmara lenta)
  </div>
<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;">
  <defs>
    <marker id="ar_in" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="#3399ff"/>
    </marker>
  </defs>

  <!-- Fundo claro -->
  <rect width="600" height="360" fill="#fafafa"/>

  <!-- Cabeça simplificada (vista lateral) -->
  <path d="M 60,80 Q 60,50 100,50 L 470,50 Q 510,50 510,90 L 510,300 L 60,300 Z"
        fill="white" stroke="#666" stroke-width="2"/>

  <!-- Palato duro (osso, fixo) -->
  <rect x="100" y="120" width="240" height="16" fill="#d4b890" stroke="#8b6f47" stroke-width="1.2"/>
  <text x="220" y="111" font-size="12" fill="#222" text-anchor="middle">PALATO DURO (não vibra)</text>

  <!-- Marca anatómica: palato mole em repouso (linha tracejada cinza) -->
  <line x1="340" y1="136" x2="380" y2="170" stroke="#bbb" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Palato mole + úvula que VIBRA visivelmente (lenta + amplitude grande para didática) -->
  <g>
    <path fill="#ffaaaa" stroke="#992222" stroke-width="2">
      <animate attributeName="d" dur="1.2s" repeatCount="indefinite"
        values="
          M 340,136 Q 365,160 360,195 L 350,210 L 345,195 Q 335,160 340,136 Z;
          M 340,136 Q 395,170 390,225 L 380,240 L 375,225 Q 335,170 340,136 Z;
          M 340,136 Q 365,160 360,195 L 350,210 L 345,195 Q 335,160 340,136 Z;
          M 340,136 Q 305,170 310,225 L 320,240 L 325,225 Q 345,170 340,136 Z;
          M 340,136 Q 365,160 360,195 L 350,210 L 345,195 Q 335,160 340,136 Z
        "/>
    </path>
  </g>
  <text x="395" y="180" font-size="13" fill="#cc0000" font-weight="bold">PALATO MOLE</text>
  <text x="395" y="197" font-size="13" fill="#cc0000" font-weight="bold">+ ÚVULA</text>
  <text x="395" y="215" font-size="11" fill="#666">vibra com a passagem</text>
  <text x="395" y="228" font-size="11" fill="#666">do ar</text>

  <!-- Língua (fixa) -->
  <path d="M 60,300 Q 200,210 340,220 Q 360,222 510,300 Z"
        fill="#e08080" stroke="#aa3333" stroke-width="1.2"/>
  <text x="200" y="285" font-size="11" fill="white" font-weight="bold">língua</text>

  <!-- Setas de ar a entrar -->
  <line x1="80" y1="195" x2="290" y2="195" stroke="#3399ff" stroke-width="6"
        marker-end="url(#ar_in)" opacity="0.85"/>
  <text x="100" y="187" font-size="13" fill="#3399ff" font-weight="bold">ar entra →</text>

  <!-- Ondas sonoras a sair (lentas e visíveis) -->
  <g>
    <circle cx="370" cy="220" r="20" fill="none" stroke="#cc4400" stroke-width="3" opacity="0.6">
      <animate attributeName="r" dur="1.2s" repeatCount="indefinite" values="10;55;10"/>
      <animate attributeName="opacity" dur="1.2s" repeatCount="indefinite" values="0.8;0;0.8"/>
    </circle>
    <circle cx="370" cy="220" r="20" fill="none" stroke="#cc4400" stroke-width="3" opacity="0.4">
      <animate attributeName="r" dur="1.2s" begin="0.6s" repeatCount="indefinite" values="10;55;10"/>
      <animate attributeName="opacity" dur="1.2s" begin="0.6s" repeatCount="indefinite" values="0.6;0;0.6"/>
    </circle>
  </g>
  <text x="380" y="265" font-size="13" fill="#cc4400" font-weight="bold">som = RONCO</text>

  <!-- Etiqueta "câmara lenta" -->
  <rect x="20" y="20" width="120" height="22" rx="3" fill="#ffea99" stroke="#cc8800"/>
  <text x="80" y="35" font-size="11" font-weight="bold" fill="#996600" text-anchor="middle">
    🐢 câmara lenta
  </text>

  <!-- Notas técnicas -->
  <text x="20" y="335" font-size="11" fill="#666" font-style="italic">
    No ronco real a frequência é 30-100 Hz (60+ vibrações por segundo).
  </text>
  <text x="20" y="350" font-size="11" fill="#666" font-style="italic">
    A palatoplastia torna o palato mais firme — vibra menos = ronca menos.
  </text>
</svg>
</div>
"""
    components.html(svg, height=400)


def animacao_ciclo_respiratorio() -> None:
    """Ciclo respiratório normal vs apneia — comparação lado-a-lado."""
    svg = """
<div style="display:flex;justify-content:center;font-family:sans-serif;">
<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;">
  <text x="20" y="22" font-size="14" font-weight="bold" fill="#222">
    Padrão respiratório: NORMAL vs SAOS
  </text>

  <!-- Lado esquerdo: NORMAL -->
  <text x="80" y="50" font-size="13" font-weight="bold" fill="#449944">✓ Sono normal</text>
  <line x1="40" y1="120" x2="320" y2="120" stroke="#bbb" stroke-width="0.8"/>
  <path fill="none" stroke="#449944" stroke-width="2.5">
    <animate attributeName="d" dur="3s" repeatCount="indefinite"
      values="
        M 40,120 Q 70,80 100,120 Q 130,160 160,120 Q 190,80 220,120 Q 250,160 280,120 Q 310,80 320,120;
        M 40,120 Q 70,160 100,120 Q 130,80 160,120 Q 190,160 220,120 Q 250,80 280,120 Q 310,160 320,120;
        M 40,120 Q 70,80 100,120 Q 130,160 160,120 Q 190,80 220,120 Q 250,160 280,120 Q 310,80 320,120
      "/>
  </path>
  <text x="40" y="155" font-size="10" fill="#666">fluxo respiratório regular →</text>

  <!-- SpO2 normal -->
  <text x="40" y="195" font-size="11" font-weight="bold">SpO₂:</text>
  <rect x="80" y="180" width="240" height="20" fill="#e8f5e8" stroke="#449944"/>
  <text x="200" y="195" font-size="13" text-anchor="middle" font-weight="bold" fill="#449944">97-99%</text>

  <text x="40" y="240" font-size="11" font-weight="bold">Sono N3:</text>
  <rect x="100" y="225" width="180" height="20" fill="#449944" opacity="0.8"/>
  <text x="190" y="240" font-size="11" text-anchor="middle" fill="white" font-weight="bold">profundo, contínuo</text>

  <!-- Linha divisória -->
  <line x1="350" y1="40" x2="350" y2="300" stroke="#999" stroke-dasharray="4,4"/>

  <!-- Lado direito: APNEIA -->
  <text x="420" y="50" font-size="13" font-weight="bold" fill="#cc4444">✗ SAOS — apneias</text>
  <line x1="380" y1="120" x2="660" y2="120" stroke="#bbb" stroke-width="0.8"/>
  <path fill="none" stroke="#cc4444" stroke-width="2.5">
    <animate attributeName="d" dur="3s" repeatCount="indefinite"
      values="
        M 380,120 Q 410,90 440,120 Q 460,140 480,120 L 540,120 Q 560,140 580,120 Q 610,90 640,120 L 660,120;
        M 380,120 Q 410,150 440,120 Q 460,100 480,120 L 540,120 Q 560,100 580,120 Q 610,150 640,120 L 660,120;
        M 380,120 Q 410,90 440,120 Q 460,140 480,120 L 540,120 Q 560,140 580,120 Q 610,90 640,120 L 660,120
      "/>
  </path>
  <rect x="480" y="115" width="60" height="10" fill="#cc4444" opacity="0.3"/>
  <text x="510" y="100" font-size="10" text-anchor="middle" fill="#cc4444" font-weight="bold">APNEIA</text>
  <text x="380" y="155" font-size="10" fill="#666">fluxo interrompido →</text>

  <!-- SpO2 SAOS -->
  <text x="380" y="195" font-size="11" font-weight="bold">SpO₂:</text>
  <rect x="420" y="180" width="240" height="20" fill="#fde0e0" stroke="#cc4444"/>
  <text x="540" y="195" font-size="13" text-anchor="middle" font-weight="bold" fill="#cc4444">85-92% ↓</text>

  <text x="380" y="240" font-size="11" font-weight="bold">Sono N3:</text>
  <rect x="440" y="225" width="40" height="20" fill="#cc4444" opacity="0.8"/>
  <rect x="490" y="225" width="30" height="20" fill="#cc4444" opacity="0.8"/>
  <rect x="530" y="225" width="50" height="20" fill="#cc4444" opacity="0.8"/>
  <rect x="590" y="225" width="30" height="20" fill="#cc4444" opacity="0.8"/>
  <text x="540" y="265" font-size="10" text-anchor="middle" fill="#cc4444">fragmentado por micro-despertares</text>
</svg>
</div>
"""
    components.html(svg, height=340)


def hipnograma_inline(antes_pos: str = "antes") -> None:
    """Hipnograma realista usando Plotly — antes vs depois.

    Convenção: 0=Wake, 1=REM, 2=N1, 3=N2, 4=N3 (eixo invertido).
    """
    import plotly.graph_objects as go

    if antes_pos == "antes":
        # Sono fragmentado: muitos micro-despertares, pouco N3, REM curto
        # ~7h de sono em passos de 15 min = 28 pontos
        tempos = list(range(0, 421, 15))  # min
        fases = [
            0, 2, 3, 0, 2, 3, 0, 2, 3, 4, 3, 0,  # primeira parte fragmentada
            2, 3, 0, 2, 3, 0, 1, 0, 2, 3, 0, 2,  # mais wake, pouca N3
            3, 0, 1, 0, 2,
        ][: len(tempos)]
        cor = "#dc2626"
        titulo = "❌ Sono FRAGMENTADO (típico de SAOS não tratada)"
        nota = (
            "Note: incursões repetidas a Wake (micro-despertares), pouco tempo "
            "em N3, REM apenas em fragmentos."
        )
    else:
        # Sono consolidado: ciclos NREM/REM regulares, N3 nas primeiras horas
        tempos = list(range(0, 421, 15))
        fases = [
            0, 2, 3, 4, 4, 4, 3, 2, 1, 1,         # ciclo 1: descida funda + REM
            2, 3, 4, 4, 3, 2, 1, 1, 1,             # ciclo 2: N3 + REM longo
            2, 3, 3, 2, 1, 1, 1, 1, 2,             # ciclo 3: predomina REM
        ][: len(tempos)]
        cor = "#059669"
        titulo = "✅ Sono CONSOLIDADO (após tratamento eficaz)"
        nota = (
            "Note: ciclos regulares de ~90 min. Tempo longo em N3 nas primeiras "
            "horas. REM aumenta nos últimos ciclos. Mínimas incursões a Wake."
        )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=tempos,
            y=fases,
            mode="lines",
            line=dict(color=cor, width=2.5, shape="hv"),
            fill="tozeroy",
            fillcolor=f"rgba({'220,38,38' if cor=='#dc2626' else '5,150,105'},0.08)",
            hovertemplate="<b>%{customdata}</b><br>min %{x}<extra></extra>",
            customdata=[
                ["Wake", "REM", "N1", "N2", "N3"][f] for f in fases
            ],
        )
    )

    fig.update_layout(
        title=dict(text=titulo, font=dict(size=14)),
        xaxis=dict(
            title="Tempo de sono (minutos desde adormecer)",
            range=[0, 420],
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
        ),
        yaxis=dict(
            tickmode="array",
            tickvals=[0, 1, 2, 3, 4],
            ticktext=["<b>Wake</b>", "REM", "N1", "N2", "<b>N3</b><br>(profundo)"],
            range=[4.5, -0.5],
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
        ),
        height=320,
        margin=dict(l=80, r=20, t=50, b=50),
        plot_bgcolor="white",
        showlegend=False,
    )

    st.plotly_chart(fig, width=620)
    st.caption(nota)
