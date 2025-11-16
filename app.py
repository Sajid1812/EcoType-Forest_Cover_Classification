import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import PowerTransformer, StandardScaler

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="Forest Cover Type Prediction",
    layout="centered",
    page_icon="🌲"
)

# ==========================
# Load Model & Encoder
# ==========================
with open('best_random_forest_model22.pkl', 'rb') as f:
    model = pickle.load(f)

with open('new_label_encoder22.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# ==========================
# Feature List Used for Training
# ==========================
top_features = [
    'Elevation',
    'Horizontal_Distance_To_Roadways',
    'Horizontal_Distance_To_Fire_Points',
    'Horizontal_Distance_To_Hydrology',
    'Wilderness_Area_1',
    'Vertical_Distance_To_Hydrology',
    'Hillshade_9am',
    'Wilderness_Area_4',
    'Aspect',
    'Hillshade_3pm'
]

# ==========================
# UI Styling
# ==========================
st.markdown("""
<style>
    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #0a5c36;
        text-align: center;
    }
    .sub-header {
        font-size: 18px;
        font-weight: 500;
        color: #333;
    }
    .footer {
        text-align:center;
        font-size:14px;
        color:gray;
        margin-top:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🌲 Forest Cover Type Prediction</p>', unsafe_allow_html=True)
st.write("Provide the required environmental and geographical values below to predict the forest cover category.")

st.sidebar.header("📌 Input Guide")
st.sidebar.info("""
- Some inputs require **transformed values**, keep consistent with training preprocessing.
- Wilderness features are binary (0 or 1).
""")

# ==========================
# Input Form
# ==========================
with st.form("input_form"):
    st.markdown('<p class="sub-header">📥 Enter Feature Values</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    input_data = {}

    for idx, feature in enumerate(top_features):
        with (col1 if idx % 2 == 0 else col2):
            
            # UI input rules based on feature type
            if feature in ['Elevation', 'Horizontal_Distance_To_Roadways', 'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points']:
                input_data[feature] = st.number_input(f"{feature} (Standardized)", value=0.0, step=0.1)

            elif feature in ['Aspect', 'Horizontal_Distance_To_Hydrology']:
                input_data[feature] = st.number_input(f"{feature} (log1p)", value=1.0, min_value=0.0, step=0.1)

            elif feature in ['Vertical_Distance_To_Hydrology', 'Hillshade_9am']:
                input_data[feature] = st.number_input(f"{feature} (Yeo-Johnson)", value=0.0, step=0.1)

            elif feature.startswith("Wilderness_Area"):
                input_data[feature] = st.radio(f"{feature} (0/1)", [0, 1], horizontal=True)

            else:
                input_data[feature] = st.number_input(feature, value=0.0)
    
    submit_btn = st.form_submit_button("🔍 Predict")

# ==========================
# Prediction
# ==========================
if submit_btn:
    input_df = pd.DataFrame([input_data])
    input_df = input_df[top_features]

    prediction_encoded = model.predict(input_df)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)

    st.success(f"🌟 **Predicted Cover Type:** `{prediction_label[0]}`")

    st.balloons()

# ==========================
# Footer
# ==========================
st.markdown('<p class="footer">Developed with ❤️ using Streamlit</p>', unsafe_allow_html=True)
