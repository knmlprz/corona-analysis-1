---
title: Analiza rozprzestrzeniania się koronawirusa w początkowym okresie pandemii
author:
  - Patryk Gronkiewicz
  - Piotr Krawiec
abstract: |
  Lorem ipsum dolor sit amet
---

# Jak znaleźć źródła danych?

To było pierwszym pytaniem jakie zadaliśmy sobie w naszym projekcie, ponieważ szczególnie na
początku pandemii dostęp do szczegółowych danych nie był tak prosty. Powodów było kilka:

- na stronie ministerstwa publikowane były wyłącznie dane z danego dnia.
- publicznie dostępne dane dotyczące wielu krajów nie zawierały podziału na
  województwa.
  
A nas szczególnie interesowały dane właśnie z podziałem na województwa, ewentualnie
na jeszcze mniejsze jednostki podziału terytorialnego.

---

# Źródła danych

Na szczęście udało nam się znaleźć inne źródła, tj. strony tworzone przez ludzi,
którzy codziennie sami zbierali te dane i udostępniali je w formie wykresów.
Przykładem takiej strony jest koronawirusunas.pl . Dzięki danym na niej zawartym
udało nam się przeprowadzić.

Do głównych źródeł danych zaliczyć możemy:

- IHME
- koronawirusunas.pl
- policja.pl

---

# Techniki zbierania danych

Główną techniką wykorzystywaną przez nas wył web scraping, stworzyliśmy skrypty,
które
(oczywiście za zgodą właścicieli portali) pobierały z nich bieżące dane. Z kolei
pozostałe dane były udostępnione publicznie w formie skompresowanych plików,
także aktualizowanych codziennie.

---

# Jak pracowaliśmy z danymi

Te dane musiały zostac sprowadzone do wspólnego formatu, tak aby wszystkie
stworzone wykresy i analizy można było odtwarzać natychmiast po aktualizacji
danych, ponieważ te zmieniały się z dnia na dzień wraz z rozwojem pandemii.
Do tego wykorzystaliśmy pythona i Jupyterlab.

---

# Jak pracowaliśmy z danymi

Z pomoca jupyterlab można stworzyć interaktywne notatniki, które działają krok
po kroku, jeden z nich służył wyłącznie do pobrania danych ze wszystkich źródeł
ich oczyszczenia i sprowadzenia do wspólnego formatu. Same analizy znalazły się
w osobnym notatniku, co umożliwiło nam zapanowanie nad projektem. Oczywiście
korzystanie z notatników też ma swoje wady, kolejne zmiany utrzymywane w
systemie kontroli wersji Git nie są czytalne.

![](img/zar.png)