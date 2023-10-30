def f(number, even):
    number = list(str(number))      # zamienienie number w listę zamiast stringa, ponieważ nie lubię operować na str
    suma = 0

    if even == True:                # jeśli wartość even jest True:
        for i in number:
            if int(i) % 2 == 0:     # jeśli wartość danej cyfry z number jest parzysta czyli podzielna przez 2 z resztą 0
                suma+=int(i)        # dodaj wartość tej liczby do sumy

    else:                           # w przypadku gdy even jest False:
        for i in number:
            if int(i) % 2 != 0:     # jeśli wartość danej cyfry z number jest nieparzysta czyli podzielna przez 2 z resztą różną od 0
                suma+=int(i)        # dodaj wartość tej liczby do sumy

    return suma                     # zwrócenie wartości sumy