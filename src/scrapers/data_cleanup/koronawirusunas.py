import os
from pathlib import Path
import pandas as pd


def clean_data():
    """
    Cleans data scraped from website www.koronawirusunas.pk

    """

    # Names of files to be deleted
    files_to_rm = ["data", "Data_przyrost_procent",
                   "datah", "datazgony", "datazk",
                   "datazz", "populationData",
                   "Data_przyrost_szpital", "Data_przyrost_testy"]

    # Names of files to be cleaned
    files_to_clean = ["dataSource_hospitalizacja", "dataSource_mobilnosc",
                      "dataSource_przyrost", "dataSource_testy"]

    # Get path to /src/scrapers/Data/koronawirusunas
    path = Path(__file__).parents[1]
    path = Path(path, r"Data/koronawirusunas")

    # Remove files
    for filename in files_to_rm:
        filepath = Path(path, filename + ".csv")
        if os.path.isfile(filepath):
            os.remove(filepath)
            print("Removed file: {}".format(filepath))

    # Check if files to clean exist
    for filename in files_to_clean:
        filepath = Path(path, filename + ".csv")
        if os.path.isfile(filepath):
            print("Found file: {}".format(filepath))
        else:
            # Exit if file is not present
            print("Error missing file: {}".format(filepath))
            return

    # Load dataframes
    hospitalizacja = pd.read_csv(Path(path, files_to_clean[0] + ".csv"),
                                 sep="\t",
                                 index_col=0,
                                 usecols=["country", "hosp",
                                          "kwar", "kwar_z", "nadzor"],
                                 parse_dates=['country'],
                                 dayfirst=True
                                 )

    mobilnosc = pd.read_csv(Path(path, files_to_clean[1] + ".csv"),
                            sep="\t",
                            index_col=0,
                            usecols=["dzien", "pieszo", "pojazdem"],
                            parse_dates=['dzien'],
                            dayfirst=True
                            )

    przyrost = pd.read_csv(Path(path, files_to_clean[2] + ".csv"),
                           sep="\t",
                           index_col=0,
                           usecols=["country", "zar", "chor", "zgo", "wyl"],
                           parse_dates=['country'],
                           dayfirst=True
                           )
    testy = pd.read_csv(Path(path, files_to_clean[3] + ".csv"),
                        sep="\t",
                        index_col=0,
                        usecols=["dzien", "smp", "testy", "testyl"],
                        parse_dates=['dzien'],
                        dayfirst=True
                        )

    # Remove index.name
    hospitalizacja.index.name = None
    mobilnosc.index.name = None
    przyrost.index.name = None
    testy.index.name = None

    # Join df
    df = hospitalizacja.join(mobilnosc, how="outer")
    df = df.join(przyrost, how="outer")
    df = df.join(testy, how="outer")
    df.sort_index()

    # Dump df to csv
    outname = "data_koronawirusunas.csv"
    df.to_csv(Path(path, outname))


if __name__ == "__main__":
    clean_data()
