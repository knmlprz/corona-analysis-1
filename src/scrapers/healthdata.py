"""
Automatically get data from healthdata.org
"""
from urllib import request
from sys import platform
from os import environ
import zipfile

URL = "https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip"


def get_data(url: str = URL):
    """
    Get Data

    ...

    Attributes
    ----------
    url : str
        string with url to download file
    """
    data_zipped = request.urlopen(URL).read()

    if platform == "linux":
        tmp_file = "/tmp/zipped.zip"
    elif platform == "win32":
        tmp_file = "{}zipped.zip".format(environ["TEMP"])
    if platform == "darwin":
        tmp_file = "{}zipped.zip".format(environ["TMPDIR"])

    with open(tmp_file, "w") as zipped:
        zipped.write(data_zipped)

    with zipfile.ZipFile("zipped.zip", "r") as zipped:
        zipped.extractall("data/healthdata")
