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
import random
nombre = random.randint(1,10)

#on peut aussi faire : 
from random import randint
nombre2 = randint(1,10)

#Pour importer toutes les fonctions d'une librairie on peut faire
from random import *

# les listes 
liste_de_nombre = [1,2,3]
liste_mixte = ["Pierre",2,"Paul",3.5]
liste_imbriquees = [1,2,[3,4]]

##Pour récupérer la longueur d'une liste "len"
long_liste = len(liste_de_nombre)

## On peut également compter le nombre de fois ou un (mot, chiffre) apparait dans la liste
ma_liste = ["Pierre","Thomas","Pierre","Paul"]
ma_liste.count("Pierre")
#Attention python est sensible à la casse. si on tape "pierre", ma_liste.count("pierre") retournera 0.


##Comment accéder à un élément :
liste = ["U","d","e","m","y"]
liste[0]
#Les identifiants commencent à 0 pour python

#Pour aller chercher le dernier élément de la liste on peut faire : 
liste[len(liste)-1]
#sinon on peut faire 
liste[-1]


#Les slices : 
liste[0:2] #permetra de récupérer "U" et "d"
liste[0:1] #permettra de récupérer "U"
#un élément est compris entre deux indices. "U" est compris entre 0 et 1, "d" est compris entre 1 et 2 etc...

# Pour récupérer toutes les infos depuis un indice jusqu'à la fin:
liste[2:]
#Pour récupérer toutes les infos du début jusqu'à un indice
liste[:4]
#Ob peut aussi le faire avec les indices négatifs
liste[:-2]
#pour récupérer toute la liste 
liste[:]


##Pour ajouter un élément à une liste : 
liste.append('Jacques')
#Pour spécifier à quel endroit on veut ajouter notre élément dans la liste : 
liste.insert(1,"Kevin")
#Pour ajouter une liste à une autre liste 
liste.extend(["Bertrand","John"])
# On peut faire un += à la place de liste.extend


##Comment retirer des éléments d'une liste :
liste2 = ["Pierre","Paul"]
liste2.remove("Pierre")

#liste2.pop(1) #il prend en parametre l'indice de l'élément que l'on souhaite enlever
#L'avantage de cette fonction est qu'elle retourne l'élément supprimé. On peut donc le conserver dans une variable.

#dernière façon de faire :
#del liste2[0] #prend en parametre l'indice de l'élément que l'on souhaite supprimer


#Un élément est-il présent dans une liste : 
liste_abc = ["a","b","c"]
"a" in liste_abc


##comment itérer dans une liste 
liste_it = [1,2,3,4]
for i in liste_it:
    print(i)

#Trier une liste 
liste_tri = [4,5,8,2,0]
liste_tri.sort() # permet de trier la liste 

#Pour inverser une liste
liste_tri.reverse()
#On peut aussi classer une liste dans le sens inverse en faisant :
liste_tri.sort(reverse=True)


#Comment modifier un élément dans une liste :
liste_mod = ["pierre","paul"]
liste_mod[1] = "john"


##Les compréhensions de liste : 
liste_comp = [1,2,3,4,5]
liste_mult = []
for i in liste:
    liste_mult.append(i*2)

#Au lieu de faire ça on peut utiliser les compréhensions de liste : 
liste_comp = [1,2,3,4,5]
liste_comp = [i*2 for i in liste_comp]
#On peut également faire des if et else à l'interieur de cette compréhension de liste.


##Les tuples : collection de données mais qui ne sont pas modifiables.
#Il se définit avec les parenthèses
mon_tuple = (1,2,3)

#pour accéder à un élément :
mon_tuple[2]
#on peut aussi faire les slices sur les tuples


couleur = (200,155,125) #bleur vert rouge
max(couleur)
min(couleur)


## Les dictionnaires : 
#permet d'accéder plus faciement aux valeurs
#Un dictionnaire fonctionne avec des paires de clefs et de valeurs
dictionnaire = {'clef':'valeur', 'clef1','valeur1'}

dico = {'Pierre':25,'Paul':30}
#Pour récupérer les infos de Pierre
dico['Pierre']

dico2 = {
    'Pierre':{'age':40,'profession':'banquier'},
    'paul':{'age':25,'profession':'ingenieur'}
    }
#Pour récuperer les infos de Pierre
dico2['Pierre']
#Pour récupérer l'age de Paul
dico2['Pierre']['age']
#Pour répérer la profession
dico2['Pierre']['profession']

##On peut également utilisée la fonction get()
dico.get('Pierre')
#25
dico2.get("Pierre").get("age")
#40

#liste des clefs contenues dans le dico
dico.keys()
#'Pierre','Paul'

#on récupère les valeyrs d'un dictionnaire
dico.values()
#dict_values([25, 30])
dico2.values()

#Pour récupérer à la fois les clefs et les valeurs d'un dictionnaire 
#on utilse la fonction items (liste de tuple)
dico.items()
dict_items([('Pierre', 25), ('Paul', 30)])
dico2.items()

