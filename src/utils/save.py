import pandas as pd


def save_dataframe(
        data: pd.DataFrame,
        filename: str,
        destination: str = "./data"):
    """
    Saves given dataframe to CSV file

    Parameters
    ----------
    data : pd.DataFrame
        given data in pandas format
    filename : str
        filename without extension
    destination : str
        data folder destination (defaults to "./data")
    """
    data.to_csv(destination + filename + ".csv", index=False, mode="w+")
