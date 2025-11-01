import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Binario": "#4287f5", "Binomial": "#28bf28", "Fibonacci": "#f74525"}

def plot_insert(data):
    # Análisis Peor caso
    df = data[data["Análisis"] == "Peor Caso"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Tamaño del Heap")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("insert_peor.png", bbox_inches='tight')
    plt.clf()

    df = df[df["Heap"] != "Binario"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Tamaño del Heap")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("insert_peor_parcial.png", bbox_inches='tight')
    plt.clf()

    df = data[data["Análisis"] == "Amortizado"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Cantidad de operaciones")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("insert_amortizado.png", bbox_inches='tight')
    plt.clf()

    df = df[df["Heap"] != "Binomial"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Cantidad de operaciones")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("insert_amortizado_parcial.png", bbox_inches='tight')
    plt.clf()

def plot_extractmin(data):
    # Análisis Peor caso
    df = data[data["Análisis"] == "Peor Caso"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Tamaño del Heap")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("pop_peor.png", bbox_inches='tight')
    plt.clf()

    df = df[df["Heap"] != "Fibonacci"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Tamaño del Heap")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("pop_peor_parcial.png", bbox_inches='tight')
    plt.clf()

    df = data[data["Análisis"] == "Amortizado"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Cantidad de operaciones")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("pop_amortizado.png", bbox_inches='tight')
    plt.clf()

    df = df[df["Heap"] != "Binomial"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "Heap", palette=palette, marker="*")
    ax.set_xlabel("Cantidad de operaciones")
    ax.set_ylabel("Tiempo promedio (milisegundos)")
    plt.savefig("pop_amortizado_parcial.png", bbox_inches='tight')
    plt.clf()


if __name__ == "__main__":
    df_1 = pd.read_csv("results/binary_insert.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    df_2 = pd.read_csv("results/binomial_insert.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    df_3 = pd.read_csv("results/fibonacci_insert.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    data = pd.concat([df_1, df_2, df_3])
    plot_insert(data)

    df_1 = pd.read_csv("results/binary_extractmin.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    df_2 = pd.read_csv("results/binomial_extractmin.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    df_3 = pd.read_csv("results/fibonacci_extractmin.csv", usecols=["n", "t_mean", "Heap", "Análisis"])
    data = pd.concat([df_1, df_2, df_3])
    plot_extractmin(data)
