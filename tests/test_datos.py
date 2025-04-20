from src.datos import cargar_ahorros

def test_cargar_ahorros():
    df = cargar_ahorros()
    assert not df.empty
    assert "mes" in df.columns and "ahorro" in df.columns
