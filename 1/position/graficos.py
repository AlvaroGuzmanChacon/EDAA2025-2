import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt



if __name__ == "__main__":
    df = pd.read_csv("results/res.csv", usecols=["n", "t_mean", "t_stdev", "experiment"])
    #df = df[df.experiment != "sequential"]
    ax = sns.lineplot(data=df, x="n", y="t_mean", hue = "experiment", marker="*")
    #ax.set_xscale('log')
    #ax.set_yscale('log')
    #ax.fill_between(df["n"], y1=df["t_mean"] - df["t_stdev"], y2=df["t_mean"] + df["t_stdev"], alpha=.5)
    plt.show()
