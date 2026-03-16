import streamlit as st
import requests
from components.styles import apply_styles
apply_styles()


st.set_page_config(page_title="Find Blood", page_icon="🔍")

st.title("🔍 Find Blood")
st.write("Search for available donors near you.")
st.markdown("---")

# ── Search Form ──────────────────────────────────────────────────────────────
blood_group = st.selectbox(
    "Blood Group *",
    options=["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
    index=0,
)

city = st.text_input("City *", placeholder="e.g. Karachi")

name = st.text_input("Donor Name (optional)", placeholder="e.g. Ahmed")

search_clicked = st.button("🔍 Search", type="primary")

st.markdown("---")

# ── Results Placeholder ───────────────────────────────────────────────────────
if search_clicked:
    if not blood_group or not city:
        st.warning("Please select a blood group and enter a city.")
    else:
        st.info(
            f"Searching for **{blood_group}** donors in **{city}**"
            + (f" named **{name}**" if name else "")
            + "..."
        )
        st.markdown("#### Results")
        # 1. Call FastAPI
        response = requests.get("http://127.0.0.1:8000/donors/search",params = {"blood_group" : blood_group, "city" : city, "name" : name})
        # 2. Convert response to list
        donors = response.json()
        # 3. Loop and display donorselse:
        for donor in donors:
            st.write(donor["name"])
            st.write(donor["city"])
            st.write(donor["blood_group"])
            st.write(donor["phone"])
            st.markdown("---")