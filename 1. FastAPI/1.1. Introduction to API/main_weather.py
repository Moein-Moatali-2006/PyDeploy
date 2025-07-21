import streamlit as st
import requests

st.set_page_config(page_title="Weather App")

st.markdown("""
    <style>
        .main {
            background-color: #eef;
        }
        .stApp {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌤️ Weather Forecast")

city = st.text_input("Enter city name...")

if st.button("Get Weather") and city:
    url = f"https://goweather.herokuapp.com/weather/{city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("temperature"):
            st.markdown(f" 📍 {city.capitalize()}")
            st.write(f"**Today:** {data['description']} / {data['temperature']}")
            st.markdown("---")
            st.markdown("#### Next 3 Days:")
            for i, day in enumerate(data['forecast'], 1):
                st.write(f"- Day {i}: {day['temperature']} / {day['wind']}")
        else:
            st.error("❌ City not found.")
    else:
        st.error("⚠️ Failed to fetch data. Try again.")
