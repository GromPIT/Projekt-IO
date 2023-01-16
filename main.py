import random

# ZAKRES_MIN i ZAKRES_MAX oznaczają przedział z którego losujemy
# ILE_LICZB oznacza ilość liczb, którą losujemy
ZAKRES_MIN = 0
ZAKRES_MAX = 1000000
ILE_LICZB = 10000

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
    listaLiczb = generujLiczbyLosowe()
    print(listaLiczb)
    posortowane = bubelSort(listaLiczb)
    print()
    print(posortowane)
    return

if __name__ == "__main__":
    main()
