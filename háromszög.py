def is_derékszögű(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def main():
    a = float(input("1. oldal: "))
    b = float(input("2. oldal: "))
    c = float(input("3. oldal: "))

    if is_derékszögű(a, b, c):
        print("Derékszögű háromszög.")
    else:
        print("Nem derékszögű háromszög.")

if __name__ == "__main__":
    main()