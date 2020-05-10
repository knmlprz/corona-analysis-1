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
    return pd.DataFrame(data)
