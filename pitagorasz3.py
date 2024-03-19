def paros_szam_e(szam):
    return szam % 2 == 0

try:
    szam1 = int(input("Kérem az első számot: "))
    szam2 = int(input("Kérem a második számot: "))
    szam3 = int(input("Kérem a harmadik számot: "))

    eredmenyek = [paros_szam_e(szam1), paros_szam_e(szam2), paros_szam_e(szam3)]

    print("Páros szám vizsgálat alapján:")
    for eredmeny in eredmenyek:
        if eredmeny:
            print("igen")
        else:
            print("nem")
except ValueError:
    print("Hibás bemenet! Kérem adjon meg három érvényes egész számot.")
