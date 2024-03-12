osszeg = 0
for szam in range(1, 1001, 26):
    print(szam, end=', ')
    osszeg += szam
print("\Az összeg:", osszeg)