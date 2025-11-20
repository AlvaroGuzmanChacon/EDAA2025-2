import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Segment Tree": "#4287f5", "Sparse Table": "#f74525"}

def plot(data):
    # Análisis Peor caso
    ax = sns.lineplot(data=data, x="n", y="t_mean", hue = "Estructura", palette=palette, marker="*")
    ax.set_xlabel("Ancho del intervalo para la consulta")
    ax.set_ylabel("Tiempo promedio de consulta RMQ (milisegundos)")
    plt.savefig("4_time_query.png", bbox_inches='tight')


if __name__ == "__main__":
    df_1 = pd.read_csv("time_query_segment_tree.csv", usecols=["n", "t_mean", "Estructura"])
    df_2 = pd.read_csv("time_query_sparse_table.csv", usecols=["n", "t_mean", "Estructura"])
    data = pd.concat([df_1, df_2])
    plot(data)
