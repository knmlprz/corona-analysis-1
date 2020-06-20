"""
Gathers demographic data from
https://pl.wikipedia.org/wiki/Podzia%C5%82_administracyjny_Polski
"""

import pandas as pd
import numpy as np
from src.utils.cleaners import fix_numerical, strip_accents

URL = r"https://pl.wikipedia.org/wiki/Podzia%C5%82_administracyjny_Polski"


def clean(data: pd.DataFrame):
    """
        Cleans data about urbanization

        ...

        Attributes
        ----------
        data : pd.DataFrame
            raw DataFrame from website
        """

    data.index.name = None
    data.drop([16, 17], inplace=True)
    data.columns = [x[1] for x in data.columns]

    data.rename(columns={
        "Województwo": "wojewodztwo",
        "Miasta": "miasta",
        "II stopień adm.": "powiaty",
        "m. na prawach powiatu": "m_powiaty",
        "ogółem": "gminy_ogolem",
        "Gminy.1": "miejskie",
        "Gminy.2": "wiejskie",
    }, inplace=True)

    data = data.loc[:,
           ['wojewodztwo', 'miasta', 'powiaty', 'm_powiaty', 'gminy_ogolem',
            'miejskie', 'wiejskie', 'miejsko-wiejskie']]

    # Fix numerical
    # cols = data.columns.drop('wojewodztwo')
    # data[cols] = data[cols].applymap(fix_numerical)
    # data[cols] = data[cols].apply(pd.to_numeric)

    # Strip accents
    data['wojewodztwo'] = data['wojewodztwo'].apply(strip_accents)
    # Fix missing 'ł' character
    data.replace({"odzkie": "lodzkie",
                  "maopolskie": "malopolskie"}, inplace=True)

    return data


def get_data(url=URL):
    """
        Scrapes data from wiki table

        ...

        Attributes
        ----------
        url : str
            url of the website with data
        """

    # Load data from web
    df = pd.read_html(url)[0]

    # Drop unused cols
    df.drop(axis=1, labels=["Herb", "Flaga"], inplace=True)

    df = clean(df)

    return {"demografia": df}


if __name__ == '__main__':
    print(get_data()['demografia'])
