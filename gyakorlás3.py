N = int(input("Kérem adja meg az N számot: "))
M = int(input("Kérem adja meg az M számot: "))

if N > M:
    print("N-nek nagyobbnak kell lennie, mint M-nek.")
else:
    for szam in range(N, M + 1):
        print(szam)