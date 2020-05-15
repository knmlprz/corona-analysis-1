import pandas as pd
import urllib
from sys import stderr
from time import sleep

URL = r"http://policja.pl/pol/form/1,Informacja-dzienna.html?page={}"


def scrape_page_data(npages: int = 10, delay: float = 0.1):
    """
    Scrapes dataset from http://policja.pl/pol/form/1,Informacja-dzienna.html

    Parameters
    ----------
    npages : int
        Number of pages to scrape
    delay : float
        Seconds of delay between requests
    """
    # List to store df
    data = []

    for i in range(0, npages):
        # Try again max 100 times
        for attempt in range(0, 100):
            try:
                # Load and parse first table in URL to df
                data.append(pd.read_html(URL.format(i), skiprows=1)[0])
                break
            except urllib.error.HTTPError:
                print("Http error. Trying again... ", file=stderr)
                sleep(delay)
    return {"policjapl": pd.concat(data)}
