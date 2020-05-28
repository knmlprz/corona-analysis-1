"""
Gathers urbanization data from
https://pl.wikipedia.org/wiki/Wojew%C3%B3dztwo
"""

import pandas as pd

URL = r"https://pl.wikipedia.org/wiki/Wojew%C3%B3dztwo"


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

    return {"urbanizacja": df}


if __name__ == '__main__':
    print(get_data())
