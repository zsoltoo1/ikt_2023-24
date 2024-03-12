Henrik = input("Henrik jön ma kosarazni?")
Hanna = input("Hanna jön ma kosarazni?")
if Henrik == "nem" and Hanna == "nem":
    print("Egyikük sem jön kosarazni")    
elif Henrik == "igen" and Hanna == "nem":
    print("Csak egyikük jön kosarazni")
elif Henrik == "nem" and Hanna == "igen":
    print("Csak egyikük jön kosarazni")
elif Henrik == "igen" and Hanna == "igen":
    print("Mindketten jönnek kosarazni")       