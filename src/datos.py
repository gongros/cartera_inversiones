import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "ahorros.csv"

def cargar_ahorros():
    return pd.read_csv(DATA_PATH)
