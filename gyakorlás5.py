osszeg = 0
szamok_szama = 0

for szam in range(1, 2021):
    osszeg += szam
    szamok_szama += 1

átlag = osszeg / szamok_szama

print("Az 1-től 2020-ig terjedő számok átlaga:", átlag)