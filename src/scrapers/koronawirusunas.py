import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import demjson

URL = "https://www.koronawirusunas.pl/{}"
PATTERN = re.compile(r"var\sdataSource_przyrost")
SUB_SITES = ("",
             "wojewodztwo-slaskie",
             "wojewodztwo-mazowieckie",
             "wojewodztwo-dolnoslaskie",
             "wojewodztwo-wielkopolskie",
             "wojewodztwo-lodzkie",
             "wojewodztwo-malopolskie",
             "wojewodztwo-opolskie",
             "wojewodztwo-kujawsko-pomorskie",
             "wojewodztwo-pomorskie",
             "wojewodztwo-zachodniopomorskie",
             "wojewodztwo-podlaskie",
             "wojewodztwo-lubelskie",
             "wojewodztwo-podkarpackie",
             "wojewodztwo-swietokrzyskie",
             "wojewodztwo-warminsko-mazurskie",
             "wojewodztwo-lubuskie")


def scrape(url=URL) -> dict:
    """
    Scrapes datasets from koronawirus.pl

    """
    web = urllib.request.urlopen(url)
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
    df = pd.DataFrame(data[cols])
    df[new_index_name] = pd.to_datetime(df[new_index_name], dayfirst=True)
    df.set_index(new_index_name, inplace=True, drop=True)
    df.index.name = None

    return df


def get_data():
    """
    Prepares and outputs cleaned DataFrame
    """

    # Load data
    data = [scrape(url=URL.format(sub)) for sub in SUB_SITES]

    # Clean data for whole country
    testy = clean(data[0]["dataSource_testy"],
                  cols=data[0]["dataSource_testy"].columns,
                  new_index_name="dzien")

    przyrost = clean(data[0]["dataSource_przyrost"],
                     cols=["country", "zar", "chor", "zgo", "wyl"],
                     new_index_name="country")

    mobilnosc = clean(data[0]["dataSource_mobilnosc"],
                      cols=["dzien", "pieszo", "pojazdem"],
                      new_index_name="dzien")

    hospitalizacja = clean(data[0]["dataSource_hospitalizacja"],
                           cols=["country", "hosp",
                                 "kwar", "kwar_z", "nadzor"],
                           new_index_name="country")

    przyrost_woj = {SUB_SITES[i][12:]: clean(data[i]["dataSource_przyrost"],
                                             cols=["country", "zar", "chor",
                                                   "zgo", "wyl"],
                                             new_index_name="country")
                    for i in range(1, len(data))}

    # Merge and return DataFrames
    df_poland = pd.merge(testy, przyrost, how='outer', left_index=True,
                         right_index=True)
    df_poland = pd.merge(df_poland, mobilnosc, how='outer', left_index=True,
                         right_index=True)
    df_poland = pd.merge(df_poland, hospitalizacja, how='outer',
                         left_index=True,
                         right_index=True)

    return {"koronawirusunas": df_poland, **przyrost_woj}


if __name__ == '__main__':
    print(get_data())
