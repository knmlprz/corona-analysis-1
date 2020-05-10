import os
from pathlib import Path


def clean_data():
    """
    Cleans data scraped from website www.koronawirusunas.pk

    """

    # Names of files to be deleted
    files_to_rm = ["data", "Data_przyrost_procent",
                   "datah", "datazgony", "datazk",
                   "datazz", "populationData"]

    # Get path to /src/scrapers/Data/koronawirusunas
    path = Path(__file__).parents[1]
    path = Path(path, r"Data/koronawirusunas")

    # Remove files
    for filename in files_to_rm:
        filepath = Path(path, filename + ".csv")
        os.remove(filepath)
        print("Removed file: {}".format(filepath))


if __name__ == "__main__":
    clean_data()
