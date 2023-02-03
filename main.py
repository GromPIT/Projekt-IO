import random, datetime, re
from datetime import timedelta
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

# Shell Sort - ulepszony insertSort
def shellSort(listaLiczb):
    ile = len(listaLiczb)
    # wyznaczenie wsp. odstępu zal. od rozmiaru tablicy

    h = 1
    while h < ile:
        h = 3*h + 1
    h //= 9
    if h == 0:
        h = 1
    # print(h)

    while h > 0:
        for j in range(ile - h - 1, -1, -1):
            # print("\t",j)
            pom = listaLiczb[j]
            i = j + h
            while i < ile and pom > listaLiczb[i]:
                listaLiczb[i - h] = listaLiczb[i]
                i += h
            listaLiczb[i - h] = pom
        h //= 3

    print(listaLiczb)

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
        if not reg.match(liczba) or liczba=='':
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
        czas = czas_stop - czas_start
        if 'Sorted' in dict(wyniki):
            wyniki['Sorted']['SUMA'] += czas
            if czas > wyniki['Sorted']['MAX']:
                wyniki['Sorted']['MAX'] = czas
            if czas < wyniki['Sorted']['MIN']:
                wyniki['Sorted']['MIN'] = czas
        else:
            wyniki['Sorted'] = {'SUMA': czas, 'AVG': None, 'MIN':czas, 'MAX':czas}
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        if len(listaLiczb) <= 10000:

            # sortowanie bąbelkowe - PMG
            print("\tSortowanie bąbelkowe v1... ", end='')
            czas_start = datetime.datetime.now()
            posortowane = bubelSort(listaLiczb.copy())
            czas_stop = datetime.datetime.now()
            czas = czas_stop - czas_start
            if 'Sortowanie bąbelkowe' in dict(wyniki):
                wyniki['Sortowanie bąbelkowe']['SUMA'] += czas
                if czas > wyniki['Sortowanie bąbelkowe']['MAX']:
                    wyniki['Sortowanie bąbelkowe']['MAX'] = czas
                if czas < wyniki['Sortowanie bąbelkowe']['MIN']:
                    wyniki['Sortowanie bąbelkowe']['MIN'] = czas
            else:
                wyniki['Sortowanie bąbelkowe'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
            print("DONE!")
            # print(f"Posortowane :\n{posortowane}")

            # sortowanie bąbelkowe v2 - PMG
            print("\tSortowanie bąbelkowe v2... ", end='')
            czas_start = datetime.datetime.now()
            posortowane = bubelSort_v2(listaLiczb.copy())
            czas_stop = datetime.datetime.now()
            czas = czas_stop - czas_start
            if 'Sortowanie bąbelkowe v2' in dict(wyniki):
                wyniki['Sortowanie bąbelkowe v2']['SUMA'] += czas
                if czas > wyniki['Sortowanie bąbelkowe v2']['MAX']:
                    wyniki['Sortowanie bąbelkowe v2']['MAX'] = czas
                if czas < wyniki['Sortowanie bąbelkowe v2']['MIN']:
                    wyniki['Sortowanie bąbelkowe v2']['MIN'] = czas
            else:
                wyniki['Sortowanie bąbelkowe v2'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
            print("DONE!")
            # print(f"Posortowane :\n{posortowane}")

            # sortowanie koktajlowe - PMG
            print("\tSortowanie koktajlowe... ", end='')
            czas_start = datetime.datetime.now()
            posortowane = koktajlSort(listaLiczb.copy())
            czas_stop = datetime.datetime.now()
            czas = czas_stop - czas_start
            if 'Sortowanie koktajlowe' in dict(wyniki):
                wyniki['Sortowanie koktajlowe']['SUMA'] += czas
                if czas > wyniki['Sortowanie koktajlowe']['MAX']:
                    wyniki['Sortowanie koktajlowe']['MAX'] = czas
                if czas < wyniki['Sortowanie koktajlowe']['MIN']:
                    wyniki['Sortowanie koktajlowe']['MIN'] = czas
            else:
                wyniki['Sortowanie koktajlowe'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
            print("DONE!")

        # sortowanie grzebieniowe  - PMG
        print("\tSortowanie grzebieniowe... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = grzebienSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        czas = czas_stop - czas_start
        if 'Sortowanie grzebieniowe' in dict(wyniki):
            wyniki['Sortowanie grzebieniowe']['SUMA'] += czas
            if czas > wyniki['Sortowanie grzebieniowe']['MAX']:
                wyniki['Sortowanie grzebieniowe']['MAX'] = czas
            if czas < wyniki['Sortowanie grzebieniowe']['MIN']:
                wyniki['Sortowanie grzebieniowe']['MIN'] = czas
        else:
            wyniki['Sortowanie grzebieniowe'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
        print("DONE!")

        # sortowanie przez wstawianie - PMG
        print("\tSortowanie przez wstawianie... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = insertSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        czas = czas_stop - czas_start
        if 'Sortowanie przez wstawianie' in dict(wyniki):
            wyniki['Sortowanie przez wstawianie']['SUMA'] += czas
            if czas > wyniki['Sortowanie przez wstawianie']['MAX']:
                wyniki['Sortowanie przez wstawianie']['MAX'] = czas
            if czas < wyniki['Sortowanie przez wstawianie']['MIN']:
                wyniki['Sortowanie przez wstawianie']['MIN'] = czas
        else:
            wyniki['Sortowanie przez wstawianie'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
        print("DONE!")

        # sortowanie metodą Shella - PMG
        print("\tSortowanie metodą Shella... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = shellSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        czas = czas_stop - czas_start
        if 'Sortowanie metodą Shella' in dict(wyniki):
            wyniki['Sortowanie metodą Shella']['SUMA'] += czas
            if czas > wyniki['Sortowanie metodą Shella']['MAX']:
                wyniki['Sortowanie metodą Shella']['MAX'] = czas
            if czas < wyniki['Sortowanie metodą Shella']['MIN']:
                wyniki['Sortowanie metodą Shella']['MIN'] = czas
        else:
            wyniki['Sortowanie metodą Shella'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
        print("DONE!")


        # sortowanie szybkie - PMG
        print("\tSortowanie szybkie... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = quickSort(listaLiczb.copy(), 0, len(listaLiczb) - 1)
        czas_stop = datetime.datetime.now()
        czas = czas_stop - czas_start
        if 'Sortowanie szybkie' in dict(wyniki):
            wyniki['Sortowanie szybkie']['SUMA'] += czas
            if czas > wyniki['Sortowanie szybkie']['MAX']:
                wyniki['Sortowanie szybkie']['MAX'] = czas
            if czas < wyniki['Sortowanie szybkie']['MIN']:
                wyniki['Sortowanie szybkie']['MIN'] = czas
        else:
            wyniki['Sortowanie szybkie'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")

        # sortowanie kopcowe - PMG
        print("\tSortowanie kopcowe... ", end='')
        czas_start = datetime.datetime.now()
        posortowane = heapSort(listaLiczb.copy())
        czas_stop = datetime.datetime.now()
        czas = czas_stop - czas_start
        if 'Sortowanie kopcowe' in dict(wyniki):
            wyniki['Sortowanie kopcowe']['SUMA'] += czas
            if czas > wyniki['Sortowanie kopcowe']['MAX']:
                wyniki['Sortowanie kopcowe']['MAX'] = czas
            if czas < wyniki['Sortowanie kopcowe']['MIN']:
                wyniki['Sortowanie kopcowe']['MIN'] = czas
        else:
            wyniki['Sortowanie kopcowe'] = {'SUMA': czas, 'AVG': None, 'MIN': czas, 'MAX': czas}
        print("DONE!")
        # print(f"Posortowane :\n{posortowane}")
        print("}\n")

    wyniki['Sorted']['AVG'] = wyniki['Sorted']['SUMA'] / repeat
    try:
        wyniki['Sortowanie bąbelkowe']['AVG'] = wyniki['Sortowanie bąbelkowe']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie bąbelkowe v2']['AVG'] = wyniki['Sortowanie bąbelkowe v2']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie koktajlowe']['AVG'] = wyniki['Sortowanie koktajlowe']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie grzebieniowe']['AVG'] = wyniki['Sortowanie grzebieniowe']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie przez wstawianie']['AVG'] = wyniki['Sortowanie przez wstawianie']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie metodą Shella']['AVG'] = wyniki['Sortowanie metodą Shella']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie kopcowe']['AVG'] = wyniki['Sortowanie kopcowe']['SUMA'] / repeat
    except:
        pass

    try:
        wyniki['Sortowanie szybkie']['AVG'] = wyniki['Sortowanie szybkie']['SUMA'] / repeat
    except:
        pass

    wypiszWyniki(wyniki)

    return

def wypiszWyniki(wyniki):
    # wyniki = sorted(wyniki.items(), key='SUMA')
    wyniki = sorted(wyniki.items(), key=lambda x: x[1]['AVG'])
    print("TABELA WYNIKÓW")
    print()
    print('/-------------------------------------------------------------------------------------------------'
          '-------------------------------\\')
    print('|  MIEJSCE  |       METODA SORTOWANIA       |   ŁĄCZNY CZAS  |   ŚREDNI CZAS  |    ROZSTĘP     |    MIN. CZAS   |  MAKS. CZAS    | ')
    print('|-------------------------------------------------------------------------------------------------'
          '-------------------------------|')
    miejsce = 1
    for w, v in wyniki:
        print("| {:^10}| {:30}| {:15}| {:15}| {:15}| {:15}| {:15}|".format(str(miejsce),w, str(v['SUMA']), str(v['AVG']), str(v['MAX'] - v['MIN']), str(v['MIN']), str(v['MAX'])))
        miejsce += 1

    print('\\------------------------------------------------------------------------------------------------'
          '--------------------------------/')

    print()
    input("Naciśnij ENTER...")
    print()
    print("REFLEKSJA... (niezależnie od wyników, zakresów i ilości prób)")
    print()
    print("Można powiedzieć, że algorytm wbudowany w Pythona jest świetnie zoptymalizowany...")
    print("Można powiedzieć, że sortowanie szybkie jest naprawdę bardzo szybkie...")
    print("Można powiedzieć, że sortowanie przez wstawianie ze złożonością O(n^2) jest super wydajne...")
    print()
    print("Jednak niezmiennie od wielu lat sortowanie grzebieniowe robi na mnie zdecydowanie największe wrażenie!")
    print("Nie jest najszybsze. Nie jest najbardziej efektywne... Ale w jego sercu siedzi \"toporne\" sortowanie bąbelkowe")
    print("i pomimo tego stoi niemalże ramię w ramię z teoretycznie znacznie lepszymi i wydajniejszymi algorytmami!")
    print("Algorytmami, których złożoność idzie w logarytmy... a tu taki zonk - istnieje bardzo szybki \"bubel\"-sort :-)")
    print()
    print("A odkrył je... Polak! Pan Włodzimierz Dobosiewicz w 1980 roku :)")
    print()
    print("PMG")
    print()
    input("Naciśnij ENTER...")

    return

def main():

    winieta()
    min = pobierzLiczbeCalkowita("Podaj dolny zakres tablicy: ")
    max = pobierzLiczbeCalkowita("Podaj górny zakres tablicy: ")
    count = pobierzLiczbeCalkowita("Podaj ilość liczb do losowania (sensowna czasowo ilość 10 000): ")
    repeat = pobierzLiczbeCalkowita("Podaj ilość powtórzeń (zalecane przynajmniej 5): ")
    sortowanie(int(min), int(max), int(count), int(repeat))

    return

if __name__ == "__main__":
    main()
