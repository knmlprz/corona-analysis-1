---
title: Zaraźliwość koronawirusa
subtitle: Analiza rozprzestrzeniania się koronawirusa w początkowym okresie pandemii
author:
  - Patryk Gronkiewicz
  - Piotr Krawiec
lang: pl
theme: Dresden
colorscheme: orchid
fonttheme: professionalfonts
---

# Dlaczego akurat takie dane?

# Zdobywanie danych

## Scraping

## Użycie API

API używamy do pobierania danych pogodowych. Pochodzą one z [Meteostatu](https://meteostat.net/en/sources), a pobieramy je dla Warszawy.

### Dostępne dane

API udostępnia takie dane jak temperatura (średnia, max, min), dane o wietrze, nasłonecznieniu, opadach i ciśnieniu - spróbowaliśmy znaleźć korelację między tymi danymi, a zachorowaniami (niekoniecznie natychmiastową). Dla naszego użytku to było najłatwiejsze rozwiązanie, ponieważ Meteostat dostarcza dobre jakościowo dane bez dodatkowych opłat w przeciwieństwie do usług takich jak AccuWeather. Jako miejsce pobrania danych wybraliśmy Warszawę ze względu na bycie - mniej więcej - w centrum kraju. Dodatkowym atutem jest też to, że jako pojedyncze miasto jest największa w Polsce, więc można się było tam spodziewać najlepszego odwzorowania trendów w kraju. Drugim dobrym strzałem mógł się okazać Śląsk ze względu na duże zagęszczenie ludności i fakt, że cała aglomeracja przewyższa populacją Warszawę. 

# Wnioski

## Czego się nauczyliśmy z tej analizy?

## Co innego zyskaliśmy?

