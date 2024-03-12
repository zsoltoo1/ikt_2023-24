import random

gondolt_szám = random.randint(1,6)
kitalálta = False
while not kitalálta:
    tipp = int(input('Szerinted?'))
    print("Próbáld újra!")
    if tipp == gondolt_szám:
        kitalálta = True
        print("Ügyes!")