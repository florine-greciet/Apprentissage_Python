#Mini projet 01 : devine un nombre
from random import randint

#fonction format
# essai = input('Entrez un nombre ({0} essai): '
#	.format(i))



nombre_a_deviner = randint(1,100) #nombre aléatoire choisi dans [1,100]
print(nombre_a_deviner)

nombre_tape = 0
nombre_essai = 0 
while nombre_tape != nombre_a_deviner:
	nombre_essai += 1
	#input récupere le texte tapé au clavier partition par l'utilisateur
	nombre_tape = int(input("Entrez un nombre "))
	if nombre_tape > nombre_a_deviner:
		print("Le nombre a deviner est plus petit que " + str(nombre_tape))
	elif nombre_tape < nombre_a_deviner:
		print("Le nombre a deviner est plus grand que " + str(nombre_tape))
	else:
		print("Bavo, vous avez gagné en " + str(nombre_essai) + " essais")
		
print('Fin du jeu')
	