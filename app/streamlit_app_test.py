import streamlit as st
import pandas as pd
import joblib
from datetime import datetime  # à ajouter

# --- Configuration de la page ---
st.set_page_config(page_title="Prédiction Ligue 1", page_icon="⚽", layout="wide")

# --- En-tête avec logo ---
col1, col2 = st.columns([1, 6])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/fr/7/76/Ligue1_Uber_Eats_logo.png", width=90)
with col2:
    st.title("⚽ Prédiction de Résultats Ligue 1 – Saison 2023/2024")

st.markdown("<hr style='border:1px solid #ccc;margin:10px 0;'>", unsafe_allow_html=True)
st.markdown("### 🔍 Sélectionne un match et découvre la prédiction du modèle")

# --- Chemins des fichiers ---
model_path = r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\model.pkl"
data_path = r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\ligue1_2023_2024.csv"
cleaned_path = r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\cleaned_data.csv"

# --- Charger les fichiers ---
raw_df = pd.read_csv(data_path)
model_df = pd.read_csv(cleaned_path)
model_df = model_df.select_dtypes(include=['number'])
model = joblib.load(model_path)

# --- Créer une liste lisible de matchs ---
raw_df['match_label'] = (
    raw_df['home_team'] + " vs " + raw_df['away_team'] +
    " (" + raw_df['date'].astype(str) + ")"
)
match_list = raw_df['match_label'].tolist()

# --- Interface de sélection ---
st.markdown("### 🎯 Choisis ton match")

with st.container():
    selected_match = st.selectbox("Match à prédire :", match_list)
    st.write(f"📅 Date : {raw_df.loc[raw_df['match_label'] == selected_match, 'date'].values[0]}")
    if st.button("🔮 Lancer la prédiction"):
        # Trouver l’index du match sélectionné
        match_index = raw_df[raw_df['match_label'] == selected_match].index[0]

        # Sélectionner la ligne correspondante dans le jeu nettoyé
        X = model_df.drop(columns=['result'], errors='ignore')
        sample = X.iloc[[match_index]]

        # Faire la prédiction
        prediction = model.predict(sample)[0]

        # --- Résultat ---
        st.subheader("Résultat prédit :")
        if prediction == 1:
            st.success("🏠 Victoire de l'équipe **à domicile**")
        elif prediction == 0:
            st.info("🤝 **Match nul**")
        else:
            st.error("🚀 Victoire de l'équipe **à l'extérieur**")

        # --- Détails du match ---
        st.markdown("### 📊 Détails du match sélectionné :")
        c1, c2, c3 = st.columns(3)
        c1.metric("🏠 Équipe domicile", raw_df.loc[match_index, "home_team"])
        c2.metric("🚀 Équipe extérieure", raw_df.loc[match_index, "away_team"])
        c3.metric("📅 Date", raw_df.loc[match_index, "date"])

    # --- Afficher le résultat ---
    st.subheader("Résultat prédit :")
    if prediction == 1:
        st.success("🏠 Victoire de l'équipe **à domicile**")
    elif prediction == 0:
        st.info("🤝 **Match nul**")
    else:
        st.error("🚀 Victoire de l'équipe **à l'extérieur**")

    # --- Tableau récapitulatif ---
    st.markdown("### 📊 Détails du match sélectionné :")
    st.dataframe(
        raw_df.loc[[match_index], ['date', 'home_team', 'away_team', 'home_goals', 'away_goals', 'result']]
    )

st.markdown("---")
st.markdown("""
    <style>
    body {background-color:#f7f9fc;}
    .stButton>button {
        background-color:#2d7dd2;
        color:white;
        border-radius:10px;
        height:3em;
        width:100%;
        font-weight:bold;
    }
    .stButton>button:hover {
        background-color:#1b4f91;
        color:white;
    }
    </style>
""", unsafe_allow_html=True)
st.caption("Créé avec ❤️ par Cédric Boimin | Projet Machine Learning - Ligue 1 2023/2024")
