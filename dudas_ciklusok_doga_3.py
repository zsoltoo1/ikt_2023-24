#Kezdőérték beolvasása
kezdőérték = int(input("Kérem, adja meg a kezdőértéket: "))

#Végérték beolvasása
végérték = int(input("Kérem, adja meg a végértéket: "))

#Növekvő sorrendben kiírás
print("Növekvő sorrend:")
for szam in range(kezdőérték, végérték + 1):
    print(szam, end=', ')

#Csökkenő sorrendben kiírás
print("\nCsökkenő sorrend:")
for szam in range(végérték, kezdőérték - 1, -1):
    print(szam, end=', ')