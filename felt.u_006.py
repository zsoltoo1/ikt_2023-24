szam = int(input("Adjon meg egy egész számot: "))

if szam % 3 == 0 and szam % 4 == 0:
    print("A szám 3-mal és 4-gyel is osztható.")
elif szam % 3 == 0:
    print("A szám csak 3-mal osztható.")
elif szam % 4 == 0:
    print("A szám csak 4-gyel osztható.")
else:
    print("A szám sem 3-mal, sem 4-gyel nem osztható.")