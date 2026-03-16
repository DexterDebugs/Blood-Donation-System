import streamlit as st

def apply_styles():
    # CSS only
    st.markdown("""
        <style>
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
            [data-testid="stHeader"] {
                background: #f62d2d !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML logo — separate block
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