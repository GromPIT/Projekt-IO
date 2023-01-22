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

    # wyświetlenie wyników - na razie dirty
    print(wyniki)
    return

if __name__ == "__main__":
    main()
