import streamlit as st


def apply_styles():
    st.markdown("""
        <style>
            /* Import Google Font */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

            /* Apply font everywhere */
            * {
                font-family: 'Poppins', sans-serif !important;
            }
            /* Sidebar styling */
            [data-testid="stSidebar"] {
                background-color: #ff5858 !important;
            }
            [data-testid="stSidebar"] * {
                color: white !important;
            }
            [data-testid="stSidebarNavLink"] {
                font-size: 1.1em !important;
                font-weight: 600 !important;
                padding: 12px 16px !important;
            }
            [data-testid="stSidebarNavLink"]:hover {
                background-color: #cc0000 !important;
                border-radius: 8px;
            }
            [data-testid="stSidebarNavLink"][aria-current="page"] {
                background-color: #f62d2d !important;
                border-radius: 8px;
            }

            /* Header styling */
            [data-testid="stHeader"] {
                background: #f62d2d !important;
            }

            /* Hide anchor links on headings */
            h1 a, h2 a, h3 a, h4 a {
                display: none !important;
            }

            /* Button styling */
            [data-testid="stButton"] button {
                width: 200px !important;
                padding: 12px !important;
                font-size: 1.1em !important;
                cursor: pointer !important;
            }

            /* Input field styling */
            [data-testid="stTextInput"] input {
                background: white !important;
                border: 2px solid #ffcccc !important;
                border-radius: 8px !important;
                padding: 12px 16px !important;
                font-size: 1em !important;
                color: #1a1a1a !important;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
                cursor: text !important;
            }

            [data-testid="stTextInput"] input:focus {
                border: 2px solid #cc0000 !important;
                box-shadow: 0 0 0 3px rgba(204,0,0,0.1) !important;
            }

            [data-testid="stTextInput"] input::placeholder {
                color: #aaa !important;
                font-style: italic !important;
            }

            /* Input labels */
            [data-testid="stTextInput"] label,
            [data-testid="stSelectbox"] label {
                font-weight: 600 !important;
                color: #1a1a1a !important;
                font-size: 1em !important;
            }

            /* Selectbox cursor */
            [data-testid="stSelectbox"] * {
                cursor: pointer !important;
            }

            /* Nuclear fix for selectbox selected value */
            div[data-baseweb="select"] div[class*="single-value"],
            div[data-baseweb="select"] div[class*="singleValue"],
            div[data-baseweb="select"] > div > div > div,
            div[data-baseweb="select"] input,
            div[data-baseweb="select"] span:not([class*="indicator"]) {
                color: #1a1a1a !important;
                opacity: 1 !important;
                visibility: visible !important;
                -webkit-text-fill-color: #1a1a1a !important;
            }
            /* Stat card hover effect */
            .stat-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .stat-card:hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }

            /* How it works card hover */
            .how-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .how-card:hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }

            /* Button hover effects */
            .btn-primary {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .btn-primary:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(204,0,0,0.4) !important;
            }

            .btn-secondary {
                transition: all 0.2s ease !important;
            }
            .btn-secondary:hover {
                background: #cc0000 !important;
                color: white !important;
                transform: translateY(-2px) !important;
            }

            /* Donor card hover */
            .donor-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .donor-card:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }
            /* Hide Streamlit tooltips */
            [data-testid="stTooltipIcon"],
            [data-testid="stSidebar"] button title,
            .stTooltip {
                display: none !important;
            }

            /* Hide sidebar collapse button tooltip */
            [data-testid="stSidebarCollapseButton"] {
                display: none !important;
            }
            /* Main content padding */
            [data-testid="stAppViewContainer"] > div:nth-child(2) {
                padding: 2rem 3rem !important;
            }

            /* Better spacing between sections */
            .stats-container,
            .how-container {
                margin: 40px 0 !important;
            }

            /* Page titles styling */
            h1 {
                font-size: 2.5em !important;
                font-weight: 800 !important;
                color: #1a1a1a !important;
                margin-bottom: 5px !important;
            }

            /* Page subtitles */
            p {
                font-size: 1em !important;
                color: #555 !important;
                line-height: 1.6 !important;
            }

            /* Divider styling */
            hr {
                border: none !important;
                border-top: 1px solid #ffcccc !important;
                margin: 20px 0 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML logo
    st.markdown("""
        <div style="
            position: fixed;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 999;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        ">
            <span style="font-size: 1.5em;">🩸</span>
            <span style="
                color: white;
                font-size: 1.3em;
                font-weight: 800;
                letter-spacing: 1px;
                text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
            ">Blood<span style="color: #ffcccc;">Connect</span></span>
        </div>
    """, unsafe_allow_html=True)