import pandas as pd
from typing import TypedDict
from scipy.optimize import curve_fit


class Output(TypedDict):
    outputParams: pd.DataFrame
    fit: pd.DataFrame


# Fit model functions


def linear(x, a, b):
    """Linear fit model"""
    return a * x + b


def quadratic(x, a, b, c):
    """Quadratic fit model"""
    return a * x**2 + b * x + c


# Main algorithm function


def main(data: pd.DataFrame, model: str, inputParams: pd.DataFrame) -> Output:
    """Fit a linear or quadratic model to some data"""

    params, _ = curve_fit(
        f=globals()[model],  # Call the global function named "model"
        xdata=data.index,
        ydata=data["y"],
        p0=inputParams["init"],
    )

    # Transform curve_fit output into expected output table format
    names = ["a", "b", "c"]
    table = [[name, param] for name, param in zip(names, params)]
    outputParams = pd.DataFrame(
        table,
        columns=["name", "value"],
    )

    # Calculate the optimised fit curve
    fit = data.copy(deep=True)
    fit["y"] = globals()[model](fit.index, *params)

    return {
        "outputParams": outputParams,
        "fit": fit,
    }
