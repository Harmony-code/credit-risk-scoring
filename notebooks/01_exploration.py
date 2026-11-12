import pandas as pd
from pathlib import Path

# Charger le jeu de données
file_path = Path("data/raw/cs-training.csv")
df=pd.read_csv(file_path)

#Supprimer la colonne 'Unnamed: 0' si elle existe
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]    
print("donées chargées avec succès")

print("Dimensions du jeu de données:", df.shape)
print("\nAperçu des premières lignes du jeu de données:")
print(df.head())

print("\nInformations sur le jeu de données:")
print(df.info())

print("Types de variables:")
print(df.dtypes)

# Calculer les statistiques descriptives pour les variables numériques moyennes, médianes, écart-types, minimums et maximums
print("\nStatistiques descriptives des variables numériques:")
print(df.describe())

# Vérifier les valeurs manquantes et les doublons
missing_values = df.isnull().sum()
print("\nNombre de valeurs manquantes par variable:")
print(missing_values)

# Calculer le pourcentage de valeurs manquantes par variable
print("\nPourcentage de valeurs manquantes par variable:")
missing_percentage = (missing_values / len(df)) * 100
print(missing_values / len(df) * 100)

# Vérifier les doublons
duplicate_rows = df.duplicated().sum()
print("\nNombre de lignes dupliquées dans le jeu de données:", duplicate_rows)

# Identifier la variable cible
target_variable = 'SeriousDlqin2yrs'
print("\nRépartition de la variable cible:")
print(df[target_variable].value_counts())
