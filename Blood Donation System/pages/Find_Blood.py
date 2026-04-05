import streamlit as st
import requests
import pandas as pd
import random
from geopy.geocoders import Nominatim  # Nominatim → the tool that converts city names to coordinates
from components.styles import apply_styles
from components.donor_card import donor_card

st.set_page_config(page_title="Find Blood", page_icon="🔍")

apply_styles()

# -------------------- Maps Coordinates - Helper Functions ----------------------------------------
def get_coordinates(city):  # give it a city name, it gives back coordinates
    geolocator = Nominatim(user_agent="bloodconnect")
    # user_agent is just your app's name — Nominatim requires it to identify who's making requests.
    location = geolocator.geocode(city)
    # This sends "Hyderabad" to Nominatim and gets back coordinates — like typing a city into Google Maps search.
    if location:
        return location.latitude, location.longitude
    return None, None
    # If city was found → return lat/long. If not found → return None so app doesn't crash.


st.title("🔍 Find Blood")
st.write("Search for available donors near you.")
st.markdown("---")

# ── Search Form ──────────────────────────────────────────────────────────────
blood_group_options = ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
blood_group = st.selectbox(
    "Blood Group *",
    options=blood_group_options,
    index=0,
    format_func=lambda x: "Select blood group..." if x == "" else x
)

city = st.text_input("City *", placeholder="e.g. Warangal")
name = st.text_input("Donor Name (optional)", placeholder="e.g. Chandra Varma")
search_clicked = st.button("🔍 Search", type="primary")

st.markdown("---")

# ── Results ──────────────────────────────────────────────────────────────────
if search_clicked:
    if not blood_group or not city:
        st.warning("Please select a blood group and enter a city.")
    else:
        st.info(f"Searching for **{blood_group}** donors in **{city}**" + (f" named **{name}**" if name else "") + "...")
        st.markdown("#### Results")
        response = requests.get("http://127.0.0.1:8000/donors/search", params={"blood_group": blood_group, "city": city, "name": name})
        donors = response.json()
        if len(donors) == 0:
            st.warning("No donors found. Try different filters.")
        else:
            #1. Build map data
            map_data = []       # if donors found, find their coordinates 
            city_coords = {}
            for donor in donors:
                city = donor["city"]
                if city not in city_coords:
                    lat, lon = get_coordinates(city)
                    city_coords[city] = (lat, lon)
                else:
                    lat, lon = city_coords[city]
                lat, lon = get_coordinates(donor["city"])
                # After getting coordinates, add small random offset
                if lat:
                    lat += random.uniform(-0.01, 0.01)
                    lon += random.uniform(-0.01, 0.01)
                    map_data.append({"lat": lat, "lon": lon})
            #2. Show map
            df = pd.DataFrame(map_data)
            st.map(df,zoom=11)
            #3 Show donor Cards
            for donor in donors:
                donor_card(donor)   # get coordinates and append to map_data

# -------Footer ---------------------------------------------------------------
from components.emergency_footer import emergency_footer

emergency_footer()

##**Rule to remember:**

##imports → set_page_config → apply_styles → rest of code