szam = input("Adjon meg egy számot 1-7 között: ")
szam = int(szam)
if szam == 1:
    print(f"Hétfő")
elif szam == 2:
    print(f"Kedd")
elif szam == 3:
    print(f"Szerda")
elif szam == 4:
    print(f"Csütörtök")
elif szam == 5:
    print(f"Péntek")
elif szam == 6:
    print(f"Szombat")
elif szam == 7:
    print(f"Vasárnap")
else:
    print(f"1-7 közötti számot kérek!")