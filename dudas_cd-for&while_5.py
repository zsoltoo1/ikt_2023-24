# 1.
print("For ciklus:")
osszeg = 0
db = 0

for _ in range(1000):  # Felső határ a biztonság kedvéért
    szam = float(input("Kérek egy számot (0 végjel): "))
    if szam == 0:
        break
    osszeg += szam
    db += 1

if db > 0:
    atlag = osszeg / db
    print("Az összeg:", osszeg)
    print("Az átlag:", atlag)
else:
    print("Nem adtál meg érvényes számot.\n")

# 2. 
print("While ciklus:")
# 2. while ciklussal
osszeg = 0
db = 0

while True:
    szam = float(input("Kérek egy számot (0 végjel): "))
    if szam == 0:
        break
    osszeg += szam
    db += 1

if db > 0:
    atlag = osszeg / db
    print("Az összeg:", osszeg)
    print("Az átlag:", atlag)
else:
    print("Nem adtál meg érvényes számot.\n")
