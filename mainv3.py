zmienne = list()
wyrazenie = list()
working = True
implikacje = list()
rownowaznosci = list()
alternatywy = list()
koniunkcje = list()
negacje = list()


print("wpisz ile zmiennych bedzie w wyrazeniu")
print("Potraktuj zlozone wyrazenia jako jedno wyrazenie, tzn jezeli chcesz przeksztalcic'(pVp) -> (pvp)' to wpisz '(pvp)' jako jedna zmienna")
for i in range(int(input())):
    print("wprowadz zmienne")
    zmienne.append(input())

print("oto twoje zmienne" ,zmienne)

print("Wpisz wyrażenie logiczne a ja przerobie je na uproszczone")
print("Zmienne wprowadzaj wedlug tego schematu:"
      "pierwsza zmienna na liscie powyzej odpowiada numerowi 0, druga numerowi 1, trzecia numerowi 2 itd.")
print("Implikacje umieść jako jedno w ten spoób '->' ")
print("Równoważność umieść jako jedno w ten sposób '<->' ")
print("Alternatywę umieść jako 'v' ")
print("Koniunkcje umieść jako '^' ")
print("Aby zakonczyc dodawani wprowadź '?'")

while working == True:
    wyrazenie.append((input()))
    for j in range(len(zmienne)):
        for i in range(len(wyrazenie)):
            if str(j) == str(wyrazenie[i]):
                wyrazenie[i] = zmienne[j]
    print("wyrażenie teraz wyglada tak", wyrazenie)

    for i in range(len(wyrazenie)):
        if wyrazenie[i] == "?":
            wyrazenie.pop(i)
            working = False

for j in range(len(wyrazenie)):
    if wyrazenie[j] == "->":
        implikacje.append(j)

for j in range(len(wyrazenie)):
    if wyrazenie[j] == "<->":
        rownowaznosci.append(j)

for j in range(len(wyrazenie)):
    if wyrazenie[j] == "^":
        koniunkcje.append(j)

for j in range(len(wyrazenie)):
    if wyrazenie[j] == "v":
        alternatywy.append(j)

for j in range(len(wyrazenie)):
    if wyrazenie[j] == "~":
        negacje.append(j)


if len(implikacje) != 0:
    wyrazenie.insert(implikacje[0]-1, "~")
    wyrazenie[implikacje[0]+1] = " v "
    implikacje.pop(0)
    for j in range(len(zmienne)):
        for i in range(len(wyrazenie)):
            if str(j) == str(wyrazenie[i]):
                wyrazenie[i] = zmienne[j]
    print("wyrażenie teraz wyglada tak", wyrazenie)



if len(rownowaznosci) != 0:
    if wyrazenie[0] or wyrazenie[2] != "~":
        rowno = ["(", "~", wyrazenie[0], "v", wyrazenie[2], ")", "^", "(", "~", wyrazenie[2], "v", wyrazenie[0], ")" ]
        wyrazenie = rowno
        print(wyrazenie)
    elif wyrazenie[0] == "~":
        rowno = ["(", "~", wyrazenie[1], "v", wyrazenie[2], ")", "^", "(", "~", wyrazenie[2], "v", wyrazenie[1], ")"]
        wyrazenie = rowno
        print(wyrazenie)
    elif wyrazenie[2] == "~":
        rowno = ["(", "~", wyrazenie[0], "v", wyrazenie[3], ")", "^", "(", "~", wyrazenie[3], "v", wyrazenie[0], ")"]
        wyrazenie = rowno
        print(wyrazenie)


if len(negacje) != 0:
    li = list(zmienne[0])
    for i in range(len(li)):
        if li[i] == '^':
            print(li)
            li[i] = "v"
            li.insert(i-1, "~")
            print(li)

            li.insert(i+2, "~")
            for i in range(len(li)):
                if li[i] == "~" and li[i+1] == "~":
                    li.remove(li[i+1])
                    li.remove((li[i]))
            print(li)
            break

        elif li[i] == 'v':
            li[i] = "^"
            li.insert(i-1, "~")
            li.insert(i+2, "~")
            for i in range(len(li)):
                if li[i] == "~" and li[i+1] == "~":
                    li.remove(li[i+1])
                    li.remove((li[i]))
            print(li)

            break



for i in range(wyrazenie):
    if wyrazenie[i] == "~" and wyrazenie[i+1] == "~":
        wyrazenie.remove(wyrazenie[i+1])
        wyrazenie.remove((wyrazenie[i]))

