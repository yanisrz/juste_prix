import random
import time 
prix = random.randint(1, 50)
debut_chrono = time.time()
devine=""
compteur: int = 0
print(prix)
while devine != prix:
    compteur += 1
    devine = input("Devines le prix entre 1 et 50: ")
    if devine.isdigit() == False:
        print("!!Ce n'est pas un nombre, essaye encore!!😡")
        devine = input("reesaie: ")
        continue
    devine = int(devine)
    if devine < prix:
        print("C'est trop petit !!")
    elif devine > prix:
        print("C'est trop grand !!")
    
fin_chrono = time.time()
chrono =int(fin_chrono-debut_chrono)
print(f"bravo tu as trouve le prix en {compteur} tentatives et en {chrono}s!")
    
   


