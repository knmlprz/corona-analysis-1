# Corona analysis 1

This repository is made to gather all data about spreading of SARS-CoV-2 in 
Poland.

## Requirements

* `Python` 3.4 or greater
* `BeautifulSoup` 4
* `Pandas`
* `Seaborn`

## Data sources

* [Meteostat](https://meteostat.net/en/sources) Meteorological data: Copyright ©
National Oceanic and Atmospheric Administration (NOAA),
Deutscher Wetterdienst (DWD)
* [RMF24](https://www.rmf.fm/inc/outer/korona-wykres/wykres.html)
* [Polish Police statistics](http://policja.pl/pol/form/1,dok.html)
* [Koronawirusunas](http://koronawirusunas.pl)
* [IHME](http://www.healthdata.org/)

## Installation
```
$ git clone https://github.com/prz-ml/corona-analysis-1.git 
$ cd corona-analysis-1
$ python -m pip install -r requirements.txt
$ python setup.py install
```

## Usage
All the scripts in `corona-analysis/scrapers` contain `get_data()` that gathers 
and cleans dataset of choice.
```python
from corona_analysis.scrapers import koronawirusunas
koronawirusunas.get_data()
```
**Gathering some datasets may require an api key. Currently only `meteostat` 
scraper requires one.**
