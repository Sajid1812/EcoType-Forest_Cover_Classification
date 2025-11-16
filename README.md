# 🌲 Forest Cover Type Prediction - Machine Learning Web App

This repository contains a **Streamlit-based web application** that predicts the **forest cover type** using a trained **Random Forest Machine Learning model**. Users can input environmental and geographical parameters, and the model returns the most probable forest cover classification.

---

## 📌 Key Features

- 🧠 Uses pre-trained Random Forest Model  
- ⚙️ Encoded output using Label Encoder  
- 🎛 Interactive Streamlit UI with input validation  
- 📊 Uses top 10 important features from dataset  
- 🚀 Fast and real-time prediction  

---

## 🧠 Technologies Used

| Component        | Technology |
|------------------|------------|
| Language         | Python     |
| Framework        | Streamlit  |
| ML Model         | Random Forest |
| Preprocessing    | PowerTransformer, StandardScaler, LabelEncoder |
| Libraries        | pandas, numpy, pickle |

---

## 📁 Project Structure


---

## 🧩 Input Features

| Feature Name                         | Value Format / Transformation  |
|-------------------------------------|--------------------------------|
| Elevation                           | Standardized (numeric)         |
| Horizontal_Distance_To_Roadways     | Standardized (numeric)         |
| Horizontal_Distance_To_Fire_Points  | Standardized (numeric)         |
| Horizontal_Distance_To_Hydrology    | log1p transformed              |
| Vertical_Distance_To_Hydrology      | Yeo–Johnson transformed        |
| Hillshade_9am                       | Yeo–Johnson transformed        |
| Hillshade_3pm                       | Standardized (numeric)         |
| Aspect                              | log1p transformed              |
| Wilderness_Area_1                   | 0 / 1 (binary)                 |
| Wilderness_Area_4                   | 0 / 1 (binary)                 |

⚠️ **Note:** Ensure inputs follow preprocessing used in model training.

---

## 🚀 How to Run the App

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

streamlit run app.py
