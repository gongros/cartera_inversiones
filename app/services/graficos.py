import matplotlib.pyplot as plt

def graficar_ahorros(df, show=True):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df["mes"], df["ahorro"], marker='o')
    ax.set_title("Ahorro mensual en dólares")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Ahorro (USD)")
    ax.grid(True)
    plt.tight_layout()
    if show:
        plt.show()
    return fig
