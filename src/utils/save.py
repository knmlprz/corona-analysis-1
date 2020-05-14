import pandas as pd
from src.utils.paths import get_path
from pathlib import Path


def save_dataframe(
        data: pd.DataFrame,
        filename: str):
    """
    Saves given dataframe to CSV file

    Parameters
    ----------
    data : pd.DataFrame
        given data in pandas format
    filename : str
        filename without extension
    """
    data.to_csv(Path(get_path(), filename + ".csv"), index=False, mode="w+")
