def cselekves_kepesseg(eletkor):
    if eletkor < 14:
        print("Cselekvőképtelen")
    elif 14 <= eletkor <= 18:
        print("Korlátozottan cselekvőképes")
    else:
        print("Nagykorú")

try:
    eletkor = int(input("Kérem az életkorát: "))
    cselekves_kepesseg(eletkor)
except ValueError:
    print("Hibás bemenet! Kérem adjon meg egy érvényes egész számot.")
