def negyzet_kerulet(oldal):
    return 4 * oldal

def negyzet_terulet(oldal):
    return oldal ** 2

def main_negyzet():
    oldal = float(input("Kérem, adja meg a négyzet oldalhosszát: "))
    while oldal <= 0:
        oldal = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
    kerulet = negyzet_kerulet(oldal)
    terulet = negyzet_terulet(oldal)
    print("A négyzet kerülete:", kerulet)
    print("A négyzet területe:", terulet)

main_negyzet()