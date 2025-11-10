import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Segment Tree": "#4287f5", "Sparse Table": "#f74525"}

def plot(data):
    ax = sns.lineplot(data=data, x="n", y="total", hue = "Estructura", palette=palette, marker="*")
    ax.set_xlabel("Instante de tiempo")
    ax.set_ylabel("Uso de memoria (en GB)")
    plt.savefig("4_memoria.png", bbox_inches='tight')
    plt.clf()

    df = data[data["Estructura"] == "Sparse Table"]
    ax = sns.lineplot(data=df, x="n", y="total", marker="*", color=palette["Sparse Table"])
    ax.set_xlabel("Instante de tiempo")
    ax.set_ylabel("Uso de memoria (en GB)")
    plt.savefig("4_memoria_sp.png", bbox_inches='tight')
    plt.clf()


    df = data[data["Estructura"] == "Segment Tree"]
    ax = sns.lineplot(data=df, x="n", y="total", marker="*", color=palette["Segment Tree"])
    ax.set_xlabel("Instante de tiempo")
    ax.set_ylabel("Uso de memoria (en GB)")
    plt.savefig("4_memoria_seg.png", bbox_inches='tight')



if __name__ == "__main__":
    df_1 = pd.read_csv("seg_table_size.csv", usecols=["n", "total"])
    df_1["Estructura"] = "Segment Tree"
    df_2 = pd.read_csv("sp_table_size.csv", usecols=["n", "total"])
    df_2["Estructura"] = "Sparse Table"
    data = pd.concat([df_1, df_2])
    data["total"] = data["total"] - 4295044048
    data = data[data["total"] >= 0]
    data["total"] = data["total"] / 2**30
    plot(data)
