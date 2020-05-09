import re
from urllib import request

import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://www.rmf.fm/inc/outer/korona-wykres/wykres.html"


def remove_prefix(string, prefix):
    """
    Removes unwanted prefix from string
    :param string string to edit
    :param prefix patter for prefix
    """
    if prefix in string[: len(prefix)]:
        return string[len(prefix) :]
    else:
        return string


def remove_suffix(string, suffix):
    """
    Removes unwanted suffix from string
    :param string string to edit
    :param suffix patter for suffix
    """
    if suffix in string[: len(suffix)]:
        return string[len(suffix) :]
    else:
        return string


def scrape_page_data(url=url):
    """
    Scrapes data from rmf's chart
    :param url url of the website with data
    """
    # Load web page
    page = request.urlopen(url)
    # Create parser
    soup = bs(page.read(), "html.parser")
    # Data is stored in the last script
    data = str(soup.body.find("script"))

    # find lists of data
    (sick, deaths, recovers) = re.findall(r"\[\[.*\]\]", data)

    sick = sick.split("],[")
    deaths = deaths.split("],[")
    recovers = recovers.split("],[")

    sick = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in sick
    ]
    deaths = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in deaths
    ]
    recovers = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in recovers
    ]

    sick = [i.split("),") for i in sick]
    deaths = [i.split("),") for i in deaths]
    recovers = [i.split("),") for i in recovers]

    sick = [["-".join(i[0][1:].split(",")), i[1]] for i in sick]
    deaths = [["-".join(i[0][1:].split(",")), i[1]] for i in deaths]
    recovers = [["-".join(i[0][1:].split(",")), i[1]] for i in recovers]

    return {"sick": sick, "deaths": deaths, "recovers": recovers}


def convert_data(sick, deaths, recovers):
    """
    Returns dict of dataframes. Elements named same as function arguments
    :param sick list of lists with date and amount of sick people
    :param deaths list of lists with date and amount of dead people
    :param recovers list of lists with date and amount of recovered people
    """

    sick = pd.DataFrame(sick)
    sick.columns = ("date", "sick")

    deaths = pd.DataFrame(deaths)
    deaths.columns = ("date", "deaths")

    recovers = pd.DataFrame(recovers)
    recovers.columns = ("date", "recovers")

    return {"sick": sick, "deaths": deaths, "recovers": recovers}
