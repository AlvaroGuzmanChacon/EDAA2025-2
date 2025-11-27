import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#archivo_original,tamano_original_mb,tiempo_construccion_ms,tamano_estructura_mb

def plot_tconstruccion_memoria(data):
    # Gráfico de memoria de estructura por tiempo de construccion
    df_promedio = data.groupby(['archivo_original', 'tamano_estructura_mb', "Estructura"])['tiempo_construccion_ms'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df_promedio, x="tiempo_construccion_ms", y="tamano_estructura_mb", ax=ax, style="Estructura", hue = "archivo_original", s = 70, alpha=0.8)#, palette = palette)
    h, l = ax.get_legend_handles_labels()
    ax.legend(h[1:5], l[1:5], title="Dataset")
    ax.grid()
    ax.set_xlabel(r"Tiempo de construcción (ms)")
    ax.set_ylabel(r"Tamaño de la estructura (MB)")
    plt.savefig(f"P2_memoria_tconstruccion.png", bbox_inches='tight')
    plt.clf()

def plot_tconstruccion_estructura(data):
    # Gráfico de tiempo de construccion por estructura, por dataset.
    for dataset in data["archivo_original"].unique():
        fig, ax = plt.subplots(figsize=(8, 6))
        data_i = data[data["archivo_original"] == dataset]
        sns.barplot(data=data_i, x="Estructura", y="tiempo_construccion_ms", ax=ax, hue = "Estructura")#, palette = palette)
        ax.set_ylabel(r"Tiempo de construcción (ms)")
        ax.set_title(dataset)
        plt.savefig(f"P2_tconstruccion_estructura_{dataset}.png", bbox_inches='tight')
        plt.clf()

def plot_tconstruccion_estructura_total(data):
    # Gráfico de tiempo de construccion por estructura, por dataset.
    fig, ax = plt.subplots(figsize=(8, 6))
    data["tiempo_construccion_ms_normalizado"] = data["tiempo_construccion_ms"] / data["tamano_original_mb"]
    sns.barplot(data=data, x="archivo_original", y="tiempo_construccion_ms_normalizado", ax=ax, hue = "Estructura")#, palette = palette)
    ax.set_ylabel(r"Tiempo de construcción normalizado")
    ax.set_xlabel("Dataset")
    plt.legend(
        loc='lower center',
        bbox_to_anchor=(0.5, 1),
        ncol=3,
        frameon=False
    )
    promedio_SA = data[data["Estructura"]=="SA"]["tiempo_construccion_ms_normalizado"].mean()
    promedio_SALCP = data[data["Estructura"]=="SA+LCP"]["tiempo_construccion_ms_normalizado"].mean()
    promedio_FM = data[data["Estructura"]=="FM-Index"]["tiempo_construccion_ms_normalizado"].mean()
    promedios = [promedio_SA, promedio_SALCP, promedio_FM]
    for i in range(3):
        plt.axhline(
            y=promedios[i],
            color=sns.color_palette()[i],
            linestyle='--',
            linewidth=1,
        )
    plt.savefig(f"P2_tconstruccion_estructura_total.png", bbox_inches='tight')
    plt.clf()

def plot_memoria_estructura(data):
    # Gráfico de memoria utilizada por estructura, por dataset.
    for dataset in data["archivo_original"].unique():
        fig, ax = plt.subplots(figsize=(8, 6))
        data_i = data[data["archivo_original"] == dataset]
        sns.barplot(data=data_i, x="Estructura", y="tamano_estructura_mb", ax=ax, hue = "Estructura")#, palette = palette)
        ax.set_ylabel("Uso de memoria (MB)")
        ax.set_title(dataset)
        plt.savefig(f"P2_memoria_estructura_{dataset}.png", bbox_inches='tight')
        plt.clf()

def plot_memoria_estructura_total(data):
    # Gráfico de tiempo de construccion por estructura.
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=data, x="archivo_original", y="tamano_estructura_mb", ax=ax, hue = "Estructura")#, palette = palette)
    plt.legend(
        loc='lower center',
        bbox_to_anchor=(0.5, 1),
        ncol=3,
        frameon=False
    )
    ax.set_ylabel("Uso de memoria (MB)")
    ax.set_xlabel("Dataset")
    plt.savefig(f"P2_memoria_estructura_total.png", bbox_inches='tight')
    plt.clf()

def plot_compresion_estructura(data):
    # Gráfico de grado de compresión por estructura, por dataset.
    data["Compresion"] = data["tamano_estructura_mb"] / data["tamano_original_mb"]
    for dataset in data["archivo_original"].unique():
        fig, ax = plt.subplots(figsize=(8, 6))
        data_i = data[data["archivo_original"] == dataset]
        sns.barplot(data=data_i, x="Estructura", y="Compresion", ax=ax, hue = "Estructura")#, palette = palette)
        ax.set_ylabel("Grado de compresión")
        ax.set_ylim(bottom=None, top=13)
        ax.set_title(dataset)
        plt.savefig(f"P2_compresion_estructura_{dataset}.png", bbox_inches='tight')
        plt.clf()

def plot_compresion_estructura_total(data):
    # Gráfico de grado de compresión por estructura.
    data["Compresion"] = data["tamano_estructura_mb"] / data["tamano_original_mb"]
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=data, x="archivo_original", y="Compresion", ax=ax, hue = "Estructura")#, palette = palette)
    plt.legend(
        loc='lower center',
        bbox_to_anchor=(0.5, 1),
        ncol=3,
        frameon=False
    )
    promedio_SA = data[data["Estructura"]=="SA"]["Compresion"].mean()
    promedio_SALCP = data[data["Estructura"]=="SA+LCP"]["Compresion"].mean()
    promedio_FM = data[data["Estructura"]=="FM-Index"]["Compresion"].mean()
    promedios = [promedio_SA, promedio_SALCP, promedio_FM]
    for i in range(3):
        plt.axhline(
            y=promedios[i],
            color=sns.color_palette()[i],
            linestyle='--',
            linewidth=1,
        )
    ax.set_ylabel("Grado de compresión")
    ax.set_xlabel("Dataset")
    plt.savefig(f"P2_compresion_estructura_total.png", bbox_inches='tight')
    plt.clf()


if __name__ == "__main__":
    #archivo_original,tamano_original_mb,tiempo_construccion_ms,tamano_estructura_mb
    df_1 = pd.read_csv("SA-construccion.csv")
    df_1["Estructura"] = "SA"
    df_2 = pd.read_csv("SA-LCP-construccion.csv")
    df_2["Estructura"] = "SA+LCP"
    df_3 = pd.read_csv("FM-construccion.csv")
    df_3["Estructura"] = "FM-Index"
    data_construccion = pd.concat([df_1,df_2,df_3])
    plot_memoria_estructura(data_construccion)
    plot_compresion_estructura(data_construccion)
    plot_tconstruccion_estructura(data_construccion)
    plot_memoria_estructura_total(data_construccion)
    plot_compresion_estructura_total(data_construccion)
    plot_tconstruccion_estructura_total(data_construccion)
    plot_tconstruccion_memoria(data_construccion)
