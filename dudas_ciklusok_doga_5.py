osszeg = 0
db = 0

while True:
    szam = float(input("Kérem, adjon meg egy számot (0 vége): "))
    
    if szam == 0:
        break  # Kilépés a ciklusból, ha a felhasználó 0-t adott meg
    
    osszeg += szam
    db += 1

if db > 0:
    atlag = osszeg / db
    print(f"A megadott számok összege: {osszeg}")
    print(f"A megadott számok átlaga: {atlag}")
else:
    print("Nem adott meg számot.")
