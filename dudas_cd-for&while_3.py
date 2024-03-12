# 1.
print("For ciklus:")
kezdo = int(input("Kérem a kezdőértéket: "))
veg = int(input("Kérem a végértéket: "))

print("Növekvő sorrend:")
for i in range(kezdo, veg + 1):
    print(i, end=", ")
print("\nCsökkenő sorrend:")
for i in range(veg, kezdo - 1, -1):
    print(i, end=", ")
print("\n")

# 2.
print("While ciklus:")
# 2. while ciklussal
kezdo = int(input("Kérem a kezdőértéket: "))
veg = int(input("Kérem a végértéket: "))

print("Növekvő sorrend:")
i = kezdo
while i <= veg:
    print(i, end=", ")
    i += 1
print("\nCsökkenő sorrend:")
i = veg
while i >= kezdo:
    print(i, end=", ")
    i -= 1
print("\n")
