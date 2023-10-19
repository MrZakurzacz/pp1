godz = int(input("Podaj liczbę godzin: "))
stawka = int(input("Podaj stawkę godzinową: "))
if godz > 40:
    wynagrodzenie = godz*stawka*1.5
else:
    wynagrodzenie = godz*stawka
print(f"Wynagrodzenie wynosi: {wynagrodzenie}")