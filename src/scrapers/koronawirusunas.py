import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import demjson

URL = "https://www.koronawirusunas.pl"
PATTERN = re.compile(r"var\sdataSource_mobilnosc")


def scrape() -> dict:
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


def clean(data: pd.DataFrame, cols: list, new_index_name: str):
    """
    Performs basic cleaning of DataFrame

    Attributes
    ----------
    data : pd.DataFrame
        pd.DataFrame containing data to clean
    cols : list
        list of cols to extract from DataFrame
    new_index_name : str
        name of col that contains dates, becomes new index
    """
    df = pd.DataFrame(data["dataSource_testy"][cols])
    df[new_index_name] = pd.to_datetime(df[new_index_name], dayfirst=True)
    df.set_index(new_index_name, inplace=True, drop=True)
    df.index.name = None

    return df


def get_data():
    """
    Prepares and outputs cleaned DataFrame
    """

    # Load data
    data = scrape()

    # Clean data
    testy = clean(data["dataSource_testy"],
                  cols=data["dataSource_testy"].columns,
                  new_index_name="dzien")

    przyrost = clean(data["dataSource_przyrost"],
                     cols=["country", "zar", "chor", "zgo", "wyl"],
                     new_index_name="country")

    mobilnosc = clean(data["dataSource_mobilnosc"],
                      cols=["dzien", "pieszo", "pojazdem"],
                      new_index_name="dzien")

    hospitalizacja = clean(data["dataSource_hospitalizacja"],
                           cols=["country", "hosp",
                                 "kwar", "kwar_z", "nadzor"],
                           new_index_name="country")

    # Merge and return DataFrames
    df = pd.merge(testy, przyrost, how='outer', left_index=True,
                  right_index=True)
    df = pd.merge(df, mobilnosc, how='outer', left_index=True,
                  right_index=True)
    df = pd.merge(df, hospitalizacja, how='outer', left_index=True,
                  right_index=True)

    return {"koronawirusunas": df}


if __name__ == '__main__':
    get_data()
