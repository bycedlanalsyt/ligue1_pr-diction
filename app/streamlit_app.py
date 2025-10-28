import streamlit as st
import pandas as pd
import joblib

# --- Titre ---
st.title("⚽ Prédiction de Résultats Ligue 1 - Saison 2023/2024")

# --- Charger le modèle ---
model_path = r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\model.pkl"
data_path = r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\cleaned_data.csv"

model = joblib.load(model_path)
df = pd.read_csv(data_path)
df = df.select_dtypes(include=['number'])

# --- Interface utilisateur ---
st.subheader("🔍 Faire une prédiction sur un match existant")

match_index = st.number_input("Choisis un numéro de match (0 à 305)", min_value=0, max_value=305, value=0)

# --- Prédiction ---
X = df.drop(columns=['result'], errors='ignore')
sample = X.iloc[[match_index]]
prediction = model.predict(sample)[0]

# --- Afficher le résultat ---
if prediction == 1:
    st.success("🏠 Victoire de l'équipe à domicile")
elif prediction == 0:
    st.info("🤝 Match nul")
else:
    st.error("🚀 Victoire de l'équipe à l'extérieur")

st.write("✅ Modèle de prédiction prêt !")
