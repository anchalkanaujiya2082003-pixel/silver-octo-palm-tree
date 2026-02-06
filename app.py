import streamlit as st
st.set_page_config(
    page_title="Beauty Product Recommender",
    page_icon="🧴"
)
with st.sidebar:
    st.markdown("## 💖 Skin Care Recommender")
    st.write("Personalized skincare suggestions just for you ✨")

    st.markdown("---")

    skin_type = st.selectbox(
        "🌿 Select Skin Type",
        ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
    )

    concern = st.multiselect(
        "✨ Skin Concerns",
        ["Acne", "Pigmentation", "Dark Spots", "Wrinkles", "Dull Skin"]
    )

    budget = st.radio(
        "💰 Budget Range",
        ["Low", "Medium", "High"]
    )

    recommend_btn = st.button("💄 Get Recommendations")

    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")

import streamlit as st

# Page config
st.set_page_config(
    page_title="Skin Care Product Recommender",
    page_icon="🧴",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(to right, #ffe4e1, #fff0f5);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title */
    h1 {
        color: #d6336c;
        text-align: center;
        font-weight: bold;
    }

    /* Subheaders */
    h2, h3 {
        color: #b5179e;
    }

    /* Input labels */
    label {
        color: #6a0572;
        font-weight: 600;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #ff1493;
        color: white;
    }

    /* Selectbox & text inputs */
    .stSelectbox, .stTextInput, .stNumberInput {
        background-color: #ffffff;
        border-radius: 10px;
    }

    /* Recommendation card */
    .recommend-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import joblib

# Load model & encoders
model = joblib.load("beauty_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.set_page_config(page_title="Beauty Product Recommender", layout="centered")

st.title("🧴 Skin Care Product Recommender")
st.write("✨ Find the best skincare products based on your skin type and concerns ✨")


# User Inputs
age = st.slider("Age", 18, 45, 22)
gender = st.selectbox("Gender", ["Female", "Male"])
skin_tone = st.selectbox("Skin Tone", ["Fair", "Medium", "Dark"])
skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination", "Normal"])
skin_problem = st.selectbox(
    "Skin Problem", ["Acne", "Pigmentation", "Dryness", "Wrinkles", "Dullness", "None"]
)
sensitivity = st.selectbox("Sensitive Skin?", ["Yes", "No"])
climate = st.selectbox("Climate", ["Humid", "Dry", "Cold", "Moderate", "Hot"])
product_type = st.selectbox(
    "Preferred Product Type", ["Face Wash", "Moisturizer", "Serum", "Face Cream"]
)
brand = st.selectbox(
    "Preferred Brand",
    ["Lakme", "Plum", "Minimalist", "Cetaphil", "Neutrogena", "Nivea", "The Ordinary"]
)
ingredients_type = st.selectbox("Ingredients Type", ["Natural", "Chemical"])
price_range = st.selectbox("Price Range", ["Budget", "Mid", "Premium"])

# Predict button
if st.button("Recommend Product"):
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "skin_tone": skin_tone,
        "skin_type": skin_type,
        "skin_problem": skin_problem,
        "sensitivity": sensitivity,
        "climate": climate,
        "product_type": product_type,
        "brand": brand,
        "ingredients_type": ingredients_type,
        "price_range": price_range
    }])

    # Encode input
    for col, encoder in label_encoders.items():
        if col != "recommended_product":
            input_data[col] = encoder.transform(input_data[col])

    prediction = model.predict(input_data)
    product = label_encoders["recommended_product"].inverse_transform(prediction)

    st.success(f"✨ Recommended Product: **{product[0]}**")

    
