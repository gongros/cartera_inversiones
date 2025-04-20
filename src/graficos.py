import matplotlib.pyplot as plt

def graficar_ahorros(df):
    plt.figure(figsize=(8, 5))
    plt.plot(df["mes"], df["ahorro"], marker='o')
    plt.title("Ahorro mensual en dólares")
    plt.xlabel("Mes")
    plt.ylabel("Ahorro (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
