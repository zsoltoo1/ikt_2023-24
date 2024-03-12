def teglalap_kerulet(a, b):
    return 2 * (a + b)

def teglalap_terulet(a, b):
    return a * b

def main_teglalap():
    a = float(input("Kérem, adja meg a téglalap egyik oldalát: "))
    while a <= 0:
        a = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
    b = float(input("Kérem, adja meg a téglalap másik oldalát: "))
    while b <= 0:
        b = float(input("A megadott érték nem pozitív! Kérem, adjon meg egy pozitív számot: "))
    kerulet = teglalap_kerulet(a, b)
    terulet = teglalap_terulet(a, b)
    print("A téglalap kerülete:", kerulet)
    print("A téglalap területe:", terulet)

main_teglalap()