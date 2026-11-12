from pathlib import Path
import pandas as pd


def load_raw():
    #Charge les données brutes de scoring de crédit.

    file_path = Path("data/raw/cs-training.csv")

    if not file_path.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {file_path}"
        )

    df = pd.read_csv(file_path)

    # Suppression de la colonne d'index sans nom
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    return df