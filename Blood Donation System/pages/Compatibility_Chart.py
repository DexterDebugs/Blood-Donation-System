import streamlit as st
import pandas as pd
from components.styles import apply_styles
apply_styles()

st.set_page_config(page_title="Compatibility Chart", page_icon="📊")

st.title("📊 Blood Type Compatibility")
st.write("Who can donate to whom? Use this chart as a quick reference.")
st.markdown("---")

# ── Compatibility Table ───────────────────────────────────────────────────────
compatibility = {
    "Blood Type": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
    "Can Donate To": [
        "A+, AB+",
        "A+, A-, AB+, AB-",
        "B+, AB+",
        "B+, B-, AB+, AB-",
        "AB+ only",
        "AB+, AB-",
        "A+, B+, AB+, O+",
        "Everyone (Universal Donor)",
    ],
    "Can Receive From": [
        "A+, A-, O+, O-",
        "A-, O-",
        "B+, B-, O+, O-",
        "B-, O-",
        "Everyone (Universal Receiver)",
        "AB-, A-, B-, O-",
        "O+, O-",
        "O- only",
    ],
}

df = pd.DataFrame(compatibility)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")

# ── Bar Chart: Donor Frequency (Dummy) ───────────────────────────────────────
st.subheader("🧪 Donor Distribution by Blood Type")
st.caption("Placeholder data — replace with real database counts later.")

chart_data = pd.DataFrame(
    {
        "Blood Type": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        "Number of Donors": [320, 80, 280, 60, 95, 30, 410, 140],
    }
).set_index("Blood Type")

st.bar_chart(chart_data)

st.markdown("---")

# ── Quick Tip ─────────────────────────────────────────────────────────────────
st.info(
    "💡 **O-** is the universal donor — their blood can be given to anyone in an emergency. "
    "**AB+** is the universal receiver — they can accept blood from any type."
)

from components.emergency_footer import emergency_footer
emergency_footer()
