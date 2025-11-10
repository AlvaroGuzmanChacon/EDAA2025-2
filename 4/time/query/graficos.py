import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Segment Tree": "#4287f5", "Sparse Table": "#f74525"}

def plot(data):
    # Análisis Peor caso
    ax = sns.lineplot(data=data, x="n", y="t_mean", hue = "structure", palette=palette, marker="*")
    ax.set_xlabel("Tamaño de la estructura (n)")
    ax.set_ylabel("Tiempo promedio de consulta RMQ (milisegundos)")
    plt.savefig("time_query.png", bbox_inches='tight')


if __name__ == "__main__":
    df_1 = pd.read_csv("segment_tree.csv", usecols=["n", "t_mean", "structure"])
    df_2 = pd.read_csv("sparse_table.csv", usecols=["n", "t_mean", "structure"])
    data = pd.concat([df_1, df_2])
    plot(data)
