szo1 = input(f"Adj meg egy szót!:")
szo2 = input(f"Adj meg egy másik szót!:")
if len(szo1) > len(szo2):
    print(f"A hosszab szó:{szo1}")
elif len(szo1) < len(szo2):
    print(f"A hosszab szó:{szo2}")
else:
    print(f"A két szó egforma hosszú")