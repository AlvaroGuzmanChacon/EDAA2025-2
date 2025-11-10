import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Segment Tree": "#4287f5", "Sparse Table": "#f74525"}

def plot(data):
    ax = sns.lineplot(data=data, x="n", y="t_mean", hue = "Estructura", palette=palette, marker="*")
    ax.set_xlabel("Cantidad de elementos (n)")
    ax.set_ylabel("Tiempo promedio de construcción (segundos)")
    plt.savefig("4_time_construction.png", bbox_inches='tight')


if __name__ == "__main__":
    df_1 = pd.read_csv("time_construction_segment_tree.csv", usecols=["n", "t_mean", "Estructura"])
    df_2 = pd.read_csv("time_construction_sparse_table.csv", usecols=["n", "t_mean", "Estructura"])
    data = pd.concat([df_1, df_2])
    data["t_mean"] = data["t_mean"]/1000
    plot(data)
