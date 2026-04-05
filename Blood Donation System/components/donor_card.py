##styled card for each donor

import streamlit as st

def donor_card(donor):
    st.markdown(f"""
        <div style="
            background: white;
            border-radius: 12px;
            padding: 20px 25px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 5px solid #cc0000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <div>
                <h3 style="margin:0; color:#1a1a1a;">👤 {donor['name']}</h3>
                <p style="margin:5px 0; color:#666;">📍 {donor['city']}</p>
                <p style="margin:5px 0; color:#666;">📞 {donor['phone']}</p>
            </div>
            <div style="text-align:center;">
                <span style="
                    background: #cc0000;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 20px;
                    font-size: 1.3em;
                    font-weight: 800;
                ">{donor['blood_group']}</span>
                <p style="margin-top:8px; color:{'green' if donor['is_available'] else 'gray'};">
                    {'✅ Available' if donor['is_available'] else '❌ Unavailable'}
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)