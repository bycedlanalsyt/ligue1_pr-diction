# ⚽ Sport Result Prediction - Ligue 1

Un projet de prédiction de résultats de matchs de football pour la Ligue 1 française, saison 2023/2024, utilisant l'apprentissage automatique.

## 📋 Description du Projet

Ce projet vise à prédire les résultats des matchs de football (victoire à domicile, match nul, ou victoire à l'extérieur) en utilisant des données historiques et des statistiques de matchs. Le modèle est entraîné sur les données de la Ligue 1 pour la saison 2023/2024 et utilise un algorithme de Random Forest.

## 🏗️ Structure du Projet

```
sport_result_prediction/
├── app/                    # Application Streamlit
│   ├── streamlit_app.py    # Interface principale
│   └── streamlit_app_test.py
├── data/                   # Données du projet
│   ├── raw/                # Données brutes
│   │   └── ligue1_2023_2024.csv
│   ├── processed/          # Données nettoyées
│   │   └── cleaned_data.csv
│   └── model.pkl           # Modèle entraîné
├── notebooks/              # Notebooks Jupyter pour l'exploration
│   └── 01_exploration.ipynb
├── src/                    # Code source Python
│   ├── data_preparation.py # Préparation des données
│   ├── train_model.py      # Entraînement du modèle
│   └── predict.py          # Prédictions
├── requirements.txt        # Dépendances Python
└── README.md              # Ce fichier
```

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt** (ou télécharger le projet)
   ```bash
   git clone <url-du-depot>
   cd sport_result_prediction
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Sur Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Utilisation

### 1. Préparation des données

Nettoyez et préparez les données à partir du fichier brut:

```bash
python src/data_preparation.py
```

Cette commande va:
- Charger les données brutes depuis `data/raw/ligue1_2023_2024.csv`
- Nettoyer les données (suppression des colonnes inutiles, gestion des valeurs manquantes)
- Encoder les résultats (H=1, D=0, A=-1)
- Sauvegarder les données nettoyées dans `data/processed/cleaned_data.csv`

### 2. Entraînement du modèle

Entraînez le modèle de Random Forest:

```bash
python src/train_model.py
```

Cette commande va:
- Charger les données nettoyées
- Séparer les données en ensembles d'entraînement et de test (80/20)
- Entraîner un modèle Random Forest avec 100 estimateurs
- Évaluer la précision du modèle
- Sauvegarder le modèle dans `data/model.pkl`

### 3. Faire des prédictions

Faire des prédictions sur de nouveaux matchs:

```bash
python src/predict.py
```

### 4. Interface Web (Streamlit)

Lancer l'application web interactive:

```bash
streamlit run app/streamlit_app.py
```

L'interface permet de:
- Sélectionner un match par son index
- Visualiser la prédiction (victoire domicile, nul, ou victoire extérieur)

## 📊 Technologies Utilisées

- **Python** - Langage de programmation principal
- **Pandas** - Manipulation et analyse de données
- **Scikit-learn** - Machine Learning (Random Forest)
- **Joblib** - Sauvegarde et chargement de modèles
- **Streamlit** - Interface web interactive

## 📦 Dépendances Principales

Les dépendances du projet sont listées dans `requirements.txt`:
- pandas
- scikit-learn
- joblib
- streamlit

## 🎯 Fonctionnalités

- ✅ Prédiction de résultats de matchs (victoire domicile, nul, victoire extérieur)
- ✅ Interface web interactive avec Streamlit
- ✅ Modèle de Random Forest entraîné sur les données de la Ligue 1
- ✅ Pipeline de préparation des données
- ✅ Évaluation de la performance du modèle

## 📝 Notes

- Le modèle est entraîné sur les données de la saison 2023/2024 de la Ligue 1
- Les données sont encodées numériquement pour l'entraînement
- Le modèle utilise un Random Forest avec 100 estimateurs

## 🔧 Configuration

Les chemins des fichiers de données et du modèle sont configurables dans les scripts Python. Les chemins actuels pointent vers:
- Données brutes: `data/raw/ligue1_2023_2024.csv`
- Données nettoyées: `data/processed/cleaned_data.csv`
- Modèle: `data/model.pkl`

## 👤 Cédric BOIMIN

Projet développé dans le cadre de l'apprentissage du Machine Learning appliqué au sport.

## 📄 Licence

Ce projet est fourni à des fins éducatives et d'apprentissage.

