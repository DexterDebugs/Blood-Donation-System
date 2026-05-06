import streamlit as st
import requests
from components.styles import apply_styles
from components.emergency_footer import emergency_footer
st.set_page_config(page_title="Donor Login", page_icon="🔐")
apply_styles()

email = st.text_input("Email")
password = st.text_input("Password",type="password")

login_clicked = st.button("Login")

if login_clicked:
    response = requests.post(
        "http://127.0.0.1:8000/donors/login",
        json={"email":email, "password":password}
    )

    if response.status_code == 200:
        data = response.json()
        st.session_state["logged_in"] = True
        st.session_state["donor_id"] = data["donor_id"]
        st.session_state["donor_name"] = data["name"]
        st.switch_page("pages/Donor_Dashboard.py")
    else:
        st.error("Invalid email or password")

emergency_footer()