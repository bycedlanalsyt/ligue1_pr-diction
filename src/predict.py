import pandas as pd
import joblib

def predict_new_match(data_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\cleaned_data.csv",
                      model_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\model.pkl"):
    # Charger le modèle
    model = joblib.load(model_path)

    # Charger quelques lignes de données (par exemple les 5 premières)
    df = pd.read_csv(data_path)

    # Ne garder que les colonnes numériques
    df = df.select_dtypes(include=['number'])

    # On garde la même structure que pour l'entraînement
    X = df.drop(columns=['result'], errors='ignore')

    # Faire une prédiction sur les 5 premiers matchs
    sample = X.head(5)
    preds = model.predict(sample)

    print("🔮 Prédictions (1 = victoire domicile, 0 = nul, -1 = victoire extérieur) :")
    print(preds)

if __name__ == "__main__":
    predict_new_match()
