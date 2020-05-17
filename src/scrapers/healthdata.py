"""
Automatically get data from healthdata.org
"""
import zipfile
import requests
from io import BytesIO, StringIO
import pandas as pd

URL = "https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip"
FILENAME = "Hospitalization_all_locs.csv"


def get_data(url: str = URL) -> dict:
    """
    Get Data

    Attributes
    ----------
    url : str
        string with url to download file
    """
    # Get file as bytes
    request = requests.get(url)
    data_zipped = zipfile.ZipFile(BytesIO(request.content))

    # Find dataset in zip file
    filelist = data_zipped.namelist()
    file = next((s for s in filelist if FILENAME in s), None)

    return {"healthdata": pd.read_csv(
        StringIO(data_zipped.read(file).decode("utf-8")),
        sep=",", index_col=0)}


if __name__ == '__main__':
    print(get_data())
