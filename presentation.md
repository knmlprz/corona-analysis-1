---
title: Analiza rozprzestrzeniania się koronawirusa w początkowym okresie pandemii
author:
  - Patryk Gronkiewicz
  - Piotr Krawiec
abstract: |
  Lorem ipsum dolor sit amet
---


# Źródła danych

To było pierwszym sporym wyzwaniem w naszym projekcie, ponieważ szczególnie na początku
pandemii dostęp do szczegółowych danych nie był tak prosty, ponieważ: 
- na stronie ministerstwa publikowane były wyłącznie dane z danego dnia.
- publicznie dostępne dane dotyczące wielu krajów nie zawierały podziału na województwa.

Na szczęście udało nam się znaleźć inne źródła, tj. strony tworzone przez ludzi, którzy
codziennie sami zbierali te dane i udostępniali je w formie wykresów. Przykładem takiej 
strony jest koronawirusunas.pl . Dzięki danym na niej zawartym udało nam się 
przeprowadzić.

Do głównych źródeł danych zaliczyć możemy:
- IHME
- koronawirusunas.pl
- policja.pl

# Techniki zbierania danych

Główną techniką wykorzystywaną przez nas wył web scraping, stworzyliśmy skrypty, które
(oczywiście za zgodą właścicieli portali) pobierały z nich bieżące dane. Z kolei pozostałe
dane były udostępnione publicznie w formie skompresowanych plików, także aktualizowanych
codziennie. 


![](img/zar.png)