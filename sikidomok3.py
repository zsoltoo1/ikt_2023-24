def haromszog_terulet(alap, magassag):
    return 0.5 * alap * magassag

def main_haromszog():
    alap = float(input("Kérem, adja meg a háromszög alapját: "))
    while alap <= 0:
        alap = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
    magassag = float(input("Kérem, adja meg a háromszög magasságát: "))
    while magassag <= 0:
        magassag = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
    terulet = haromszog_terulet(alap, magassag)
    print("A háromszög területe:", terulet)

main_haromszog()