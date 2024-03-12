import random

felhasznalo_valasztas = input("Kérlek válassz fejet (F) vagy írást (Í): ")

veletlen_eredmeny = random.choice(["fej", "írás"])

if felhasznalo_valasztas.lower() == veletlen_eredmeny[0].lower():
    print("Gratulálok, eltaláltad!")
else:
    print("Sajnos nem találtad el. Az eredmény:", veletlen_eredmeny)