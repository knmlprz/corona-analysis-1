from pathlib import Path
import pandas as pd
from functools import reduce
from sys import stderr
from src.utils.paths import get_path


def datafolder_path():
    return get_path(subdir="koronawirusunas")


def clean_datasource_testy(path=datafolder_path(), filename="dataSource_testy.csv"):
    if Path(path, filename).is_file():
        df = pd.read_csv(Path(path, filename),
                         sep="\t",
                         index_col=0,
                         usecols=["dzien", "smp", "testy", "testyl"],
                         parse_dates=['dzien'],
                         dayfirst=True
                         )
        df.index.name = None
        return df
    else:
        print("File {} not found".format(filename), file=stderr)
        return pd.DataFrame()


def clean_datasource_przyrost(path=datafolder_path(), filename="dataSource_przyrost.csv"):
    if Path(path, filename).is_file():
        df = pd.read_csv(Path(path, filename),
                         sep="\t",
                         index_col=0,
                         usecols=["country", "zar", "chor", "zgo", "wyl"],
                         parse_dates=['country'],
                         dayfirst=True
                         )
        df.index.name = None
        return df
    else:
        print("File {} not found".format(filename), file=stderr)
        return pd.DataFrame()


def clean_datasource_mobilnosc(path=datafolder_path(), filename="dataSource_mobilnosc.csv"):
    if Path(path, filename).is_file():
        df = pd.read_csv(Path(path, filename),
                         sep="\t",
                         index_col=0,
                         usecols=["dzien", "pieszo", "pojazdem"],
                         parse_dates=['dzien'],
                         dayfirst=True
                         )
        df.index.name = None
        return df
    else:
        print("File {} not found".format(filename), file=stderr)
        return pd.DataFrame()


def clean_datasource_hospitalizacja(path=datafolder_path(), filename="dataSource_hospitalizacja.csv"):
    if Path(path, filename).is_file():
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
    else:
        print("File {} not found".format(filename), file=stderr)
        return pd.DataFrame()


def clean_data():
    """
    Cleans data scraped from website www.koronawirusunas.pk

    :returns pandas.DataFrame containing merged data
    """
    # Load dataframes
    df = [
        clean_datasource_hospitalizacja(),
        clean_datasource_mobilnosc(),
        clean_datasource_przyrost(),
        clean_datasource_testy(),
    ]

    df_merged = reduce(lambda left, right: pd.merge(left, right,
                                                    how='outer',
                                                    left_index=True,
                                                    right_index=True), df)
    return df_merged


if __name__ == "__main__":
    print(clean_data())
