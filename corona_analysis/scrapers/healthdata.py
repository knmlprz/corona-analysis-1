"""
Automatically get data from healthdata.org
"""
import zipfile
from io import BytesIO, StringIO
import pandas as pd
from urllib import request

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
    req = request.urlopen(url).read()
    data_zipped = zipfile.ZipFile(BytesIO(req))

    # Find dataset in zip file
    filelist = data_zipped.namelist()
    file = next((s for s in filelist if FILENAME in s), None)

    return {"healthdata": pd.read_csv(
        StringIO(data_zipped.read(file).decode("utf-8")),
        sep=",", index_col=0)}


if __name__ == '__main__':
    print(get_data())
