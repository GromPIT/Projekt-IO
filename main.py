import random

# ZAKRES_MIN i ZAKRES_MAX oznaczają przedział z którego losujemy
# ILE_LICZB oznacza ilość liczb, którą losujemy
ZAKRES_MIN = 0
ZAKRES_MAX = 100
ILE_LICZB = 100

def generujLiczbyLosowe():
    listaLiczb = []

    for i in range(ILE_LICZB):
        listaLiczb.append(random.randint(ZAKRES_MIN, ZAKRES_MAX))

    return listaLiczb

def main():
    listaLiczb = generujLiczbyLosowe()
    print(listaLiczb)

    return

if __name__ == "__main__":
    main()
