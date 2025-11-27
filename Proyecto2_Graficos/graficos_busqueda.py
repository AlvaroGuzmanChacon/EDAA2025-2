import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#archivo_original,tamano_patron,tiempo_busqueda_ns,ocurrencias

def plot_tbusqueda_lengthpatron(data):
    # Gráfico de tiempo de búsqueda por largo de patrón, por dataset.
    for dataset in data["archivo_original"].unique():
        fig, ax = plt.subplots(figsize=(8, 6))
        data_i = data[data["archivo_original"] == dataset]
        sns.lineplot(data=data_i, x="tamano_patron", y="tiempo_busqueda_ns", ax=ax, hue = "Estructura")#, palette = palette)
        ax.legend()
        ax.set_ylabel(r"Tiempo de búsqueda ($ns$)")
        ax.set_title(dataset)
        plt.savefig(f"P2_tbusqueda_largopatron_{dataset}.png", bbox_inches='tight')
        plt.clf()

def plot_tbusqueda_occpatron(data): 
    # QUIZAS NO VALGA LA PENA PORQUE SÓLO HAY VARIABILIDAD DE OCURRENCIAS PARA PATRONES CHICOS
    # NO SE NOTA LA DIFERENCIA DE TIEMPO SI ES QUE HUBIERA
    # Gráfico de tiempo de búsqueda por número de ocurrencias de patrón, por dataset.
    for dataset in data["archivo_original"].unique():
        fig, ax = plt.subplots(figsize=(8, 6))
        data_i = data[data["archivo_original"] == dataset]
        sns.lineplot(data=data_i, x="tamano_patron", y="tiempo_busqueda_ns", ax=ax, hue = "Estructura")#, palette = palette)
        ax.legend()
        ax.set_ylabel(r"Tiempo de búsqueda ($ns$)")
        ax.set_title(dataset)
        plt.savefig(f"P2_tbusqueda_largopatron_{dataset}.png", bbox_inches='tight')
        plt.clf()



if __name__ == "__main__":
    #archivo_original,tamano_patron,tiempo_busqueda_ns,ocurrencias
    df_1 = pd.read_csv("SA-busquedas1.csv")
    df_1["Estructura"] = "SA"
    df_2 = pd.read_csv("SA-LCP-busquedas1.csv")
    df_2["Estructura"] = "SA+LCP"
    df_3 = pd.read_csv("FM-busquedas1.csv")
    df_3["Estructura"] = "FM-Index"
    data_busqueda = pd.concat([df_1,df_2,df_3])
    plot_tbusqueda_lengthpatron(data_busqueda)
