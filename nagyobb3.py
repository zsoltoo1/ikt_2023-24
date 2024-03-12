óra = int(input('Hány óra van most?'))
if 8 <= óra < 16:
    print("A bolt nyitva van.")
    print("Ennyi órád van még odaérni:", 16 - óra)
else:
    print("A bolt zárva van.")    