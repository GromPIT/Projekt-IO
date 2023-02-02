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
        print(f"Iteracja nr {i}: wygenerowano liczby \u007b")
        # print(f"{listaLiczb}")

        # wbudowana w pythona metoda sorted - JB
        print("\tSortowanie wbudowaną metodą \"sorted\"...", end='')
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
        print("\tSortowanie bąbelkowe.... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = bubelSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        if 'Sortowanie bąbelkowe' in dict(wyniki):
            wyniki['Sortowanie bąbelkowe'] += czas_stop - czas_start
        else:
            wyniki['Sortowanie bąbelkowe'] = czas_stop - czas_start
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

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
        print("\tSortowanie kopcowe.... ", end='')
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

    return


def main():

    winieta()

    min = pobierzLiczbeCalkowita("Podaj dolny zakres tablicy: ")
    max = pobierzLiczbeCalkowita("Podaj górny zakres tablicy: ")
    count = pobierzLiczbeCalkowita("Podaj ilość liczb do losowania: ")
    repeat = pobierzLiczbeCalkowita("Podaj ilość powtórzeń : ")

    sortowanie(int(min), int(max), int(count), int(repeat))



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
