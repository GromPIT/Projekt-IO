import random, datetime

# komentarz Marysi
# komentarz
# ZAKRES_MIN i ZAKRES_MAX oznaczają przedział z którego losujemy
# ILE_LICZB oznacza ilość liczb, którą losujemy
ZAKRES_MIN = 0
ZAKRES_MAX = 100
ILE_LICZB = 10000

# generowanie tablicy (listy) liczb losowych w zadanym zakresie i ilości
def generujLiczbyLosowe():
    listaLiczb = []

    for i in range(ILE_LICZB):
        listaLiczb.append(random.randint(ZAKRES_MIN, ZAKRES_MAX))

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
                listaLiczb[i], listaLiczb[i+1] = listaLiczb[i+1], listaLiczb[i]

    return listaLiczb

# Piter
# Heap sort
def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]
    pass

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
            listaLiczb[i], listaLiczb[j] = listaLiczb[j], listaLiczb[i]
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

def main():
    # wyniki - słownik, który będzie zawierał pomiary czasu poszczególnych algorytmów (pary: nazwa - czas)
    wyniki = {}


    listaLiczb = generujLiczbyLosowe()
    print(listaLiczb)

    # sortowanie bąbelkowe
    listaBubel = listaLiczb.copy()
    print("Sortowanie bąbelkowe")
    czas_start = datetime.datetime.now()
    posortowane = bubelSort(listaBubel)
    czas_stop = datetime.datetime.now()
    wyniki['Sortowanie bąbelkowe'] = czas_stop - czas_start

    print()
    print(posortowane)

    # sortowanie szybkie
    listaQuick = listaLiczb.copy()
    print("Sortowanie szybkie")
    czas_start = datetime.datetime.now()
    posortowane = quickSort(listaQuick, 0, len(listaQuick) - 1)
    czas_stop = datetime.datetime.now()
    wyniki['Sortowanie szybkie'] = czas_stop - czas_start

    print()
    print(posortowane)

    # sortowanie kopcowe
    listaQuick = listaLiczb.copy()
    print("Sortowanie kopcowe")
    czas_start = datetime.datetime.now()
    posortowane = heapSort(listaQuick)
    czas_stop = datetime.datetime.now()
    wyniki['Sortowanie kopcowe'] = czas_stop - czas_start

    print()
    print(posortowane)


    # wbudowana w pythona metoda sorted
    listaSorted = listaLiczb.copy()
    print("Sortowanie ""sorted")
    czas_start = datetime.datetime.now()
    posortowane = sorted(listaSorted)
    czas_stop = datetime.datetime.now()
    wyniki['Sorted'] = czas_stop - czas_start

    print()
    print(posortowane)

    # wyświetlenie wyników - na razie dirty
    print(wyniki)
    return

if __name__ == "__main__":
    main()
