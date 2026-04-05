import streamlit as st
import requests
from components.styles import apply_styles
apply_styles()

st.set_page_config(page_title="Become a Donor", page_icon="❤️")

st.title("❤️ Become a Donor")
st.write("Fill in your details below to register as a blood donor.")
st.markdown("---")

# ── Donor Registration Form ───────────────────────────────────────────────────
with st.form("donor_form"):
    name = st.text_input("Full Name *", placeholder="e.g. Ravi Kumar")

    blood_group = st.selectbox(
        "Blood Group *",
        options=["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        index=0,
    )

    phone = st.text_input("Phone Number *", placeholder="e.g. 0300-1234567")

    city = st.text_input("City *", placeholder="e.g. Hyderabad")

    last_donation = st.date_input(
        "Last Donation Date",
        value=None,
        help="Leave blank if you've never donated before.",
    )

    available = st.checkbox("I am currently available to donate")

    submitted = st.form_submit_button("✅ Submit", type="primary")

# ── Post-Submit Feedback ──────────────────────────────────────────────────────
if submitted:
    if not name or not blood_group or not phone or not city:
        st.error("Please fill in all required fields (marked with *).")
    else:
        ##API call here:
        response = requests.post("http://127.0.0.1:8000/donors/register",json = {"blood_group" : blood_group, 
                                                                                 "city" : city, "name" : name,
                                                                                 "phone" : phone,
                                                                                 "last_donation_date" : str(last_donation) if last_donation else None,
                                                                                    "is_available" : available })
        ##If we want to check the status of the code:
            ##st.write(response.status_code)
            ##st.write(response.json())
        st.success(
            f"Thank you, **{name}**! Your registration has been received. "
            "We'll reach out when someone nearby needs your blood type."
        )
        st.balloons()
        st.caption("Your details has been saved successfully")
'''
The API call should go in the `else` block — because that's where you know all fields are filled correctly.
And that `st.caption` line is literally telling you what's missing 😄

Just like `Find_Blood.py.py` needed a new FastAPI route `GET /donors/search`, this page needs a new route too:
POST /donors/register
'''
from components.emergency_footer import emergency_footer
emergency_footer()
