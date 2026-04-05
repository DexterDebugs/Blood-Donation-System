import streamlit as st

def emergency_footer():
    st.markdown("""
        <style>
            .emergency-footer {
                background: linear-gradient(135deg, #ff8c00, #ffa533);
                color: white;
                padding: 20px 30px;
                border-radius: 12px;
                text-align: center;
                margin-top: 50px;
                box-shadow: 0 4px 15px rgba(255, 140, 0, 0.3);
            }
            .emergency-footer h4 {
                margin: 0;
                font-size: 1.1em;
                font-weight: 700;
                letter-spacing: 1px;
            }
            .emergency-number {
                font-size: 1.8em !important;
                font-weight: 800 !important;
                color: white !important;
                letter-spacing: 3px !important;
                margin: 8px 0 !important;
            }
            .emergency-footer p {
                margin: 5px 0 0 0;
                font-size: 0.9em;
                opacity: 0.9;
            }
        </style>

        <div class="emergency-footer">
            <h4>🚨 EMERGENCY BLOODLINE</h4>
            <p class="emergency-number">📞 104</p>
            <p>National Blood Transfusion Council Helpline — Available 24/7</p>
        </div>
    """, unsafe_allow_html=True)