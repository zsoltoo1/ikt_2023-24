import random
 
  szam = random.randint(0, 5)
  print(f'A generált szám: {szam}')  
 
  if szam > 0:
    print('A szám pozitív.')
  elif szam % 2 == 0:
    print('A szám páros.')