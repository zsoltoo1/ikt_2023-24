import math

def heron_formula(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
        return True

def triangle_type(a, b, c):
    if a== b == c:
        return "egyenlő oldalú"
    elif a == b or a == c or b == c:
        return "egyenlő szárú"
    else:
        return "általános"

def main():
    a = float(input("Adja meg az első oldal hosszát: "))
    b = float(input("Adja meg a második oldal hosszát: "))
    c = float(input("Adja meg a harmadik oldal hosszát: "))

    if is_triangle(a, b, c):
        area = heron_formula(a, b, c)
        perimeter = a + b + c
        print("A háromszög területe:", format(area, '.2f'))
        print("A háromszög kerülete:", format(perimeter, '.2f'))
        print("A háromszög típusa:", triangle_type(a, b, c))

if __name__ == "__main__":
    main()