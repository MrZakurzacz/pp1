temp_c = "a"
while type(temp_c) not in (float, int):
    temp_c = input("Podaj temperaturę, w stopniach Celsjusza: ")
    try:
        temp_c = float(temp_c)
    except ValueError:
        print("To nie jest poprawna temperatura. Spróbuj ponownie.")
temp_f = 32 + 9/5*temp_c
print(f"Temperature w stopniach Fahrenheita wynosi: {temp_f}")