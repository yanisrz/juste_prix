import random
import time 

niveau = input("     Choisis ton niveau de difficulté (facile = 1, difficile = 2): ")

if niveau == "1":
    prix = random.randint(1, 50)
    grand_prix = 50
elif niveau == "2":
    prix = random.randint(1, 100)
    grand_prix = 100
else:
    print("     Niveau de difficulté pas valide, le jeu se lance en mode facile par defaut")
    prix = random.randint(1,5) 
    grand_prix = 50



debut_chrono = time.time()
devine="     Devines le prix entre 1 et " + str(grand_prix) + ": "
compteur: int = 0
print( devine )
while devine != prix:
    compteur += 1
    devine = input("     \n     ")
    if devine.isdigit() == False:
        print("     !!Ce n'est pas un nombre, essaye encore!!😡\n")
        continue
    devine = int(devine)
    if devine < prix:
        print("     C'est trop petit !!")
        print("     reessaie encore")
    elif devine > prix:
        print("     C'est trop grand !!")
        print("     reessaie encore")

fin_chrono = time.time()
chrono = int(fin_chrono-debut_chrono)
print(f"     Bravo tu as trouve le prix en {compteur} tentatives et en {chrono}s!")
