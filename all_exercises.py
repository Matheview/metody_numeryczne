# coding=utf-8
import sys


def horner2(wsp, st, arg):
    result = ''
    if st == 0:
        wynik = wsp[st]
    else:
        wynik = wsp[st]
        result += str(wynik) + "x^" + str(st-1)
        for i in range(st, 1, -1):
            wynik = wynik * arg + wsp[i-1]
            if wynik >= 0:
                result += "+"
            if i-2 == 1:
                result += str(wynik) + "x"
            if i-2 == 0:
                result += str(wynik)
            if i-2 > 1:
                result += str(wynik) + "x^" + str(i-2)
        wynik = wynik * arg + wsp[0]
    return "Q(x) = {}\nWartość wielomianu w punkcie {} wynosi: {}\n".format(result, arg, wynik)


def schemat_hornera():
    wspol = []
    arg = 0
    stop = int(input("Podaj stopień wielomianu: "))
    for i in range(int(stop) + 1):
        wspol.append(int(input("Podaj wspolczynnik przy potedze {0}: ".format(i))))
    if stop != 0:
        arg = int(input("Podaj argument: "))
    return horner2(wspol, stop, arg)


def newton(values, pkts):
    if pkts == 2:
        result = values[1]-values[0]
        if result < 0:
            return "N{}(x) = {} {}(x-0)\n".format(pkts, values[0], result)
        else:
            return "N{}(x) = {} + {}(x-0)\n".format(pkts, values[0], result)
    if pkts > 2:
        results = []
        datamatrix = []
        for _ in range(pkts):
            datamatrix.append([0] * pkts)
        datamatrix[0][0] = values[1] - values[0]
        results.append(datamatrix[0][0])
        for i in range(1, pkts-1):
            for j in range(i+1):
                if j == 0:
                    datamatrix[i][j] = values[i+1] - values[i]
                else:
                    datamatrix[i][j] = (datamatrix[i][j-1] - datamatrix[i-1][j-1]) / (j+1)
                if i == j:
                    results.append(datamatrix[i][j])
        wzor = "N{}(x) = {}".format(pkts, values[0])
        for i in range(pkts-1):
            if results[i] == 0:
                pass
            else:
                if results[i] == 1:
                    wzor += "+" + str(results[i])
                    for j in range(i + 1):
                        wzor += "(x-{})".format(j)
                    if i == pkts - 2:
                        break
                elif results[i] == -1:
                    wzor += str(results[i])
                    for j in range(i + 1):
                        wzor += "(x-{})".format(j)
                    if i == pkts - 2:
                        break
                else:
                    if results[i] < 0:
                        wzor += str(results[i])
                    else:
                        wzor += "+" + str(results[i])
                    for j in range(i+1):
                        wzor += "(x-{})".format(j)
                    if i == pkts-2:
                        break
        return wzor+"\n"
    else:
        return "Wprowadzono niewłasciwe dane"


def interpolacja_newtona():
    values = []
    pkts = int(input("Podaj ilość punktów x (od 0 do n): "))
    if int(pkts) < 2:
        return "Zbyt mała liczba punktów"
    else:
        for i in range(pkts):
            values.append(int(input("Podaj wartość fx(x{0}): ".format(i))))
        return newton(values, pkts)


def metoda_stycznej():
    return "Metoda jeszcze nie gotowa\n"


def kwadratura():
    return "Metoda jeszcze nie gotowa\n"


def main():
    while True:
        choose = input("""Wybierz metodę:
  1. schemat Hornera
  2. interpolacja Netwon'a
  3. metoda stycznej
  4. kwadratura
  9. Wyjście\n""")
        if choose == '1':
            print(schemat_hornera())
            choose = ''
        if choose == '2':
            print(interpolacja_newtona())
            choose = ''
        if choose == '3':
            print(metoda_stycznej())
            choose = ''
        if choose == '4':
            print(kwadratura())
            choose = ''
        if choose == '9':
            sys.exit(0)
        if choose != '':
            print("Nieprawidłowy wybór")


if __name__ == "__main__":
    main()
