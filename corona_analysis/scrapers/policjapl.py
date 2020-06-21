import pandas as pd
import urllib
import urllib.error
from sys import stderr
from time import sleep

URL = r"http://policja.pl/pol/form/1,Informacja-dzienna.html?page={}"


def scrape(npages: int = 10, delay: float = 0.5):
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
        for _ in range(0, 100):
            try:
                # Load and parse first table in URL to df
                data.append(pd.read_html(URL.format(i), skiprows=1)[0])
                break
            except urllib.error.HTTPError:
                print("Http error. Trying again... ", file=stderr)
                sleep(delay)
            except ConnectionResetError:
                print("ConnectionResetError error. Trying again... ",
                      file=stderr)
                sleep(delay)
    return {"policjapl": pd.concat(data)}


if __name__ == '__main__':
    print(scrape(delay=2))
