import streamlit as st

st.set_page_config(
    page_title="BloodConnect",
    page_icon="🩸",
    layout="wide"
)

# --- CSS --------------------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] a {
            color: white !important;
            font-size: 1.1em;
            font-weight: 600;
            padding: 10px 15px;
            border-radius: 8px;
            display: block;
        }
        [data-testid="stSidebar"] a:hover {
            background: #f62d2d !important;
            height: 60px !important;    
        }

        /* Fix become donor button */
        .btn-primary, .btn-secondary {
            text-decoration: none !important;
            color: white !important;
        }

        .btn-secondary {
            color: #cc0000 !important;
        }
        /* Hide default streamlit header */
        [data-testid="stHeader"] {
            background: #f62d2d !important;
        }
        .hero {
            background: linear-gradient(135deg, rgba(204, 47, 47, 0.38), rgba(204,0,0,0.85)),
                        url('https://i.pinimg.com/736x/48/a0/1a/48a01ab26322d93bbd50bdda842be925.jpg') center/cover no-repeat;
            padding: 60px 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }        .hero h1 {
            font-size: 3em;
            font-weight: 800;
        }
        .hero p {
            font-size: 1.2em;
            opacity: 0.9;
        }
    </style>

    <div class="hero">
        <h1>🩸 Find Blood In Seconds</h1>
        <p>Smart matching connects you with available donors instantly.<br>
        Search by blood group and location in real time.</p>
    </div>
""", unsafe_allow_html=True)

# ── CTA Buttons ──────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .btn-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0 40px 0;
        }
        .btn-primary {
            background: #cc0000;
            color: white;
            padding: 18px 40px;
            border-radius: 10px;
            font-size: 1.2em;
            font-weight: 700;
            text-decoration: none;
            border: none;
            cursor: pointer;
        }
        .btn-secondary {
            background: transparent;
            color: #cc0000;
            padding: 18px 40px;
            border-radius: 10px;
            font-size: 1.2em;
            font-weight: 700;
            text-decoration: none;
            border: 2px solid #cc0000;
            cursor: pointer;
        }
    </style>

    <div class="btn-container">
        <a href="/Find_Blood" target="_self" class="btn-primary">🔍 Search for Blood</a>
        <a href="/Become_Donor" target="_self" class="btn-secondary">❤️ Become a Donor</a>
    </div>
""", unsafe_allow_html=True)
# ── Stats Section (Dummy Numbers) ────────────────────────────────────────────
st.markdown("""
    <style>
        .stats-container {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            flex: 1;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .stat-icon {
            font-size: 2em;
            margin-bottom: 10px;
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: 800;
            color: #cc0000;
        }
        .stat-label {
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }
        /* White text for all sidebar items */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Active page highlight */
        [data-testid="stSidebarNavLink"][aria-current="page"] {
            background-color: #cc0000 !important;
            border-radius: 8px;
        }
    </style>

    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-icon">⏱️</div>
            <div class="stat-number">30s</div>
            <div class="stat-label">Avg Search Time</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-number">1,240</div>
            <div class="stat-label">Registered Donors</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🩸</div>
            <div class="stat-number">All 8</div>
            <div class="stat-label">Blood Groups</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">📍</div>
            <div class="stat-number">47</div>
            <div class="stat-label">Cities Covered</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .how-container {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin: 30px 0;
        }
        .how-card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            flex: 1;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .how-icon {
            background: #cc0000;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5em;
            margin: 0 auto 15px auto;
        }
        .how-title {
            font-size: 1.2em;
            font-weight: 700;
            color: #111;
            margin-bottom: 10px;
        }
        .how-desc {
            color: #666;
            font-size: 0.9em;
        }
        .section-title {
            text-align: center;
            font-size: 2em;
            font-weight: 800;
            margin: 40px 0 10px 0;
            color: #111;
        }
        .section-subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
    </style>

    <div class="section-title">How It Works</div>
    <div class="section-subtitle">Three simple steps to find or donate blood</div>

    <div class="how-container">
        <div class="how-card">
            <div class="how-icon">🔍</div>
            <div class="how-title">1. Search</div>
            <div class="how-desc">Search by blood group and location to find matching donors in seconds.</div>
        </div>
        <div class="how-card">
            <div class="how-icon">📞</div>
            <div class="how-title">2. Connect</div>
            <div class="how-desc">Get donor contact details and reach out directly for quick coordination.</div>
        </div>
        <div class="how-card">
            <div class="how-icon">🩸</div>
            <div class="how-title">3. Save Lives</div>
            <div class="how-desc">Complete the donation process and help save someone's life today.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .cta-section {
            background: linear-gradient(135deg, #8B0000, #cc0000);
            border-radius: 15px;
            padding: 60px 40px;
            text-align: center;
            color: white;
            margin: 30px 0;
        }
        .cta-title {
            font-size: 2.5em;
            font-weight: 800;
            margin-bottom: 15px;
        }
        .cta-desc {
            font-size: 1.1em;
            opacity: 0.9;
            margin-bottom: 30px;
        }
    </style>

    <div class="cta-section">
        <div class="cta-title">Ready to Save a Life? ❤️</div>
        <div class="cta-desc">
            Join thousands of donors making a difference every day.<br>
            Your blood donation can save up to 3 lives.
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,2])
with col2:
    if st.button("❤️ Register Now", use_container_width=True):
        st.switch_page("pages/Become_Donor.py")