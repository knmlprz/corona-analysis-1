import pandas as pd
from corona_analysis.utils.paths import get_path
from pathlib import Path


def save_dataframe(
        data: pd.DataFrame,
        filename: str,
        subdir: str = ""):
    """
    Saves given dataframe to CSV file

    Parameters
    ----------
    data : pd.DataFrame
        given data in pandas format
    filename : str
        filename without extension
    subdir : str
        subdirectory of ./data to put files into
    """
    data.to_csv(Path(get_path(subdir=subdir), filename + ".csv"),
                mode="w+")


def save_dataframes(
        data: dir,
        subdir: str = ""):
    """
    Saves given dataframes to specified subdir in ./data

    Parameters
    ----------
    data : pd.DataFrame
        given data in dict :  {"filename": pd.DataFrame, ...}
    subdir : str
        subdirectory of ./data to put files into
    """
    for key in data.keys():
        save_dataframe(data=data[key], filename=key, subdir=subdir)
