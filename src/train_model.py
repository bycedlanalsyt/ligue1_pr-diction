import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(data_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\cleaned_data.csv",
                model_path=r"C:\Users\boimi\OneDrive\Documents\sport_result_prediction\data\model.pkl"):
    # Charger les données
    df = pd.read_csv(data_path)

    # Supprimer toutes les colonnes non numériques
    df = df.select_dtypes(include=['number'])

    # Vérifier que 'result' est bien dedans
    if 'result' not in df.columns:
        print("⚠️ La colonne 'result' a peut-être été supprimée. Vérifie ton fichier cleaned_data.csv")
        return

    # Séparer les features et la cible
    X = df.drop(columns=['result'])
    y = df['result']

    # Séparer en entraînement et test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Créer et entraîner le modèle
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Évaluer
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Précision du modèle : {accuracy:.2f}")

    # Sauvegarder
    joblib.dump(model, model_path)
    print(f"✅ Modèle enregistré dans : {model_path}")

if __name__ == "__main__":
    train_model()
