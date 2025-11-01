import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"binaria": "#4287f5", "secuencial": "#28bf28", "exponencial": "#f74525"}

def plot_size():
    df = pd.read_csv("results/res_size.csv", usecols=["n", "t_mean", "Búsqueda"])

    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Búsqueda", palette=palette, marker="*")
    ax.set_xlabel("Tamaño del arreglo")
    ax.set_ylabel("Tiempo (milisegundos)")
    plt.savefig("size_tiempo_full.png", bbox_inches='tight')
    plt.clf()

    df = df[df.Búsqueda != "secuencial"]

    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Búsqueda", marker="*", palette=palette)
    ax.set_xlabel("Tamaño del arreglo")
    ax.set_ylabel("Tiempo (milisegundos)")
    plt.savefig("size_tiempo_partial.png", bbox_inches='tight')
    plt.clf()

    df = pd.read_csv("results/res_size_B.csv", usecols=["n", "t_mean", "Búsqueda"])
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Búsqueda", marker="*", palette=palette)
    ax.set_xlabel("Tamaño del arreglo")
    ax.set_ylabel("Tiempo (milisegundos)")
    plt.savefig("size_tiempo_B.png", bbox_inches='tight')
    plt.clf()

def plot_position():
    df = pd.read_csv("results/res_pos.csv", usecols=["n", "t_mean", "t_stdev", "Búsqueda"])
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Búsqueda", marker="*", palette=palette)
    ax.set_xlabel("Posición del elemento")
    ax.set_ylabel("Tiempo (milisegundos)")
    plt.savefig("position_tiempo_full.png", bbox_inches='tight')
    plt.clf()

    df = df[df.Búsqueda != "secuencial"]

    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Búsqueda", marker="*", palette=palette)
    ax.set_xlabel("Posición del elemento")
    ax.set_ylabel("Tiempo (milisegundos)")
    plt.savefig("position_tiempo_partial.png", bbox_inches='tight')
    plt.clf()


if __name__ == "__main__":
    plot_size()
    plot_position()
