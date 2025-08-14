import streamlit as st
import joblib
import pandas as pd

# Load the trained model pipeline (includes preprocessing)
model = joblib.load("best_fit_model (2).pkl")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ Overview", "📊 Prediction"])

# ========
# HOME PAGE
# ========
if page == "🏠 Home":
    st.markdown(
        "<h1 style='color: #4CAF50; text-align: center;'>📱 Products Discount Data Analysis & Estimation</h1>",
        unsafe_allow_html=True
    )
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTfyBEp1ZKKov4PnnRkdkeXIVtsB6nf9H-6g&s",
        use_container_width=True
    )
    st.markdown("""
    ## Welcome to the Smartphone Discount Prediction
    This app helps you *predict the discount price* of smartphones
    based on their brand, RAM, storage, display size, battery, and camera details.

*💡 Why use this app?*
- 📊 Helps *e-commerce sellers* plan competitive discounts to attract more customers.
- 🛒 Assists *buyers* in estimating the best deal before making a purchase.
- 📈 Useful for *market analysis* and tracking *price trends* over time.
- 🧠 Supports *data-driven decision making* for better pricing strategies.
- ⏳ Saves *time* by predicting prices instantly without manual calculations.
- 🎯 Helps target *specific customer segments* with personalized discounts.
- 📦 Useful for *inventory clearance planning* by setting optimal discount rates.
- 🔍 Provides *insights into brand-wise pricing patterns* in the market.

Navigate to the *Prediction* tab from the sidebar to try it yourself!
    """)

# ========
# OVERVIEW PAGE
# ========
elif page == "ℹ️ Overview":
    st.title("📖 Project Overview")
    st.markdown("""
    ### 📌 Objective
    Predict the *Discount Price* of smartphones using machine learning.

    ### 📊 Dataset
    The model was trained on data scraped from:
    - *Amazon* 📦
    - *Flipkart* 🛒

    ### 📐 Features Used
    - *Brand* 🏷️
    - *RAM* (GB) 💾
    - *ROM* (GB) 📂
    - *Display Size* (inches) 📱
    - *Battery* (mAh) 🔋
    - *Front Camera (MP)* 🤳
    - *Back Camera (MP)* 📷

    ### ⚙️ How It Works
    1. Enter smartphone specifications.
    2. The app processes the input through the trained pipeline.
    3. The model predicts the *discount price*.

    ### 📈 Use Cases
    - Price strategy planning for e-commerce platforms.
    - Budget estimation for buyers.
    - Competitive market analysis.
    """)

# ========
# 📊 PREDICTION PAGE
# ==================
elif page == "📊 Prediction":
    st.title("📊 Predict Smartphone Discount Price")
    input_features = {}

    # Brand dropdown
    brands = ['Samsung', 'Apple', 'Redmi', 'OnePlus', 'Realme', 'Vivo', 'Oppo', 'Motorola', 'Poco', 'Others']
    input_features['Brand'] = st.selectbox("Select Brand", brands)

    # Predefined spec options
    ram_options = [4, 6, 8, 12, 16]
    rom_options = [64, 128, 256, 512, 1024]
    display_options = [5.5, 6.5, 6.7, 6.8, 7.0]
    battery_options = [4000, 5000, 5600, 6000, 6600]
    front_cam_options = [8, 12, 16, 32]
    back_cam_options = [50, 64, 108, 200]

    # Dropdowns for each spec
    input_features['RAM'] = st.selectbox("Select RAM (GB)", ram_options)
    input_features['ROM'] = st.selectbox("Select Storage (GB)", rom_options)
    input_features['Display_Size'] = st.selectbox("Select Display Size (inches)", display_options)
    input_features['Battery'] = st.selectbox("Select Battery Capacity (mAh)", battery_options)
    input_features['Front_Cam(MP)'] = st.selectbox("Select Front Camera (MP)", front_cam_options)
    input_features['Back_Cam(MP)'] = st.selectbox("Select Back Camera (MP)", back_cam_options)

    # Predict Button
    if st.button("🚀 Predict Discount Price"):
        df = pd.DataFrame([input_features])
        # Since preprocessing is inside the pipeline, we can directly pass df
        prediction = model.predict(df)[0]
        st.success(f"💰 Predicted Discount Price: ₹{prediction:,.2f}")
        st.balloons()
