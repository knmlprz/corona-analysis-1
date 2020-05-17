import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import demjson
from functools import reduce

URL = "https://www.koronawirusunas.pl"
PATTERN = re.compile(r"var\sdataSource_mobilnosc")


def scrape_page_data() -> dict:
    """
    Scrapes datasets from koronawirus.pl

    """
    web = urllib.request.urlopen(URL)
    soup = BeautifulSoup(web.read(), "lxml")

    # Get first script tag that contains PATTERN
    script = soup.find('script', text=PATTERN)

    # Group all vars to ('var name,'[data]')
    jsdata = re.findall(
        r'var\s*(.*?)\s*=(\s*\[[\s\S]*?\]);', script.string)

    return {t[0]: pd.DataFrame(demjson.decode(t[1])) for t in jsdata}


def clean_df(data: pd.DataFrame, cols: list, datecol: str):
    """
    Performs basic cleaning of DataFrame

    Attributes
    ----------
    data : pd.DataFrame
        pd.DataFrame containing data to clean
    cols : list
        list of cols to extract from DataFrame
    datecol : str
        name of col that contains dates, becomes new index
    """
    df = pd.DataFrame(data["dataSource_testy"][cols])
    df[datecol] = pd.to_datetime(df[datecol], dayfirst=True)
    df.set_index(datecol, inplace=True, drop=True)
    df.index.name = None

    return df


def get_data():
    """
    Prepares and outputs cleaned DataFrame
    """

    # Load data
    data = scrape_page_data()

    # Clean data
    testy = clean_df(data["dataSource_testy"],
                     cols=data["dataSource_testy"].columns,
                     datecol="dzien")

    przyrost = clean_df(data["dataSource_przyrost"],
                        cols=["country", "zar", "chor", "zgo", "wyl"],
                        datecol="country")

    mobilnosc = clean_df(data["dataSource_mobilnosc"],
                         cols=["dzien", "pieszo", "pojazdem"],
                         datecol="dzien")

    hospitalizacja = clean_df(data["dataSource_hospitalizacja"],
                              cols=["country", "hosp",
                                    "kwar", "kwar_z", "nadzor"],
                              datecol="country")

    # Merge and return DataFrames
    dframes = [
        hospitalizacja,
        mobilnosc,
        przyrost,
        testy,
    ]

    df_merged = reduce(lambda left, right: pd.merge(left, right,
                                                    how='outer',
                                                    left_index=True,
                                                    right_index=True), dframes)
    return {"koronawirusunas": df_merged}


if __name__ == '__main__':
    get_data()
