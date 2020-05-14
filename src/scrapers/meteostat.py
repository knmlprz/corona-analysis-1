"""
Gathers data from meteostat API
"""

from urllib import request
from json import JSONDecoder
from os import environ
from sys import stderr

import pandas as pd

URL = "https://api.meteostat.net/v1/history/daily?station={}&start={}&end={}&key={}"
STATION = "12375"  # Warsaw


def get_data(end_date: str,
             key: str = None,
             start_date: str = "2020-02-01",
             url: str = URL,
             station: str = STATION,
             ) -> dict:
    """
    Gets data from meteostat API

    Parameters
    ----------
    end_date : str
        last important date
    key : str, optional
        API key (isn't required if meteostat environmental variable is set)
    start_date : str, optionsl
        first important date (default is "2020-02-01")
    url : str, optional
        meteostat template formatted API URL (default is daily history)
    station : str, optional
        station ID (default is Warsaw)
    """
    if key is None:
        try:
            key = environ["meteostat"]
        except KeyError:
            print("There's no key", file=stderr)
    decoder = JSONDecoder()
    binary_data = request.urlopen(
        url.format(station, start_date, end_date, key)).read()
    print(binary_data)
    data = decoder.decode(binary_data.decode("utf8"))["data"]
    print(data)

    return data


def convert(data: dict) -> pd.DataFrame:
    """
    Converts dict to dataframe

    Parameters
    ----------
    data : dict
        dict to be converted
    """
    return pd.DataFrame(data)
