import pandas as pd
from os import environ
from sys import platform


def save_dataframe(
        data: pd.DataFrame,
        filename: str,
        destination: str = None):

    """
    Saves given dataframe to CSV file

    Parameters
    ----------
    data : pd.DataFrame
        given data in pandas format
    filename : str
        filename without extension
    destination : str, optional
        data folder destination (defaults to system cache directory)
    """
    if destination is None:
        if platform == "linux":
            destination = environ["HOME"] + "/.cache/ca1/"
        if platform == "win32":
            destination = environ["localappdata"] + "\\ca1\\"
        if platform == "darwin":
            destination = environ["HOME"] + "/Library/Caches/ca1/"
            
    data.to_csv(destination + filename + ".csv", index=False, mode="w+")
