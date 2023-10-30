def f(card_number):
    i = 0                               # wartość która przyda nam się żeby wiedzieć w którym miejscu card_number jesteśmy (można też użyć enumerate)
    card_number = list(card_number)     # zamienienie card_number z str na listę, bo nie lubię str

    for a in card_number:

        if i>1 and i<12:                # jeśli sprawdzana liczba jest w indeksie od 2 do 11 (czyli pozycji 3 do 12)
            card_number[i]="*"          # zamień liczbę na pozycji na *
        i+=1                            # podniesienie liczby pozycyjnej

    return("".join(card_number))        # zwrócenie z funkcji str z liczbami w pozycji od 3 do 12 zamienionymi na *
                                        # .join łączy listę w całość do pustego stringa "", ponieważ
                                        # zwracana wartość ma być stringiem