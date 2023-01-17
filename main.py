import random, datetime

# ZAKRES_MIN i ZAKRES_MAX oznaczają przedział z którego losujemy
# ILE_LICZB oznacza ilość liczb, którą losujemy
ZAKRES_MIN = 0
ZAKRES_MAX = 1000000
ILE_LICZB = 1000

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
def generujLiczbyLosowe():
    listaLiczb = []

    for i in range(ILE_LICZB):
        listaLiczb.append(random.randint(ZAKRES_MIN, ZAKRES_MAX))

    return listaLiczb

def main():
    # wyniki - słownik, który będzie zawierał pomiary czasu poszczególnych algorytmów (pary: nazwa - czas)
    wyniki = {}


    listaLiczb = generujLiczbyLosowe()
    print(listaLiczb)

    # sortowanie bąbelkowe
    czas_start = datetime.datetime.now()
    posortowane = bubelSort(listaLiczb)
    czas_stop = datetime.datetime.now()
    wyniki['Sortowanie bąbelkowe'] = czas_stop - czas_start

    print()
    print(posortowane)


    # wyświetlenie wyników - na razie dirty
    print(wyniki)
    return

if __name__ == "__main__":
    main()
