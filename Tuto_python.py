##LES VARIABLES :
# - peuvent être de type integer, string, bootean, float 

## LES CONDITIONS : 
# pas besoin de parenthèse ou d'accolade pour faire une condition.
#Il faut cependant mettre ":" après avoir écrit la condition 
#Puis indenter tout ce qu'il y aura à l'intérieur de la condition

#LES OPERATEURS : not, or, and
## Dans l'execution not est plus for que and qui est plus fort que True
# True and  False or True : True and False = False, puis False or True = True (car au moins une des propositions est vraies)

## comparaison : pas égal (en python 2 on peut aussi utiliser <>)
print(10 != 5)

### LES LIBRAIRIES ###
#Integration d'une librairie
import(random) 
nombre = random.randint(1,10)

#on peut aussi faire : 
from random import randint
nombre2 = randint(1,10)

#Pour importer toutes les fonctions d'une librairie on peut faire
from random import *
