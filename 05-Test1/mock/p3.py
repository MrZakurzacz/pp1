def f(name):
    name = list(name)
    acronym = ""

    for num,i in enumerate(name):   # użycie funkcji enumerate ułatwia życie, bo tak można w łatwy sposób wziąć znak występujący po spacji

        if num == 0:                # jeśli sprawdzana litera jest pierwszą literą
            acronym += i            # zapisze ją do acronym

        if i == " ":                # jeśli występuje spacja
            acronym += name[num+1]  # weźmie następny znak z tekstu i doda go do str o nazwie acronym
                                    # 1 jest dodane do num, ponieważ num ma index sprawdzanej wartości
                                    # bez dodania 1 do acronym została dodana by spacja

    return acronym                  # zwrócenie akronimu