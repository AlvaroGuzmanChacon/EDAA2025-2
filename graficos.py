import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"sources": "blue"}

def plot_2(data):
    # Gráfico de largo de patrón vs tiempo, por dataset.
    ax = sns.lineplot(data=data, x="tamano_patron", y="tiempo_busqueda_ns", hue = "archivo_original", palette=palette, marker="*")
    ax.set_xlabel("Largo del patrón")
    ax.set_ylabel("Tiempo promedio de búsqueda (Nanosegundos)")
    plt.show()
    #plt.savefig("4_time_query.png", bbox_inches='tight')

def plot_1(data):
    # Gráfico de número de ocurrencias vs tiempo, por largo de patron, por dataset.
    ax = sns.lineplot(data=data, x="ocurrencias", y="tiempo_busqueda_ns", hue = "tamano_patron", marker="*")
    ax.set_xlabel("Número de ocurrencias")
    ax.set_ylabel("Tiempo promedio de búsqueda (Nanosegundos)")
    ax.set_xlim([-1000,10**5+1000])
    plt.show()
    #plt.savefig("4_time_query.png", bbox_inches='tight')

if __name__ == "__main__":
    #archivo_original,tamano_patron,tiempo_busqueda_ns,ocurrencias
    data = pd.read_csv("exp-FM-busquedas.csv")
    plot_1(data)
    plot_2(data)
