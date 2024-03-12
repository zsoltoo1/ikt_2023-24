def draw_pocak(rows):
    for i in range(1, rows + 1):
        if i <= rows // 2:
            print("O " * i)
        else:
            print("O " * (rows - i + 1))

while True:
    try:
        szam = int(input("Adj meg egy páros számot: "))
        if szam % 2 == 0:
            draw_pocak(szam)
            break  # Kilép a while ciklusból, ha a páros számot megadta a felhasználó
        else:
            print("A megadott szám nem páros. Próbáld újra.")
    except ValueError:
        print("Érvénytelen bemenet. Kérlek, adj meg egy számot.")
