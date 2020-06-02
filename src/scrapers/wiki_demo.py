"""
Gathers demographic data from
https://pl.wikipedia.org/wiki/Podzia%C5%82_administracyjny_Polski
"""

import pandas as pd

URL = r"https://pl.wikipedia.org/wiki/Podzia%C5%82_administracyjny_Polski"


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

    return {"demografia": df}


if __name__ == '__main__':
    print(get_data())
