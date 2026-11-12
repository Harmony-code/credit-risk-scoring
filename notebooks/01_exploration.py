import pandas as pd
from pathlib import Path
file_path = Path("data/raw/cs-training.csv")
df=pd.read_csv(file_path)
print("donées chargées avec succès")
