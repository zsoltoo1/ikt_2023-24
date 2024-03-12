szam = input("Adj meg egy számot: ")
szam = int(szam)
szam1 = input("Adj meg még egy számot: ")
szam1 = int(szam1)
if szam > szam1:
    print(f"{szam} nagyobb ennyivel: {szam - szam1}")
elif szam1 > szam:
    print(f"{szam1} nagyobb ennyivel: {szam1 - szam}")
else:
    print(f"A két szám egyenlő!")