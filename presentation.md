---
title: Analiza rozprzestrzeniania się koronawirusa w początkowym okresie pandemii
author:
  - Patryk Gronkiewicz
  - Piotr Krawiec
abstract: |
  Lorem ipsum dolor sit amet
---

# O nas

::: notes
Jesteśmy studentami Politechniki Rzeszowskiej na kierunku Inżynieria i analiza
danych, a także członkami nowo stworzonego koła uczenia maszynowego. Chcemy
pokazać to, co udało nam się odkryć w trakcie realizacji pierwszego Hackathonu
realizowanego w naszym kole, a dotyczył on pandemii.
:::

[//]: # (Dodać logo koła naukowego)

# Nasz cel

::: notes
Naszym celem było znalezienie, reguł asocjacyjnych i ciekawych zależności w
danych z zachorwań, które docelowo miały nam posłużyć do lepszego zrozumienia
sposobu rozprzestrzeniania się koronawirusa SARS-COV-2 i przewidywania ilości
zachorowań.

Pokażemy, w jaki sposób pracowaliśmy, jakich technik używaliśmy i jak zdobyliśmy
dane, których używaliśmy. Mamy nadzieję, że są wśród was studenci, których
zainteresujemy naszą pracą i dołączą do naszego koła naukowego.
:::

# Dane

::: notes
Jeszcze, gdy zaczynaliśmy, liczba zachorowań nie przekraczała 500 osób
dziennie (był to okres od marca do maja 2020), wtedy kolejnymi falami określano
niewielkie z perspektywy czasu wzrosty zakażeń. 
:::

# Jak znaleźć źródła danych?

::: notes
To było pierwszym pytanie, jakie zadaliśmy sobie w naszym projekcie. Szczególnie
na początku pandemii dostęp do szczegółowych danych nie był tak prosty. Powodów
było kilka:

- na stronie ministerstwa publikowane były wyłącznie dane z danego dnia.
- publicznie dostępne dane dotyczące wielu krajów nie zawierały podziału na
  województwa.

A szczególnie interesowały nas dane z podziałem na województwa, ewentualnie na
jeszcze mniejsze jednostki podziału terytorialnego.
:::

# Źródła danych

::: notes
Na szczęście udało nam się znaleźć inne źródła, tj. strony tworzone przez ludzi,
którzy codziennie sami zbierali te dane i udostępniali je w formie wykresów.
Przykładem takiej strony jest <koronawirusunas.pl>. Dzięki uprzejmości jej
twórców udało nam się pobrać dane na niej zawarte i przeprowadzić wszystkie
analizy.

Do głównych źródeł danych zaliczyć możemy:

- IHME
- koronawirusunas.pl
- policja.pl
:::

# Techniki zbierania danych

::: notes
Główną techniką wykorzystywaną przez nas był web scraping, stworzyliśmy skrypty,
które (oczywiście za zgodą właścicieli portali) pobierały z nich bieżące dane. Z
kolei pozostałe dane były udostępnione publicznie w formie skompresowanych
plików, także aktualizowanych codziennie.
:::

## Dostęp do API

::: notes
Część danych była dostępna bezpośrednio z API, tzn. wysyłając zapytanie do
strony otrzymywaliśmy dane gotowe do przyjęcia przez program. Była to
sytuacja o tyle prostsza od scrapingu, że nie musieliśmy dodatkowo przetwarzać
tych danych.

Wśród danych dostępnych przez API były dane pogodowe, jednak bardzo ułatwiało
to pracę.
:::

# Jak pracowaliśmy z danymi

::: notes
Te dane musiały zostac sprowadzone do wspólnego formatu, tak aby wszystkie
stworzone wykresy i analizy można było odtwarzać natychmiast po aktualizacji
danych, ponieważ te zmieniały się z dnia na dzień wraz z rozwojem pandemii. Do
tego wykorzystaliśmy pythona i Jupyterlab.
::: 

# Jak pracowaliśmy z danymi

::: notes
Z pomoca jupyterlab można stworzyć interaktywne notatniki, które działają krok
po kroku, jeden z nich służył wyłącznie do pobrania danych ze wszystkich źródeł
ich oczyszczenia i sprowadzenia do wspólnego formatu. Same analizy znalazły się
w osobnym notatniku, co umożliwiło nam zapanowanie nad projektem. Oczywiście
korzystanie z notatników też ma swoje wady, kolejne zmiany utrzymywane w
systemie kontroli wersji Git nie są czytalne.
:::

![Wykres zarażeń województwa + Polska](img/zar.png)
