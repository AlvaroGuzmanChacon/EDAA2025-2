import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"sources": "blue"}

def plot_1(data):
    # Gráfico de largo de patrón vs tiempo, por dataset.
    ax = sns.lineplot(data=data, x="tamano_patron", y="tiempo_busqueda_ns", hue = "archivo_original", palette=palette, marker="*")
    ax.set_xlabel("Largo del patrón")
    ax.set_ylabel("Tiempo promedio de búsqueda (Nanosegundos)")
    plt.show()
    #plt.savefig("4_time_query.png", bbox_inches='tight')

def plot_2(data):
    # Gráfico de número de ocurrencias vs tiempo, por largo de patron, por dataset.
    ax = sns.lineplot(data=data, x="ocurrencias", y="tiempo_busqueda_ns", hue = "tamano_patron", marker="*")
    ax.set_xlabel("Número de ocurrencias")
    ax.set_ylabel("Tiempo promedio de búsqueda (Nanosegundos)")
    ax.set_xlim([-1000,10**5+1000])
    plt.show()
    #plt.savefig("4_time_query.png", bbox_inches='tight')


def plot_3(data):
    # Gráfico de estructura vs tiempo de construcción, por dataset.
    ax = sns.lineplot(data=data, x="ocurrencias", y="tiempo_busqueda_ns", hue = "tamano_patron", marker="*")
    ax.set_xlabel("Número de ocurrencias")
    ax.set_ylabel("Tiempo promedio de búsqueda (Nanosegundos)")
    ax.set_xlim([-1000,10**5+1000])
    plt.show()
    #plt.savefig("4_time_query.png", bbox_inches='tight')

def plot_memoria_estructura(data):
    # Gráfico de estructura vs tiempo de construcción, por dataset.
    #palette = {"SA": "blue", "SA+LCP":"red", "FM-Index": "green"}
    #archivo_original,tamano_original_mb,tiempo_construccion_ms,tamano_estructura_mb
    for dataset in data["archivo_original"].unique():
        data_i = data[data["archivo_original"] == dataset]
        ax = sns.barplot(data=data_i, x="Estructura", y="tamano_estructura_mb", hue = "Estructura")#, palette = palette)
        ax.set_ylabel("Uso de memoria (MB)")
        plt.savefig(f"P2_memoria_estructura_{dataset}.png", bbox_inches='tight')
        plt.clf()

if __name__ == "__main__":
    #archivo_original,tamano_patron,tiempo_busqueda_ns,ocurrencias
    df_1 = pd.read_csv("SA-construccion.csv")
    df_1["Estructura"] = "SA"
    df_2 = pd.read_csv("SA-LCP-construccion.csv")
    df_2["Estructura"] = "SA+LCP"
    df_3 = pd.read_csv("FM-construccion.csv")
    df_3["Estructura"] = "FM-Index"
    data_mb = pd.concat([df_1,df_2,df_3])
    plot_memoria_estructura(data_mb)
