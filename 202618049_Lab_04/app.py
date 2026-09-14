# ============================================================
# STAYPREDICT AI
# Airbnb Price Prediction Application
# DS605 - Fundamentals of Machine Learning
# ============================================================

import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StayPredict AI",
    page_icon="🏠",
    layout="wide"
)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():
    model_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "airbnb_price_pipeline.pkl"
    )
    return joblib.load(model_path)

model = load_model()


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🏠 StayPredict AI")

st.subheader("Smart Airbnb Price Prediction")

st.write(
    "Enter the Airbnb listing details below to estimate "
    "the nightly rental price."
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

st.header("🏡 Airbnb Listing Information")


# ------------------------------------------------------------
# LOCATION
# ------------------------------------------------------------

st.subheader("📍 Location")

col1, col2 = st.columns(2)

with col1:

    neighbourhood_group = st.selectbox(
        "Neighbourhood Group",
        [
            "Brooklyn",
            "Manhattan",
            "Queens",
            "Bronx",
            "Staten Island"
        ]
    )

    neighbourhood = st.text_input(
        "Neighbourhood",
        value="Williamsburg"
    )


with col2:

    latitude = st.number_input(
        "Latitude",
        value=40.7180,
        format="%.4f"
    )

    longitude = st.number_input(
        "Longitude",
        value=-73.9500,
        format="%.4f"
    )


st.divider()


# ------------------------------------------------------------
# ROOM AND STAY INFORMATION
# ------------------------------------------------------------

st.subheader("🛏️ Stay Information")

col3, col4 = st.columns(2)

with col3:

    room_type = st.selectbox(
        "Room Type",
        [
            "Entire home/apt",
            "Private room",
            "Shared room"
        ]
    )

    minimum_nights = st.number_input(
        "Minimum Nights",
        min_value=1,
        max_value=365,
        value=2,
        step=1
    )


with col4:

    availability_365 = st.number_input(
        "Availability per Year",
        min_value=0,
        max_value=365,
        value=200,
        step=1
    )


st.divider()


# ------------------------------------------------------------
# GUEST ACTIVITY
# ------------------------------------------------------------

st.subheader("⭐ Guest Activity")

col5, col6 = st.columns(2)

with col5:

    number_of_reviews = st.number_input(
        "Number of Reviews",
        min_value=0,
        value=10,
        step=1
    )


with col6:

    reviews_per_month = st.number_input(
        "Reviews per Month",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.2f"
    )


st.divider()


# ------------------------------------------------------------
# HOST INFORMATION
# ------------------------------------------------------------

st.subheader("👤 Host Information")

calculated_host_listings_count = st.number_input(
    "Host Listings Count",
    min_value=1,
    value=1,
    step=1
)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

host_activity = (
    calculated_host_listings_count
    + number_of_reviews
)


st.info(
    f"📈 Host Activity Score: {host_activity}"
)


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({

    "neighbourhood_group": [
        neighbourhood_group
    ],

    "neighbourhood": [
        neighbourhood
    ],

    "latitude": [
        latitude
    ],

    "longitude": [
        longitude
    ],

    "room_type": [
        room_type
    ],

    "minimum_nights": [
        minimum_nights
    ],

    "number_of_reviews": [
        number_of_reviews
    ],

    "reviews_per_month": [
        reviews_per_month
    ],

    "calculated_host_listings_count": [
        calculated_host_listings_count
    ],

    "availability_365": [
        availability_365
    ],

    "host_activity": [
        host_activity
    ]
})


# ============================================================
# PREDICTION
# ============================================================

st.divider()

st.header("💰 Price Prediction")

st.write(
    "Click the button below to generate the estimated "
    "nightly Airbnb price."
)


if st.button(
    "✨ Generate Price Estimate",
    use_container_width=True
):

    prediction = model.predict(input_data)[0]

    prediction = max(0, prediction)

    st.success(
        "Prediction generated successfully!"
    )

    st.metric(
        "🏠 Estimated Nightly Price",
        f"${prediction:,.2f}"
    )

    st.caption(
        "The predicted value is an estimated nightly price "
        "generated by the trained Random Forest model."
    )


# ============================================================
# ABOUT THE APPLICATION
# ============================================================

st.divider()

with st.expander("🔎 About StayPredict AI"):

    st.write(
        "StayPredict AI is a machine learning application "
        "developed for predicting Airbnb nightly prices."
    )

    st.write(
        "The application uses a tuned Random Forest "
        "regression model trained on NYC Airbnb listing data."
    )

    st.write(
        "The model uses location, room type, stay information, "
        "guest activity, availability and host activity "
        "as input features."
    )

    st.write(
        "Final Test R² Score: 0.577"
    )

    st.write(
        "Final MAE: $31.67"
    )

    st.write(
        "Final RMSE: $43.75"
    )


