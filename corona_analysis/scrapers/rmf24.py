"""
This module gathers data from RMF24 chart
"""

import re
from urllib import request
from typing import List, Dict, Any, Optional

import pandas as pd
from bs4 import BeautifulSoup

from corona_analysis.utils.affixes import remove_prefix
from corona_analysis.utils.affixes import remove_suffix

URL = "https://www.rmf.fm/inc/outer/korona-wykres/wykres.html"


def scrape(data_url: str = URL) -> Dict[str, Any]:
    """
    Scrapes data from rmf's chart

    ...

    Attributes
    ----------
    data_url : str
        url of the website with data
    """
    # Load web page
    page = request.urlopen(data_url)

    # Create parser
    soup = BeautifulSoup(page.read(), "html.parser")
    # Data is stored in the last script
    data = str(soup.body.find("script"))

    # find lists of data
    (sick, deaths, recoveries, vaccinations) = re.findall(r"\[\[.*\]\]", data)

    sick = sick.split("],[")
    deaths = deaths.split("],[")
    recoveries = recoveries.split("],[")
    vaccinations = vaccinations.split("],[")

    sick = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in sick
    ]
    deaths = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in deaths
    ]
    recoveries = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in recoveries
    ]
    vaccinations = [
        remove_suffix(remove_prefix(remove_prefix(i, "[["), "Date.UTC"), "]]")
        for i in vaccinations
    ]

    sick = [i.split("),") for i in sick]
    deaths = [i.split("),") for i in deaths]
    recoveries = [i.split("),") for i in recoveries]
    vaccinations = [i.split("),") for i in vaccinations]

    sick = [["-".join(i[0][1:].split(",")), i[1]] for i in sick]
    deaths = [["-".join(i[0][1:].split(",")), i[1]] for i in deaths]
    vaccinations = [["-".join(i[0][1:].split(",")), i[1]] for i in vaccinations]

    return {
        "sick": sick,
        "deaths": deaths,
        "recovers": recoveries,
        "vaccinations": vaccinations,
    }


def get_data(url: str = URL) -> Dict[str, pd.DataFrame]:
    """
    Returns dataframe of deaths, recovered and sick people

    Attributes
    ----------
    sick : list
        list of lists with date and amount of sick people
    deaths : list
        list of lists with date and amount of dead people
    recovers : list
        list of lists with date and amount of recovered people

    Returns
    -------
    dict
        "rmf24" with dataframe
    """
    data = scrape(URL)

    sickDF = pd.DataFrame(data["sick"])
    sickDF.columns = ("date", "sick")

    deathsDF = pd.DataFrame(data["deaths"])
    deathsDF.columns = ("date", "deaths")

    recoveriesDF = pd.DataFrame(data["recoveries"])
    recoveriesDF.columns = ("date", "recoveries")

    vaccinationsDF = pd.DataFrame(data["vaccinations"])
    vaccinationsDF.columns = ("date", "vaccinations")

    tmp = pd.merge(sickDF, deathsDF, how="outer", on="date")
    tmp = pd.merge(tmp, recoveriesDF, how="outer", on="date")
    tmp = pd.merge(tmp, vaccinationsDF, how="outer", on="date")

    return {"rmf24": tmp}
