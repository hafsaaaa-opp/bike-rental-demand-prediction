import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("bike_demand_model.pkl")

# Page settings
st.set_page_config(
    page_title="Bike Rental Demand Predictor",
    page_icon="🚲",
    layout="centered"
)

# Title
st.title("🚲 Bike Rental Demand Predictor")
st.write("Predict bike rental demand using weather and time conditions.")

st.divider()

# Input section
st.subheader("📋 Enter Conditions")

season = st.selectbox(
    "Season",
    ["Spring", "Summer", "Fall", "Winter"]
)

month = st.slider("Month", 1, 12, 6)
day = st.slider("Day", 1, 31, 15)
hour = st.slider("Hour", 0, 23, 10)

weather = st.selectbox(
    "Weather",
    [
        "Clear / Few Clouds",
        "Mist / Cloudy",
        "Light Rain / Snow",
        "Heavy Rain / Snow"
    ]
)

temperature = st.slider(
    "Temperature",
    0.0, 1.0, 0.50, 0.01
)

humidity = st.slider(
    "Humidity",
    0.0, 1.0, 0.50, 0.01
)

windspeed = st.slider(
    "Wind Speed",
    0.0, 1.0, 0.20, 0.01
)

workingday = st.selectbox(
    "Working Day",
    ["Yes", "No"]
)

# Convert inputs to model values
season_value = {
    "Spring": 1,
    "Summer": 2,
    "Fall": 3,
    "Winter": 4
}[season]

weather_value = {
    "Clear / Few Clouds": 1,
    "Mist / Cloudy": 2,
    "Light Rain / Snow": 3,
    "Heavy Rain / Snow": 4
}[weather]

workingday_value = 1 if workingday == "Yes" else 0

# Prediction button
if st.button("🚲 Predict Bike Demand", use_container_width=True):

    input_data = pd.DataFrame({
        "season": [season_value],
        "yr": [1],
        "mnth": [month],
        "hr": [hour],
        "holiday": [0],
        "weekday": [2],
        "workingday": [workingday_value],
        "weathersit": [weather_value],
        "temp": [temperature],
        "atemp": [temperature],
        "hum": [humidity],
        "windspeed": [windspeed],
        "day": [day]
    })

    prediction = model.predict(input_data)[0]
    predicted_bikes = max(0, round(prediction))

    st.success("Prediction Generated Successfully!")
    st.metric(
        label="🚲 Predicted Bike Demand",
        value=f"{predicted_bikes} Bikes"
    )
