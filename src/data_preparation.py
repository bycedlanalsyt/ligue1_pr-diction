import pandas as pd

def prepare_data(input_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\raw\ligue1_2023_2024.csv", 
                 output_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\processed\cleaned_data.csv"):
    # Charger le fichier
    df = pd.read_csv(input_path)

    # 1️⃣ Supprimer les colonnes inutiles (ex: trop de valeurs manquantes)
    df = df.dropna(thresh=len(df)*0.5, axis=1)

    # 2️⃣ Supprimer les colonnes non numériques inutiles pour l'entraînement
    columns_to_drop = ['Div', 'date', 'Time', 'home_team', 'away_team']
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # 3️⃣ Retirer les lignes où 'result' est manquant
    df = df.dropna(subset=['result'])

    # 4️⃣ Transformer la colonne 'result' en nombres (H=1, D=0, A=-1)
    df['result'] = df['result'].map({'H': 1, 'D': 0, 'A': -1})

    # 5️⃣ Remplacer les valeurs manquantes restantes par la moyenne
    df = df.fillna(df.mean(numeric_only=True))

    # 6️⃣ Sauvegarder les données nettoyées
    df.to_csv(output_path, index=False)
    print("✅ Données nettoyées et enregistrées dans :", output_path)

if __name__ == "__main__":
    prepare_data()