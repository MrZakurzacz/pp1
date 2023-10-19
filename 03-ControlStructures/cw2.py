godz, stawka = "a", "a"
while type(godz) not in (float, int):
    godz = input("Podaj liczbę godzin: ")
    try:
        godz = float(godz)
    except ValueError:
        print("Błąd, podaj wartość numeryczną")
while type(stawka) not in (float, int):
    stawka = input("Podaj stawkę godzinową: ")
    try:
        stawka = float(stawka)
    except ValueError:
        print("Błąd, podaj wartość numeryczną")
if godz > 40:
    wynagrodzenie = godz*stawka*1.5
else:
    wynagrodzenie = godz*stawka
print(f"Wynagrodzenie wynosi: {wynagrodzenie}")