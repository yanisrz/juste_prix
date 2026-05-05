import random
prix = random.randint(1, 50)

devine=""

compteur: int = 0
print(prix)
while devine != prix:
    compteur += 1
    devine = input("devine le prix entre 1 et 50: ")
    if devine.isdigit() == False:
        print("!!ce n'est pas un nombre, essaye encore!!😡")
        devine = input("reesaie: ")
        continue
    devine = int(devine)
    if devine < prix:
        print("c'est trop petit choisi un nombre plus grand")
    elif devine > prix:
        print("c'est trop grand choisi un nombre plus petit")
    
print(f"bravo tu as trouve le prix en {compteur} tentatives!")
    
   


