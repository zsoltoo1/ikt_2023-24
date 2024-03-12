import math

def kor_kerulet(sugar):
    return 2 * math.pi * sugar

def kor_terulet(sugar):
    return math.pi * sugar ** 2

def main_kor():
    beirt = input("Kérem, adja meg a kör sugárát (s) vagy átmérőjét (a): ").lower()
    while beirt not in ['s', 'a']:
        beirt = input("Nem megfelelő bemenet! Kérem, adja meg a kör sugárát (s) vagy átmérőjét (a): ").lower()
    if beirt == 's':
        sugar = float(input("Kérem, adja meg a kör sugárát: "))
    elif beirt == 'a':
        atmero = float(input("Kérem, adja meg a kör átmérőjét: "))
        while atmero <= 0:
            atmero = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
        sugar = atmero / 2
    kerulet = kor_kerulet(sugar)
    terulet = kor_terulet(sugar)
    print("A kör kerülete:", kerulet)
    print("A kör területe:", terulet)

main_kor()