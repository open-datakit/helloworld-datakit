import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def main(data: pd.DataFrame, fit: pd.DataFrame) -> Figure:
    plt.scatter(data.index, data["y"], label="Data", color="royalblue")
    plt.plot(fit.index, fit["y"], label="Fit", color="darkorange")
    plt.legend()

    # Return current figure
    return plt.gcf()
