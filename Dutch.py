def ini():
    for i in range(liczba_graczy):
        x = input("Podaj liczbe punktów ")
        x = int(x)
        tab.append(x)
    return tab


def koniec_gry():
    for i in range(liczba_graczy):
        if tab[i] >= 100:
            print(gracz)
            print(tab)
            return True
    else:
        return False


def suma():
    while not koniec_gry():
        print(gracz)
        for i in range(liczba_graczy):
            x = input("Podaj liczbe punktów ")
            x = int(x)
            tab[i] = tab[i] + x
        print(tab)
    return tab


def gracze():
    for i in range(liczba_graczy):
        imie = input("Podaj imie ")
        gracz.append(imie)
    return gracz


liczba_graczy = input("Ilu jest graczy ")
liczba_graczy = int(liczba_graczy)
tab = [] * liczba_graczy
gracz = []

gracze()
print(ini())
suma()
