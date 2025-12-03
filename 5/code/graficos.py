import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

palette = {"Segment Tree": "#4287f5", "Sparse Table": "#f74525"}
MM_types = ["MM", "MMT", "MMS"]
variables = ["cycles", "instructions", "L1-dcache-loads", "L1-dcache-load-misses", "size", "prop_miss_load"]

def process_data(N_values):
    df_list = []
    for mm_type in MM_types:
        df = pd.DataFrame()
        for N in N_values:
            filename = f"{mm_type}_{2**N}.csv"
            df_aux = pd.read_csv(filename, sep=";")
            df_aux = df_aux.drop(df_aux.columns[[0, 1]], axis=1)
            df_aux["size"] = 2**N
            df = pd.concat([df, df_aux])
        df["mm_type"] = mm_type
        df_list.append(df)
    df_ret = pd.concat(df_list).reset_index(drop=True)
    df_ret["prop_miss_load"] = df_ret["L1-dcache-load-misses"] / df_ret["L1-dcache-loads"]
    df_ret["task-clock"] = df_ret['task-clock'].str.replace(',', '.')
    df_ret["task-clock"] = pd.to_numeric(df_ret["task-clock"], errors="coerce")
    return df_ret


def plot(df):
    for variable in variables:
        ax = sns.lineplot(data=df, x=str(variable), y="task-clock", hue = "mm_type", marker="*")
        ax.set_xlabel(f"{variable}")
        ax.set_ylabel("Tiempo de ejcución (ms)")
        plt.savefig(f"5_{variable}_tiempo.png", bbox_inches='tight')
        plt.clf()



if __name__ == "__main__":
    df = process_data([6,7,8,9,10])
    #print(df.dtypes)
    plot(df)
