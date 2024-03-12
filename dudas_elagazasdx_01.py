szam = int(input("Egy egész számot kérek!"))
if szam == 0:
    print(f"A szám {szam} amit megadtál nulla.")
elif szam % 2 == 0:
    print(f"A számod {szam} páros!")
elif szam % 2 == 1:
    print(f"A számod {szam} páratlan!")