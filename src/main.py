from datos import cargar_ahorros
from graficos import graficar_ahorros

def main():
    df = cargar_ahorros()
    graficar_ahorros(df)

if __name__ == "__main__":
    main()
