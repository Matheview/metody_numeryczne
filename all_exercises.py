# coding=utf-8
import sys
import math


def horner2(wsp, st, arg):
    result = ''
    if st == 0:
        wynik = wsp[st]
    else:
        wynik = wsp[st]
        if wynik == 1:
            result += "x^" + str(st-1)
        if wynik > 1:
            result += str(wynik) + "x^" + str(st - 1)
        for i in range(st, 1, -1):
            wynik = wynik * arg + wsp[i-1]
            if wynik > 0:
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
        var = int(input("Podaj wspolczynnik przy potedze {0}: ".format(i)))
        while var == 0 and i == int(stop):
            var = int(input("BLAD! Podaj wspolczynnik przy potedze {0}: ".format(i)))
        wspol.append(var)
    if stop != 0:
        arg = int(input("Podaj argument: "))
    return horner2(wspol, stop, arg)


def newton(values, pkts, xses):
    if pkts == 2:
        result = values[1]-values[0]
        if result < 0:
            return "N{}(x) = {} {}(x-{})\n".format(pkts, values[0], result, xses[0])
        else:
            return "N{}(x) = {} + {}(x-{})\n".format(pkts, values[0], result, xses[0])
    if pkts > 2:
        results = []
        datamatrix = []
        for _ in range(pkts):
            datamatrix.append([0] * pkts)
        for i in range(0, pkts-1):
            for j in range(i+1):
                if j == 0:
                    datamatrix[i][j] = (values[i+1] - values[i]) / (xses[i+1]-xses[i])
                else:
                    datamatrix[i][j] = (datamatrix[i][j-1] - datamatrix[i-1][j-1]) / (xses[i+1]-xses[i-j])
                if datamatrix[i][j] - int(datamatrix[i][j]) == 0:
                    datamatrix[i][j] = int(datamatrix[i][j])
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
                        if xses[j] < 0:
                            wzor += "(x+{})".format((xses[j])*(-1))
                        else:
                            wzor += "(x-{})".format(xses[j])
                    if i == pkts - 2:
                        break
                elif results[i] == -1:
                    wzor += str(results[i])
                    for j in range(i + 1):
                        if xses[j] < 0:
                            wzor += "(x+{})".format((xses[j])*(-1))
                        else:
                            wzor += "(x-{})".format(xses[j])
                    if i == pkts - 2:
                        break
                else:
                    if results[i] < 0:
                        wzor += str(results[i])
                    else:
                        wzor += "+" + str(results[i])
                    for j in range(i+1):
                        if xses[j] < 0:
                            wzor += "(x+{})".format((xses[j])*(-1))
                        else:
                            wzor += "(x-{})".format(xses[j])
                    if i == pkts-2:
                        break
        return wzor+"\n"
    else:
        return "Wprowadzono niewłasciwe dane"


def interpolacja_newtona():
    values = []
    xses = []
    pkts = int(input("Podaj ilość punktów x (od 0 do n): "))
    if int(pkts) < 2:
        return "Zbyt mała liczba punktów"
    else:
        for i in range(pkts):
            xses.append(int(input("Podaj wartość x{0}: ".format(i))))
        for i in range(pkts):
            values.append(int(input("Podaj wartość fx(x{0}): ".format(i))))
        return newton(values, pkts, xses)


def kwadratura():
    return "Metoda jeszcze nie gotowa\n"


def main():
    while True:
        choose = input("""Wybierz metodę:
  1. schemat Hornera
  2. interpolacja Netwon'a
  3. kwadratura
  9. Wyjście\n""")
        if choose == '1':
            print(schemat_hornera())
            choose = ''
        if choose == '2':
            print(interpolacja_newtona())
            choose = ''
        if choose == '3':
            print(kwadratura())
            choose = ''
        if choose == '9':
            sys.exit(0)
        if choose != '':
            print("Nieprawidłowy wybór")


if __name__ == "__main__":
    main()
