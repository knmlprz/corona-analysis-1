import pandas as pd
from src.utils.paths import get_path
from pathlib import Path


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
    data.to_csv(Path(get_path(), filename + ".csv"), index=False, mode="w+")
