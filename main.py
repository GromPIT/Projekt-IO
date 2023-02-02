import random, datetime, re

# komentarz Marysi
# komentarz
# ZAKRES_MIN i ZAKRES_MAX oznaczają przedział z którego losujemy

# zastąpione funkcją
# ILE_LICZB oznacza ilość liczb, którą losujemy
# ZAKRES_MIN = 0
# ZAKRES_MAX = 100
# ILE_LICZB = 10

# zamiana liczb
def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]
    return


# generowanie tablicy (listy) liczb losowych w zadanym zakresie i ilości
def generujLiczbyLosowe(min, max, count):
    listaLiczb = []

    for i in range(count):
        listaLiczb.append(random.randint(min, max))

    return listaLiczb

# Merge-sort Marysia
# ...


# sortowanie bąbelkowe
def bubelSort(listaLiczb):
    zamiana = True
    while (zamiana):
        # optymistycznie
        zamiana = False
        for i in range(len(listaLiczb)-1):
            if listaLiczb[i] > listaLiczb[i+1]:
                zamiana = True
                swap(listaLiczb, i, i+1)

    return listaLiczb

def bubelSort_v2(listaLiczb):
    zamiana = True
    j = 0
    while (zamiana):
        # optymistycznie
        zamiana = False
        for i in range(len(listaLiczb)-1-j):
            if listaLiczb[i] > listaLiczb[i+1]:
                zamiana = True
                swap(listaLiczb, i, i+1)
        j += 1

    return listaLiczb

# sortowanie koktajlowe
def koktajlSort(listaLiczb):
    zamiana = True
    min = 0
    max = len(listaLiczb) - 1

    while zamiana:
        zamiana = False
        for i in range(max):
            if listaLiczb[i] > listaLiczb[i+1]:
                swap(listaLiczb, i, i+1)
                zamiana = True
        max -= 1

        for i in range(max, min, -1):
            if listaLiczb[i] < listaLiczb[i -1]:
                swap(listaLiczb, i-1, i)
                zamiana = True
        min += 1

    return listaLiczb

def grzebienSort(listaLiczb):
    ile = rozpietosc = len(listaLiczb)
    zamiana = True

    while rozpietosc > 1 or zamiana:
        # współczynnik rozpiętości 1,3 jest wyznaczony empirycznie przez twórców algorytmu
        rozpietosc = int(rozpietosc * 10 // 13)
        # print("R:",rozpietosc)
        if rozpietosc == 0:
            rozpietosc = 1
        zamiana = False
        i = 0
        while i + rozpietosc < ile:
            # print(i + rozpietosc)

            if listaLiczb[i] > listaLiczb[i + rozpietosc]:
                swap(listaLiczb, i, i + rozpietosc)
                zamiana = True
            i += 1
    return listaLiczb

# insertSort
def insertSort(listaLiczb):
    ile = len(listaLiczb)

    for j in range(ile-2, -1, -1):
        pom = listaLiczb[j]
        i = j + 1
        while i < ile and pom > listaLiczb[i]:
            listaLiczb[i - 1] = listaLiczb[i]
            i += 1
        listaLiczb[i-1] = pom

    return listaLiczb

# Piter
# Heap sort

def shiftDown(lista, i, upper):
    while True:
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            # 2 children
            if lista[i] >= max(lista[l], lista[r]):
                break
            elif lista[l] > lista[r]:
                swap(lista, i, l)
                i = l
            else:
                swap(lista, i, r)
                i = r
        elif l < upper:
            if lista[l] > lista[i]:
                swap(lista, i, l)
                i = l
            else:
                break
        elif r < upper:
            if lista[r] > lista[i]:
                swap(lista, i, r)
                i = r
            else:
                break
        else:
            break

def heapSort(lista):
    for j in range((len(lista)-2) // 2, -1, -1):
        shiftDown(lista, j, len(lista))
    for end in range(len(lista) - 1, 0, -1):
        swap(lista, 0, end)
        shiftDown(lista, 0, end)

    return lista

def quickSort(listaLiczb, lewy_indeks, prawy_indeks):
    i = lewy_indeks
    j = prawy_indeks
    # punkt podziału, tzw. pivot
    pivot = listaLiczb[(lewy_indeks + prawy_indeks) // 2]

    while True:
        # szukaj elementu większego niż pivot po lewej stronie tablicy
        while listaLiczb[i] < pivot:
            # przesuń indeks
            i += 1
        # szukaj elemetnu mniejszego niż pivot po prawej stronie tablicy
        while listaLiczb[j] > pivot:
            # przesuń indeks
            j -= 1
        # jeśli liczniki się nie minęły, wykonaj zamianę - jednocześnie załatwia
        # warunek wyjścia przy jednoelementowej tablicy po podziale
        if i <= j:
            # zamień liczby
            swap(listaLiczb, i, j)
            i += 1
            j -= 1
        else:
            break
    # wywołanie rekurencyjne dla obu przedziałów
    if lewy_indeks < j:
        quickSort(listaLiczb, lewy_indeks, j)
    if prawy_indeks > i:
        quickSort(listaLiczb, i, prawy_indeks)

    return listaLiczb

def winieta():
    print("""
                    *---------------------------------------------------*
                    |  PROGRAM: Porównanie metod sortowania wersja 1.0  |
                    *---------------------------------------------------*
                    |                     Autorzy :                     |
                    |                Piotr M. Garczyński                |
                    |                   Jacek Borowski                  |
                    |                   Maria Orzeszko                  |
                    *---------------------------------------------------*
                """)
    print("------------------------------------------------------------------------")
    print("OPIS:")
    print("\nProgram generuje tablicę liczb losowych, a następnie sortuje ją według")
    print("kilku algorytmów sortowania, czynność powtarzana jest zadaną ilość razy, ")
    print("a na końcu wyświetlany jest uśredniony wynik czasu wykonania")
    print("------------------------------------------------------------------------")

    return

def pobierzLiczbeCalkowita(text):
    isOk = False

    while not isOk:
        liczba = input(text)
        reg = re.compile("^[0-9]*$")
        if not reg.match(liczba):
            print("Wprowadzono niepoprawną liczbę. Spróbuj ponownie\n")
        else:
            isOk = True

    return liczba

def sortowanie(min, max, count, repeat):
    # wyniki - słownik, który będzie zawierał pomiary czasu poszczególnych algorytmów (pary: nazwa - czas)
    wyniki = {}
    print()
    for i in range(repeat):
        listaLiczb = generujLiczbyLosowe(min, max, count)
        print(f"Iteracja nr {i+1}: wygenerowano liczby \u007b")
        # print(f"{listaLiczb}")

        # wbudowana w pythona metoda sorted - JB
        print("\tSortowanie wbudowaną metodą \"sorted\"... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = sorted(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sorted' in dict(wyniki):
            wyniki['Sorted'] += czas_stop - czas_start
        else:
            wyniki['Sorted'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        # sortowanie bąbelkowe - PMG
        print("\tSortowanie bąbelkowe v1... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = bubelSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie bąbelkowe' in dict(wyniki):
            wyniki['Sortowanie bąbelkowe'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie bąbelkowe'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        # sortowanie bąbelkowe v2 - PMG
        print("\tSortowanie bąbelkowe v2... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = bubelSort_v2(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie bąbelkowe v2' in dict(wyniki):
            wyniki['Sortowanie bąbelkowe v2'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie bąbelkowe v2'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        # sortowanie koktajlowe - PMG
        print("\tSortowanie koktajlowe... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = koktajlSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie koktajlowe' in dict(wyniki):
            wyniki['Sortowanie koktajlowe'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie koktajlowe'] = czas_stop - czas_start
        print("DONE!")

        # sortowanie grzebieniowe  - PMG
        print("\tSortowanie grzebieniowe... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = grzebienSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie grzebieniowe' in dict(wyniki):
            wyniki['Sortowanie grzebieniowe'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie grzebieniowe'] = czas_stop - czas_start
        print("DONE!")

        # sortowanie przez wstawianie - PMG
        print("\tSortowanie przez wstawianie... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = grzebienSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie przez wstawianie' in dict(wyniki):
            wyniki['Sortowanie przez wstawianie'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie przez wstawianie'] = czas_stop - czas_start
        print("DONE!")

        # sortowanie szybkie - PMG
        print("\tSortowanie szybkie... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = quickSort(listaLiczb.copy(), 0, len(listaLiczb) - 1)
        czas_stop = datetime.datetime.now()
        if 'Sortowanie szybkie' in dict(wyniki):
            wyniki['Sortowanie szybkie'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie szybkie'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        # sortowanie kopcowe - PMG
        print("\tSortowanie kopcowe... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = heapSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie kopcowe' in dict(wyniki):
            wyniki['Sortowanie kopcowe'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie kopcowe'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")
        print("}\n")

    print(wyniki)

    wyniki['Sorted'] /= repeat
    wyniki['Sortowanie bąbelkowe'] /= repeat
    wyniki['Sortowanie bąbelkowe v2'] /= repeat
    wyniki['Sortowanie koktajlowe'] /= repeat
    wyniki['Sortowanie grzebieniowe'] /= repeat
    wyniki['Sortowanie przez wstawianie'] /= repeat
    wyniki['Sortowanie kopcowe'] /= repeat
    wyniki['Sortowanie szybkie'] /= repeat

    print(wyniki)


    return


def main():

    winieta()
    min = pobierzLiczbeCalkowita("Podaj dolny zakres tablicy: ")
    max = pobierzLiczbeCalkowita("Podaj górny zakres tablicy: ")
    count = pobierzLiczbeCalkowita("Podaj ilość liczb do losowania (sensowna czasowo ilość 10 000): ")
    repeat = pobierzLiczbeCalkowita("Podaj ilość powtórzeń (zalecane przynajmniej 5): ")
    sortowanie(int(min), int(max), int(count), int(repeat))

    # for i in range(10, -1, -1):
    #     print(i)
    #
    # min = 0
    # max = 10
    # count = 10
    #
    # lista = generujLiczbyLosowe(min, max, count)
    # print(lista)
    # sort = insertSort(lista)
    # print(sort)

    # listaLiczb = generujLiczbyLosowe()
    #
    #

    # print()
    # print(posortowane)
    #

    #
    # print()
    # print(posortowane)
    #
    # # sortowanie kopcowe

    #
    # print()
    # print(posortowane)
    #
    #
    # # wbudowana w pythona metoda sorted
    # listaSorted = listaLiczb.copy()
    # print("Sortowanie ""sorted")
    # czas_start = datetime.datetime.now()
    # posortowane = sorted(listaSorted)
    # czas_stop = datetime.datetime.now()
    # wyniki['Sorted'] = czas_stop - czas_start
    #
    # print()
    # print(posortowane)
    #
    # # wyświetlenie wyników - na razie dirty
    # print(wyniki)
    return

if __name__ == "__main__":
    main()
