nev = input("Adja meg a nevét: ")
kor = input("Adja meg a korát: ")
kor = int(kor)
if kor > 0 and kor < 3:
    print(f"A legfiatalabb kiskorú!")
elif kor > 4 and kor < 6:
    print(f"Óvodás korban van!")
elif kor > 7 and kor < 18:
    print(f"Érettségi előtt álló ifjú!")
elif kor > 19 and kor < 25:
    print(f"Egyetemista vagy ifjú munkavállaló!")
elif kor > 26 and kor < 65:
    print(f"Aktív dolgozó ember!")
elif kor > 66 and kor < 100:
    print(f"Megérdemelt nyugdíjas éveit élvezi!")
elif kor > 100:
    print("Ritka, mint a fehér holló!")
