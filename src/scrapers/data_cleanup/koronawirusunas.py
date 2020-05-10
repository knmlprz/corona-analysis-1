import os
from pathlib import Path
import pandas as pd
from functools import reduce


def datafolder_path():
    path = Path(__file__).parents[1]
    return Path(path, r"Data/koronawirusunas")




def clean_datasource_testy(path=datafolder_path(), filename="dataSource_testy.csv"):
    if Path(path, filename).is_file()
        df = pd.read_csv(Path(path, filename),
                         sep="\t",
                         index_col=0,
                         usecols=["dzien", "smp", "testy", "testyl"],
                         parse_dates=['dzien'],
                         dayfirst=True
                         )
        df.index.name = None
    return df


def clean_datasource_przyrost(path=datafolder_path(), filename="dataSource_przyrost.csv"):
    df = pd.read_csv(Path(path, filename),
                     sep="\t",
                     index_col=0,
                     usecols=["country", "zar", "chor", "zgo", "wyl"],
                     parse_dates=['country'],
                     dayfirst=True
                     )
    df.index.name = None
    return df


def clean_datasource_mobilnosc(path=datafolder_path(), filename="dataSource_mobilnosc.csv"):
    df = pd.read_csv(Path(path, filename),
                     sep="\t",
                     index_col=0,
                     usecols=["dzien", "pieszo", "pojazdem"],
                     parse_dates=['dzien'],
                     dayfirst=True
                     )
    df.index.name = None
    return df


def clean_datasource_hospitalizacja(path=datafolder_path(), filename="dataSource_hospitalizacja.csv"):
    df = pd.read_csv(Path(path, filename),
                     sep="\t",
                     index_col=0,
                     usecols=["country", "hosp",
                              "kwar", "kwar_z", "nadzor"],
                     parse_dates=['country'],
                     dayfirst=True
                     )
    df.index.name = None
    return df


def clean_data():
    """
    Cleans data scraped from website www.koronawirusunas.pk

    """
    # Load dataframes
    df = [
        clean_datasource_hospitalizacja(),
        clean_datasource_mobilnosc(),
        clean_datasource_przyrost(),
        clean_datasource_testy(),
    ]

    df_merged = reduce(lambda left, right: pd.merge(left, right,
                                                    how='outer'), df)
    return df_merged


if __name__ == "__main__":
    clean_data()
