def piros_karikas_film(eletkor):
    if eletkor >= 18:
        print("Megtekintheti a „piros karikás” filmet.")
    else:
        print("Nem tekintheti meg a „piros karikás” filmet.")

try:
    eletkor = int(input("Kérem az életkorát: "))
    piros_karikas_film(eletkor)
except ValueError:
    print("Hibás bemenet! Kérem adjon meg egy érvényes egész számot.")
