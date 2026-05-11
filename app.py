import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SuperAção SP – Plataforma Interativa",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Shared CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@700;900&family=Source+Sans+3:wght@400;600;700&display=swap');

  /* Reset */
  html, body, [class*="css"] { font-family: 'Source Sans 3', sans-serif; }

  /* Background */
  .stApp { background: linear-gradient(135deg, #fff8f0 0%, #fffbeb 100%); }

  /* Hide default streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding-top: 0 !important; max-width: 1100px; }

  /* ── NAV ── */
  .nav-bar {
    background: #fff;
    border-bottom: 4px solid #F79620;
    padding: 20px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 40px;
    border-radius: 0 0 12px 12px;
    box-shadow: 0 4px 16px rgba(0,0,0,.08);
  }
  .nav-logo { display: flex; align-items: center; gap: 12px; }
  .nav-logo h1 { font-family:'Merriweather',serif; font-size:26px; color:#1f2937; margin:0; }
  .nav-links { display:flex; gap:12px; }
  .nav-btn {
    display:inline-flex; align-items:center; gap:8px;
    padding:10px 24px; border-radius:12px;
    font-size:17px; font-weight:700; text-decoration:none; cursor:pointer;
    transition: all .2s;
  }
  .nav-btn-suas { background:#8C8D3A; color:#fff; }
  .nav-btn-servicos { background:#F79620; color:#fff; }
  .nav-btn-inactive { background:#f3f4f6; color:#374151; }
  .nav-btn-inactive:hover { background:#e5e7eb; }

  /* ── CARDS ── */
  .card {
    background:#fff; border-radius:24px;
    box-shadow:0 8px 32px rgba(0,0,0,.08);
    padding:48px; margin-bottom:32px;
  }
  .card-orange  { border-top:4px solid #F79620; }
  .card-olive   { border-top:4px solid #8C8D3A; }
  .card-blue    { border-top:4px solid #0D5A94; }
  .card-red     { border-top:4px solid #EE2C35; }

  .card-amber { background:linear-gradient(135deg,#fffbeb,#fff7ed); border:2px solid #fde68a; border-radius:24px; padding:48px; margin-bottom:32px; }
  .card-olive-grad { background:linear-gradient(135deg,#8C8D3A,#a8a94c); border-radius:24px; padding:48px; margin-bottom:32px; color:#fff; }
  .card-orange-grad { background:linear-gradient(135deg,#F79620,#f9ab49); border-radius:24px; padding:48px; margin-bottom:32px; color:#fff; text-align:center; }
  .card-blue-grad { background:linear-gradient(135deg,#0D5A94,#1a72b8); border-radius:24px; padding:48px; margin-bottom:32px; color:#fff; }
  .card-red-grad { background:linear-gradient(135deg,#EE2C35,#f44d55); border-radius:24px; padding:48px; margin-bottom:32px; color:#fff; }
  .card-red-grad2 { background:linear-gradient(135deg,#d92830,#EE2C35); border-radius:24px; padding:48px; margin-bottom:32px; color:#fff; }

  /* ── TYPOGRAPHY ── */
  .section-title { font-family:'Merriweather',serif; font-size:36px; font-weight:900; color:#1f2937; margin:0 0 16px; }
  .section-title-white { font-family:'Merriweather',serif; font-size:36px; font-weight:900; color:#fff; margin:0 0 16px; }
  .section-subtitle { font-size:20px; color:#4b5563; line-height:1.7; margin:0 0 32px; }
  .section-subtitle-white { font-size:20px; color:rgba(255,255,255,.9); line-height:1.7; margin:0 0 32px; }
  .section-h3 { font-family:'Merriweather',serif; font-size:28px; font-weight:700; color:#1f2937; margin:0 0 24px; }
  .section-h3-white { font-family:'Merriweather',serif; font-size:28px; font-weight:700; color:#fff; margin:0 0 24px; }
  .body-text { font-size:18px; color:#374151; line-height:1.8; }
  .body-text-white { font-size:18px; color:rgba(255,255,255,.95); line-height:1.8; }

  /* ── HIGHLIGHT BOX ── */
  .highlight-box { background:#fff; border-left:4px solid #F59E0B; border-radius:12px; padding:24px 28px; font-size:18px; color:#374151; line-height:1.8; }
  .highlight-box-white { background:rgba(255,255,255,.15); border-radius:16px; padding:24px 28px; font-size:18px; color:#fff; line-height:1.8; margin-bottom:20px; }

  /* ── INFO PILLS ── */
  .info-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:24px; }
  .info-pill { background:rgba(255,255,255,.12); border-radius:12px; padding:20px; }
  .info-pill strong { display:block; font-size:15px; margin-bottom:6px; }
  .info-pill span { font-size:17px; }

  /* ── SERVICE CARDS ── */
  .svc-header { border-radius:16px 16px 0 0; padding:28px 32px; display:flex; align-items:flex-start; gap:16px; }
  .svc-header-blue { background:linear-gradient(90deg,#0D5A94,#1a72b8); }
  .svc-header-red  { background:linear-gradient(90deg,#EE2C35,#f44d55); }
  .svc-header-red2 { background:linear-gradient(90deg,#d92830,#EE2C35); }
  .svc-body { background:#fff; border-radius:0 0 16px 16px; padding:32px; margin-bottom:28px; box-shadow:0 6px 24px rgba(0,0,0,.07); }
  .svc-title { font-family:'Merriweather',serif; font-size:22px; font-weight:700; color:#fff !important; margin:0; }
  .svc-icon { font-size:36px; flex-shrink:0; }
  .svc-label { font-size:15px; font-weight:700; color:#1f2937; margin:0 0 6px; }
  .svc-value { font-size:17px; color:#374151; margin:0 0 20px; }
  .bullet { display:flex; gap:10px; align-items:flex-start; margin-bottom:10px; }
  .dot-blue { width:8px;height:8px;border-radius:50%;background:#0D5A94;margin-top:8px;flex-shrink:0; }
  .dot-red  { width:8px;height:8px;border-radius:50%;background:#EE2C35;margin-top:8px;flex-shrink:0; }

  /* ── CTA BUTTON ── */
  .cta-btn {
    display:inline-flex; align-items:center; gap:10px;
    background:#fff; border-radius:999px;
    padding:16px 36px; font-size:18px; font-weight:700;
    box-shadow:0 4px 20px rgba(0,0,0,.15); cursor:pointer;
    border:none; text-decoration:none;
  }
  .cta-btn-orange { color:#F79620; }
  .cta-btn-olive  { color:#8C8D3A; }

  /* ── CRAS / CREAS HERO CARDS ── */
  .hero-card {
    border-radius:24px; padding:40px; color:#fff;
    transition: transform .2s, box-shadow .2s;
    cursor:pointer; margin-bottom:0;
  }
  .hero-card:hover { transform:scale(1.03); box-shadow:0 16px 48px rgba(0,0,0,.2); }
  .hero-card-blue { background:linear-gradient(135deg,#0D5A94,#1a72b8); }
  .hero-card-red  { background:linear-gradient(135deg,#EE2C35,#f44d55); }
  .hero-card h2 { font-family:'Merriweather',serif; font-size:40px; font-weight:900; margin:16px 0 8px; }
  .hero-card p  { font-size:18px; margin:0 0 20px; }
  .hero-card .inner-box { background:rgba(255,255,255,.2); border-radius:16px; padding:20px; margin-bottom:20px; }
  .hero-card .inner-box strong { display:block; font-size:16px; margin-bottom:8px; }
  .hero-card .inner-box p { font-size:16px; margin:0; }
  .hero-card .arrow-link { font-size:17px; font-weight:700; display:flex; align-items:center; gap:8px; }

  /* ── DIVIDER ── */
  .divider { border:none; border-top:1px solid #e5e7eb; margin:8px 0 32px; }

  /* Streamlit button overrides */
  .stButton > button {
    border-radius:12px !important;
    font-weight:700 !important;
    font-size:16px !important;
    padding:10px 24px !important;
    border:none !important;
    transition: all .2s !important;
  }

  /* Item 5: prevent the navbar button labels from wrapping to a second line */
  .stButton > button p,
  .stButton > button div { white-space: nowrap !important; }
  .stButton > button { white-space: nowrap !important; }

  /* ── ATTACHED CTA BUTTONS ────────────────────────────────────────────────
     We can't literally insert a Streamlit button inside a markdown card,
     so we use invisible "marker" divs together with CSS :has() selectors
     to style the button that immediately follows the marker, making it
     visually merge with the preceding card. */

  /* Cards that visually continue into the CTA button below */
  .hero-card.with-cta,
  .card-orange-grad.with-cta,
  .card-olive-grad.with-cta {
    border-radius: 24px 24px 0 0 !important;
    margin-bottom: 0 !important;
    padding-bottom: 28px !important;
  }

  /* Hide the marker container but keep it in DOM for sibling selection */
  .cta-marker { display:none; }
  div[data-testid="stVerticalBlock"] > div[data-testid="element-container"]:has(.cta-marker) {
    height: 0; margin: 0; padding: 0;
  }

  /* Pull the button up to sit flush against the card above */
  div[data-testid="element-container"]:has(.cta-marker) + div[data-testid="element-container"] {
    margin-top: 0 !important;
    margin-bottom: 32px !important;
  }
  div[data-testid="element-container"]:has(.cta-marker) + div[data-testid="element-container"] .stButton > button {
    border-radius: 0 0 24px 24px !important;
    padding: 18px 24px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    border: none !important;
    width: 100% !important;
    box-shadow: 0 6px 24px rgba(0,0,0,.10) !important;
    transition: filter .2s, transform .2s !important;
  }
  div[data-testid="element-container"]:has(.cta-marker) + div[data-testid="element-container"] .stButton > button:hover {
    filter: brightness(1.06);
    transform: translateY(-1px);
  }

  /* CRAS attached button (blue gradient, white text) */
  div[data-testid="element-container"]:has(.cta-marker.cta-cras) + div[data-testid="element-container"] .stButton > button {
    background: linear-gradient(135deg,#0D5A94,#1a72b8) !important;
    color: #fff !important;
  }
  /* CREAS attached button (red gradient, white text) */
  div[data-testid="element-container"]:has(.cta-marker.cta-creas) + div[data-testid="element-container"] .stButton > button {
    background: linear-gradient(135deg,#EE2C35,#f44d55) !important;
    color: #fff !important;
  }
  /* "Ver todos os serviços" attached button (white bg over orange card) */
  div[data-testid="element-container"]:has(.cta-marker.cta-all) + div[data-testid="element-container"] .stButton > button {
    background: #fff !important;
    color: #F79620 !important;
  }
  /* "Voltar ao SUAS" attached button (white bg over olive card) */
  div[data-testid="element-container"]:has(.cta-marker.cta-back) + div[data-testid="element-container"] .stButton > button {
    background: #fff !important;
    color: #8C8D3A !important;
  }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "suas"

# ── NAV ──────────────────────────────────────────────────────────────────────
col_logo, col_nav = st.columns([5, 6])
with col_logo:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px;padding:20px 0 8px;">
      <span style="font-size:40px;line-height:1;">🏆</span>
      <h1 style="font-family:Merriweather,serif;font-size:26px;color:#1f2937;margin:0;">SuperAção SP</h1>
    </div>
    """, unsafe_allow_html=True)

with col_nav:
    st.markdown("<div style='padding-top:20px;'></div>", unsafe_allow_html=True)
    n1, n2 = st.columns([1, 2])
    with n1:
        if st.button("🤝 SUAS", key="btn_suas",
                     type="primary" if st.session_state.page == "suas" else "secondary",
                     use_container_width=True):
            st.session_state.page = "suas"
            st.rerun()
    with n2:
        if st.button("💼 Serviços CRAS e CREAS", key="btn_servicos",
                     type="primary" if st.session_state.page == "servicos" else "secondary",
                     use_container_width=True):
            st.session_state.page = "servicos"
            st.rerun()

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: SUAS
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "suas":

    # Hero
    st.markdown("""
    <div class="card card-olive" style="text-align:center;">
      <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:20px;">
        <span style="font-size:56px;">🤝</span>
        <h2 class="section-title" style="font-size:40px;">Sistema Único de Assistência Social</h2>
      </div>
      <p class="section-subtitle">Ferramenta de Apoio para Agentes Sociais do Programa SuperAção SP</p>
    </div>
    """, unsafe_allow_html=True)

    # O que é
    st.markdown("""
    <div class="card-amber">
      <h3 class="section-h3">O que é o SUAS?</h3>
      <p class="body-text"><strong>Conceito:</strong> Política pública não contributiva, parte da
      seguridade social brasileira, regulamentada pela Lei Orgânica da Assistência Social
      (LOAS, Lei nº 8.742/1993).</p><br>
      <p class="body-text"><strong>Objetivo Central:</strong> Garantir proteção social às famílias
      e indivíduos em situação de vulnerabilidade social, promovendo direitos, cidadania e
      redução das desigualdades sociais.</p><br>
      <div class="highlight-box">
        Em 2005, foi criado o Sistema Único de Assistência Social (SUAS). Ele serve para organizar
        o funcionamento da Assistência Social em todo o Brasil. O SUAS garante que a União, os Estados
        e os Municípios trabalhem juntos para oferecer essa proteção, compartilhando recursos e
        informações para que as famílias recebam o apoio de que precisam.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Como funciona
    st.markdown('<h3 class="section-h3" style="margin-bottom:20px;">Como o SUAS Funciona?</h3>',
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background:#e8f0f9;border:2px solid #9ab8d9;border-radius:20px;padding:32px;height:100%;">
          <div style="font-size:44px;margin-bottom:16px;">🛡️</div>
          <h4 style="font-size:20px;font-weight:700;color:#1f2937;margin:0 0 16px;">Forma de Funcionamento</h4>
          <div class="bullet"><div class="dot-blue"></div>
            <span class="body-text">Execução descentralizada articulando União, Estados, Municípios e Distrito Federal</span></div>
          <div class="bullet"><div class="dot-blue"></div>
            <span class="body-text">Atuação organizada em proteção social básica (preventiva) e proteção social especial (violações de direitos)</span></div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background:#fff4e5;border:2px solid #f5c97a;border-radius:20px;padding:32px;height:100%;">
          <div style="font-size:44px;margin-bottom:16px;">⚙️</div>
          <h4 style="font-size:20px;font-weight:700;color:#1f2937;margin:0 0 16px;">Instrumentos e Serviços</h4>
          <div class="bullet"><div style="width:8px;height:8px;border-radius:50%;background:#F79620;margin-top:8px;flex-shrink:0;"></div>
            <span class="body-text">CRAS e CREAS (equipamentos públicos)</span></div>
          <div class="bullet"><div style="width:8px;height:8px;border-radius:50%;background:#F79620;margin-top:8px;flex-shrink:0;"></div>
            <span class="body-text">Serviços de acolhimento institucional</span></div>
          <div class="bullet"><div style="width:8px;height:8px;border-radius:50%;background:#F79620;margin-top:8px;flex-shrink:0;"></div>
            <span class="body-text">Programas de transferência de renda (ex.: Bolsa Família)</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:32px;'></div>", unsafe_allow_html=True)

    # SuperAção & SUAS
    st.markdown("""
    <div class="card-olive-grad">
      <h3 class="section-h3-white" style="text-align:center;">SuperAção SP e o SUAS</h3>
      <p class="body-text-white">
        <strong>A interface entre o Programa SuperAção SP e o Sistema Único de Assistência Social
        (SUAS) é essencial</strong> para assegurar a efetividade e a sustentabilidade dos resultados pretendidos.
      </p><br>
      <p class="body-text-white">
        O sucesso do Programa SuperAção SP implica garantir que as famílias participantes tenham
        acesso efetivo aos direitos sociais, políticas e serviços, possibilitando a inclusão no
        mundo do trabalho, a geração de renda e a melhoria concreta e duradoura de suas condições de vida.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Equipamentos públicos
    st.markdown('<h3 class="section-h3" style="text-align:center;margin-bottom:24px;">Equipamentos Públicos do SUAS</h3>',
                unsafe_allow_html=True)
    col_cras, col_creas = st.columns(2)
    with col_cras:
        st.markdown("""
        <div class="hero-card hero-card-blue with-cta">
          <div style="font-size:52px;">🏠</div>
          <h2>CRAS</h2>
          <p>Centro de Referência de Assistência Social</p>
          <div class="inner-box">
            <strong>Proteção Social Básica (Preventiva)</strong>
            <p>Porta de entrada da Assistência Social. Atendimento familiar e comunitário para prevenção de situações de risco.</p>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="cta-marker cta-cras"></div>', unsafe_allow_html=True)
        if st.button("Ver serviços do CRAS →", key="goto_cras", use_container_width=True):
            st.session_state.page = "servicos"
            st.session_state.scroll_to = "cras"
            st.rerun()

    with col_creas:
        st.markdown("""
        <div class="hero-card hero-card-red with-cta">
          <div style="font-size:52px;">❤️</div>
          <h2>CREAS</h2>
          <p>Centro de Referência Especializado de Assistência Social</p>
          <div class="inner-box">
            <strong>Proteção Social Especial (Interventiva)</strong>
            <p>Atendimento especializado para famílias e indivíduos em situação de violação de direitos e violência.</p>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="cta-marker cta-creas"></div>', unsafe_allow_html=True)
        if st.button("Ver serviços do CREAS →", key="goto_creas", use_container_width=True):
            st.session_state.page = "servicos"
            st.session_state.scroll_to = "creas"
            st.rerun()

    st.markdown("<div style='margin-bottom:32px;'></div>", unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div class="card-orange-grad with-cta">
      <h3 class="section-h3-white">Explore os Serviços Detalhados</h3>
      <p class="section-subtitle-white">
        Clique nos cards acima ou no menu de navegação para conhecer todos os serviços
        oferecidos pelo CRAS e CREAS
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="cta-marker cta-all"></div>', unsafe_allow_html=True)
    if st.button("Ver Todos os Serviços →", key="cta_all", use_container_width=True):
        st.session_state.page = "servicos"
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: SERVIÇOS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "servicos":

    # Back button
    if st.button("← Voltar ao SUAS", key="back"):
        st.session_state.page = "suas"
        st.rerun()

    # Hero
    st.markdown("""
    <div class="card card-orange" style="text-align:center;margin-top:12px;">
      <h2 class="section-title">Serviços do CRAS e CREAS</h2>
      <p class="section-subtitle">Conheça todos os serviços oferecidos pelos equipamentos públicos do SUAS</p>
    </div>
    """, unsafe_allow_html=True)

    # ── CRAS ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="card-blue-grad" id="cras">
      <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px;">
        <span style="font-size:56px;">🏠</span>
        <div>
          <h3 style="font-family:Merriweather,serif;font-size:44px;font-weight:900;color:#fff;margin:0;">CRAS</h3>
          <p style="font-size:20px;color:rgba(255,255,255,.9);margin:4px 0 0;">Centro de Referência de Assistência Social</p>
        </div>
      </div>
      <div class="highlight-box-white">
        <strong style="font-size:20px;">Proteção Social Básica (Preventiva)</strong><br><br>
        O CRAS é a porta de entrada da Assistência Social nos territórios. É um equipamento
        público mantido pelo município e oferece os serviços da Proteção Social Básica.<br><br>
        <strong>Funções principais:</strong> Fazer a gestão da rede socioassistencial do território
        e executar o PAIF – Serviço de Proteção e Atendimento Integral à Família.
      </div>
      <div class="info-grid">
        <div class="info-pill"><strong>Tipo de Proteção</strong><span>Básica (Preventiva)</span></div>
        <div class="info-pill"><strong>Nível de Atendimento</strong><span>Familiar e Comunitário</span></div>
        <div class="info-pill"><strong>Situação</strong><span>Risco social e prevenção</span></div>
      </div>
      <h4 style="font-size:24px;font-weight:700;color:#fff;margin:8px 0 0;">Serviços Oferecidos pelo CRAS:</h4>
    </div>
    """, unsafe_allow_html=True)

    servicos_cras = [
        {
            "icon": "👥",
            "nome": "PAIF – Proteção e Atendimento Integral à Família",
            "local": "CRAS (obrigatório)",
            "publico": "Famílias, idosos, pessoas com deficiência, crianças",
            "objetivos": [
                "Fortalecer os laços familiares",
                "Prevenir situações de violência",
                "Promover o acesso a serviços públicos",
                "Garantir proteção a idosos, pessoas com deficiência e crianças em situação de dependência",
            ],
        },
        {
            "icon": "📖",
            "nome": "SCFV – Serviço de Convivência e Fortalecimento de Vínculos",
            "local": "CRAS ou Organizações da Sociedade Civil cadastradas (complementar ao PAIF)",
            "publico": "Crianças, jovens, adultos e idosos (atendimento em grupos)",
            "objetivos": [
                "Oferecer atividades socioeducativas e culturais",
                "Fortalecer o convívio familiar e comunitário",
                "Promover o exercício da cidadania",
            ],
        },
        {
            "icon": "🤲",
            "nome": "Proteção Social Básica no Domicílio para Pessoas com Deficiência e Idosas",
            "local": "No domicílio da pessoa atendida (vinculado ao CRAS e complementar ao PAIF)",
            "publico": "Pessoas com deficiência ou idosos com limitações físicas ou sociais",
            "objetivos": [
                "Realizar visitas regulares por equipe especializada",
                "Identificar necessidades, promover cuidado",
                "Garantir acesso a direitos, autonomia e inclusão social",
                "Garantir acompanhamento técnico contínuo",
            ],
        },
    ]

    for s in servicos_cras:
        bullets_html = "".join(
            f'<div class="bullet"><div class="dot-blue"></div><span class="body-text">{o}</span></div>'
            for o in s["objetivos"]
        )
        st.markdown(f"""
        <div>
          <div class="svc-header svc-header-blue">
            <span class="svc-icon">{s['icon']}</span>
            <h4 class="svc-title">{s['nome']}</h4>
          </div>
          <div class="svc-body">
            <p class="svc-label">Local de Oferta:</p>
            <p class="svc-value">{s['local']}</p>
            <p class="svc-label">Público-alvo:</p>
            <p class="svc-value">{s['publico']}</p>
            <p class="svc-label">Principais Objetivos:</p>
            {bullets_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── CREAS ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="card-red-grad" id="creas">
      <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px;">
        <span style="font-size:56px;">❤️</span>
        <div>
          <h3 style="font-family:Merriweather,serif;font-size:44px;font-weight:900;color:#fff;margin:0;">CREAS</h3>
          <p style="font-size:20px;color:rgba(255,255,255,.9);margin:4px 0 0;">Centro de Referência Especializado de Assistência Social</p>
        </div>
      </div>
      <div class="highlight-box-white">
        <strong style="font-size:20px;">Proteção Social Especial (Interventiva)</strong><br><br>
        O CREAS é o equipamento público municipal especializado em oferecer serviços de Proteção
        Social Especial. Ele atende famílias e indivíduos que vivenciam situações de risco social,
        violação de direitos ou violência.<br><br>
        <strong>Funções principais:</strong> Coordenar a rede de proteção social especializada no
        território e executar o PAEFI – Serviço de Proteção e Atendimento Especializado a Famílias e Indivíduos.
      </div>
      <div class="info-grid">
        <div class="info-pill"><strong>Tipo de Proteção</strong><span>Especial (Interventiva)</span></div>
        <div class="info-pill"><strong>Nível de Atendimento</strong><span>Individual e Familiar</span></div>
        <div class="info-pill"><strong>Situação</strong><span>Violação ou risco grave instalado</span></div>
      </div>
      <h4 style="font-size:24px;font-weight:700;color:#fff;margin:8px 0 4px;">Proteção Social Especial de Média Complexidade</h4>
      <div class="info-pill" style="background:rgba(255,255,255,.15);font-size:17px;color:#fff;margin-top:8px;">
        Casos que exigem acompanhamento especializado, sem necessidade de acolhimento institucional
      </div>
    </div>
    """, unsafe_allow_html=True)

    servicos_media = [
        ("🛡️", "PAEFI – Serviço de Atendimento Especializado a Famílias e Indivíduos",
         "Atendimento especializado para famílias e indivíduos em situação de violação de direitos"),
        ("👥", "Serviço Especializado de Abordagem Social",
         "Busca ativa e abordagem de pessoas em situação de rua ou vulnerabilidade extrema"),
        ("✅", "Serviço de Proteção Social a Adolescentes em Cumprimento de Medida Socioeducativa (LA e PSC)",
         "Acompanhamento de adolescentes em Liberdade Assistida e Prestação de Serviços à Comunidade"),
        ("🤲", "Serviço de Proteção Social Especial para Pessoas com Deficiência, Idosas e suas Famílias",
         "Atendimento especializado visando prevenção de agravos e inclusão social"),
        ("🏠", "Serviço Especializado para Pessoas em Situação de Rua",
         "Acompanhamento especializado e construção de projeto de vida"),
    ]

    for icon, nome, desc in servicos_media:
        st.markdown(f"""
        <div>
          <div class="svc-header svc-header-red">
            <span class="svc-icon">{icon}</span>
            <h4 class="svc-title">{nome}</h4>
          </div>
          <div class="svc-body">
            <p class="body-text">{desc}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-red-grad2">
      <h4 style="font-size:26px;font-weight:700;color:#fff;margin:0 0 12px;">Proteção Social Especial de Alta Complexidade</h4>
      <div class="info-pill" style="background:rgba(255,255,255,.15);font-size:17px;color:#fff;">
        Oferece acolhimento institucional ou familiar temporário, em situações em que a proteção
        não é possível na família de origem
      </div>
    </div>
    """, unsafe_allow_html=True)

    servicos_alta = [
        ("🏠", "Serviço de Acolhimento Institucional",
         "Abrigo institucional, Casa-Lar, Casa de Passagem, Residência Inclusiva – proteção integral temporária"),
        ("👥", "Serviço de Acolhimento em República",
         "Moradia temporária com acompanhamento para jovens, adultos e idosos em situação de abandono"),
        ("👶", "Serviço de Acolhimento em Família Acolhedora",
         "Crianças e adolescentes afastados da família de origem são acolhidos por famílias cadastradas"),
        ("🛡️", "Serviço de Proteção em Situações de Calamidades Públicas e Emergências",
         "Atendimento emergencial em desastres naturais e situações de calamidade"),
    ]

    for icon, nome, desc in servicos_alta:
        st.markdown(f"""
        <div>
          <div class="svc-header svc-header-red2">
            <span class="svc-icon">{icon}</span>
            <h4 class="svc-title">{nome}</h4>
          </div>
          <div class="svc-body">
            <p class="body-text">{desc}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # Footer CTA
    st.markdown("""
    <div class="card-olive-grad with-cta" style="text-align:center;margin-top:8px;">
      <h3 class="section-h3-white">Material de Apoio para Agentes Sociais</h3>
      <p class="section-subtitle-white">
        Esta ferramenta foi desenvolvida para auxiliar os agentes sociais do Programa SuperAção SP
        no entendimento e articulação com a rede SUAS
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="cta-marker cta-back"></div>', unsafe_allow_html=True)
    if st.button("← Voltar ao SUAS", key="back_bottom", use_container_width=True):
        st.session_state.page = "suas"
        st.rerun()
