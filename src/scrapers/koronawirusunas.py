import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import demjson

URL = "https://www.koronawirusunas.pl"
PATTERN = re.compile(r"var\sdataSource_mobilnosc")


def scrape_page_data() -> dict:
    """
    Scrapes dataset from koronawirus.pl

    """
    web = urllib.request.urlopen(URL)
    soup = BeautifulSoup(web.read(), "lxml")

    # Get first script tag that contains PATTERN
    script = soup.find('script', text=PATTERN)

    # Group all vars to ('var name,'[data]')
    jsdata = re.findall(
        r'var\s*(.*?)\s*=(\s*\[[\s\S]*?\]);', script.string)

    return {t[0]: pd.DataFrame(demjson.decode(t[1])) for t in jsdata}


if __name__ == '__main__':
    scrape_page_data()
