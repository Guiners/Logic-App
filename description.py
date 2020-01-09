"""tak wiec program ma na celu pobrac cale, zlozone wyrazenie w jezyku krz i przeksztalcic je na wyrazenie alternatywne lub koniunkcyjne
aby to zrobic potrzebny jest input uzytkownika
input1 to zmienne jakie wystapia w calym wyrazeniu, robie to w celu ulatwienia zlokalizowania w liscie co jest zmienna a co nie
input2 to po prostu wstawianie pojedynczo znak po znaku tresci wyrazenia do listy
nastepnie program powinnien wykryc wszystkie nawiasy aby moc uznac je w nastepnych krokach jako pojedyncze zmienne oraz aby moc wykonywac
konkretne zadania w odpowiedniej kolejnosci
nastepnie program wykorzystujac instrukcje zawarte w tabelce przeksztalci podane wyrazenia do uproszczonej formy
na koniec program wypluje w princie przeksztalcone wyrazenie"""


"""to tak zeby to dzialalo potrzebujemy wiedziec jakie sa zmienne = zmienne = list()
mozna zrobic tak ze mozna wpisac do zmiennych cala formule
wtedy mozna by skanowac wszystkie zmienne aby znalezc w nim znaki szczegolne typu imlkacje czy cos
i od razu tam poprzeksztalcac ale to nie pewne

nastepnie uzytkownik wpisuje cale wyrazenie ze zmiennymi i program wyszukuje znakow szczegolnych typu implikacja
przeksztalca i wypluwa wszystko"""



"""i teraz tak program powinnien zapisywac pozycje znaku specjalnego na liscie oraz poprzednika i nastepnika tego znaku
i moze zrobic to tak ze bedzie szukal nastepnego znaku specjalnego przed i za nim, ktory NIE JEST w nawiasie i jezeli takiego nie znajdzie
to przyjmuje ze to co przed nim to poprzednik i to po nim to nastepnik, jezeli zas znajdzie to poprzednikiem jest wszystko do nawiasu przed znakiem
specjalnym ktory znalazl i w druga strone tak samo"""

"""ALBO program bedzie wyszukiwac w wyrazeniu zmiennych i gdy je znajdzie to po prostu wykona cale zadanie na tych zmiennych, jezeli zalozymy
taka wersje to komputer nie moze szukac implikacji i innych znakow w zmiennych okreslonych powyzej"""



