import random

veletlenszam = random.randint(1, 3)

felhasznalo_szam = int(input("Kérem adjon meg egy számot 1 és 3 között: "))

if felhasznalo_szam == veletlenszam:
    print("Gratulálok, eltaláltad a számot!")
else:
    print("Sajnos nem találtad el a számot. A generált szám:", veletlenszam)