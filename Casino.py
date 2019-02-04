#Le joueur mise sur un numéro compris entre 0 et 50
#Quand il choisit son numéro il choisit sa mise

#La roulette : 
# - les numéros pairs sont noirs
# - les numéros impairs sont rouges

#Le croupier lance la roulette, lache la bille et quand la roulette
#s'arrête il indique le numéro qui correspond au numéro gagnant

#si numéro joueur = numéro gagnant :
# il gagne 3* sa mise.

#Sinon si le numéro joeur est de la même couleur que 
#numéro gagnant
#il gagne 0.5 de sa mise

#sinon :
#il à perdu

from random import randrange
from math import ceil

cagnotte = int(input("Définissez votre mise de départ "))

while(cagnotte >0):
    nombre_roulette = randrange(50)
    print(nombre_roulette)

    nombre_choisi = int(input("Choisissez un nombre entre 0 et 49 "))
    mise = int(input("choisissez votre mise "))
    
    if(nombre_choisi == nombre_roulette):
        cagnotte += 3*mise
    
    elif((nombre_choisi%2) == (nombre_roulette%2)):
        cagnotte += ceil(0.5*mise)
    
    else:
        cagnotte -= mise
    if cagnotte >0:
        jouerEncore = input("Il vous reste {0} euros, voulez vous rejouer (o/n) ?" .format(cagnotte))
        if jouerEncore != "o":
            break
