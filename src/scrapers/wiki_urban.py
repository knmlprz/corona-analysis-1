"""
Gathers urbanization data from
https://pl.wikipedia.org/wiki/Wojew%C3%B3dztwo
"""

import pandas as pd
from src.utils.cleaners import fix_numerical, strip_accents

URL = r"https://pl.wikipedia.org/wiki/Wojew%C3%B3dztwo"


def clean(data: pd.DataFrame):
    """
        Cleans data about urbanization

        ...

        Attributes
        ----------
        data : pd.DataFrame
            raw DataFrame from website
        """

    data = data.drop(columns=["TERYT", "Miasta – siedziby województw",
                              "Wyróżnik województwa na "
                              "tablicachrejestracyjnych"])

    data.rename(columns={
        "Województwo": "wojewodztwo",
        "Powierzchnia[km²], 31.12.2018[3]": "powierzchnina",
        "Ludność(31 XII 2018)[4]": "ludnosc",
        "Gęstość zaludnienia (osób/km²)": "gestosc_zal",
        "Poziomurbanizacji(31 XII 2018)": "urbanizacja",
        "Stopa bezrobocia(I\xa02019)[5]": "stopa_bezrobocia",
        "PKB na 1 mieszkańca(31 XII 2018) [zł][3]": "pkb_na_miesz"
    }, inplace=True)

    # Fix numerical values in DataFrame
    cols = data.columns.drop('wojewodztwo', 'gestosc_zal')
    data[cols] = data[cols].applymap(fix_numerical)
    data[cols] = data[cols].apply(pd.to_numeric)

    # Strip accents
    data['wojewodztwo'] = data['wojewodztwo'].apply(strip_accents)

    # Fix missing 'ł' character
    data.replace({"odzkie": "lodzkie",
                  "maopolskie": "malopolskie"}, inplace=True)

    return data


def get_data(url=URL):
    """
        Scrapes data about urbanization
        from wiki table

        ...

        Attributes
        ----------
        url : str
            url of the website with data
        """

    # Load data from web
    df = pd.read_html(url)[0]

    df = clean(df)

    return {"urbanizacja": df}


if __name__ == '__main__':
    print(get_data())
