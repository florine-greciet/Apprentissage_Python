#Mini projet 01 : devine un nombre


## Les cours : 

#Les opérateurs : not, or, and
## Dans l'execution not est plus for que and qui est plus fort que True
# True and  False or True : True and False = False, puis False or True = True (car au moins une des propositions est vraies)

## comparaison : pas égal (en python 2 on peut aussi utiliser <>)
print(10 != 5)


### Le projet

from random import randint
#sinon : import random	et on fait random.randint


nombre_a_deviner = randint(1,100) #nombre aléatoire choisi dans [1,100]
print(nombre_a_deviner)

nombre_tape = 0
while nombre_tape != nombre_a_deviner:
#input récupere le texte tapé au clavier partition par l'utilisateur
	nombre_tape = input("Entrez un nombre ")
	if int(nombre_tape) > nombre_a_deviner:
		print("Le nombre a deviner est plus petit")
	elif int(nombre_tape) > nombre_a_deviner:
		print("Le nombre a deviner est plus grand")
	elif int(nombre_tape) == nombre_a_deviner:
		print("Bavo, vous avez gagné")
		break