import streamlit as st
import requests

st.set_page_config(page_title="My Dashboard", page_icon="👤")

from components.styles import apply_styles
apply_styles()

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.switch_page("pages/Donor_Login.py")
    st.stop()

donor_id = st.session_state["donor_id"]
response = requests.get(f"http://127.0.0.1:8000/donors/{donor_id}")
donor = response.json()

st.write(f"**Name:** {donor['name']}")
st.write(f"**Email:** {donor['email']}")
st.write(f"**Blood Group:** {donor['blood_group']}")
st.write(f"**Phone:** {donor['phone']}")
st.write(f"**City:** {donor['city']}")
st.write(f"**Available:** {'✅ Yes' if donor['is_available'] else '❌ No'}")
st.write(f"**Last Donation:** {donor['last_donation_date']}")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("pages/Donor_Login.py")