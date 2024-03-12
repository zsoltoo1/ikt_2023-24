# 1.
print("For ciklus:")
osszeg = 0
for i in range(1, 1001, 26):
    print(i, end=", ")
    osszeg += i
print("\nAz összeg:", osszeg, "\n")

# 2.
print("While ciklus:")
# 2. while ciklussal
osszeg = 0
i = 1
while i <= 1000:
    print(i, end=", ")
    osszeg += i
    i += 26
print("\nAz összeg:", osszeg, "\n")
