# Les bases du langage

## Lancer Python sous Linux

```bash
python # ouvre l'interpréteur Python 2
python3 # Python 3 (première version sortie en 2009)
# `Ctrl + D` permet de fermer la ligne de commande Python
```

```bash
python monScript.py # exécute le script en python 2
python3 monScript.py # exécute le script en python 3
```

## Exécuter un script sous windows

ouvrir un script avec **IDLE** et faire `run` ou `F5`
Sinon, glisser le fichier dans la ligne de commande pour l'exécuter
----

## Les différences Python2 vs Python3

- **l'encodage** : en Python2, pour écrire des caractères accentués, il faut ajouter sur la première ligne du script la commande suivante, ce qui n'est pas nécessaire en Python3
```py
# -*- coding: utf-8 -*-
print('Hello')
```
- **la division de nombres entiers**
```py
5/2 = 2 # python2
5/2 = 2.5 # python3
```

## Les opérations

```py
1 + 2 # 3
1 - 2 # -1
3.11 + 2.08 # 5.1899999999999995 au lieu de 5.19
4.56 * 5.3 # 24.167999999999996 au lieu de 24.168
10 / 5 # 2.0
10 // 3 # 3, partie entière de la division
10 % 3 # 1, modulo : reste de la division entière
5 ** 2 # 25, puissance
```

## Les variables

```py
nomVariable = valeur
```
- les nombres entiers (**int**) : `25`
- les nombres flottants (**float**) : `25.0`
- les chaînes de caractères (**string**), entre simples quotes, doubles quotes, ou triples doubles quotes : `"""Hello World"""`
- les booléens (**bool**) qui vallent *True* ou *False*

Quelques astuces :
```py
v += 1 # est égal à var = var + 1 (incrémentation)
# il existe aussi -= *= /=
a,b = b,a # permutation
```

## Quelques fonctions utiles

La fonction `print()` :
```py
 # en utilisant la virgule comme séparateur, les paramètres sont séparés par un espace
a = 5
print("a",a) # donne `a 5`

# la concaténation (avec le +) ne fonctionne qu'avec des variables de type string et n'ajoute pas d'espace
b='6'
print("b"+b) # donne b6
```

la fonction `type(nomVariable)` donne le type de la variable.  
La fonction `input()` permet de récupérer la saisie de l'utilisateur au format string.  
Le fonction `int(texte)` permet de convertir une donnée en entier.  
Le fonction `float(texte)` permet de convertir une donnée en float.  
Le fonction `str(texte)` permet de convertir une donnée en string.  
```py
texte = input("Veuillez saisir un nombre : ") # 2019
type(texte) # str
annee = int(texte)
type(annee) # int
```
La fonction `randint(a,b)` de la bibliothèque `random` permet de générer un nombre entier aléatoire entre a et b inclus
```py
import random
nombreAleatoire = random.randint(1,5)
print(nombreAleatoire)


from random import randint
nombreAleatoire = randint(1,5)
print(nombreAleatoire)
```

La fonction `append(a)` permet d'ajouter un élément à une liste.

La fonction `range(n)` crée un tableau de n élément allant de 0 à n-1
```py
for i in range(10):
    print(i)
# [0,1,2,3,4,5,6,7,8,9]
```
- On peut lui attribuer deux paramètres `range(n1,n2)` la fonction créera alors un tableau allant de n1 à n2-1
```py
for i in range(1,10):
    print(i)
# [1,2,3,4,5,6,7,8,9]
```
- On peut lui ajouter un troisième paramètre qui correspondra au pas.
```py
for i in range(2,10,2):
    print(i)
# [2,4,6,8]
```

## Les conditions
Les conditions ne nécessitent pas de parenthèses ou d'accolades. Il faut cependant les ":" à la fin de la condition
puis indenter tout ce qui se trouve à l'intérieur de la condition.

```py
if nb > 0:
    print("nb est positif")
elif nb < 0:
    print("nb est négatif")
else:
    print("nb est nul")
```

Les opérateurs de comparaison sont :
- `<`
- `>`
- `<=`
- `>=`
- `==`
- `!=`

Les mots clés `and`, `or` et `not` permettent d'enrichir les prédicats des conditions. Il est possible d'utiliser des parenthèses pour définir de manière précises les priorités.
`not` est plus fort que `and` qui lui-même est plus fort que `or`. On peut mettre des parenthèses pour changer cet ordre naturel.
```py
if var>5 and var<10:
if var==5 or var==10:
if not a==5: # équivalent à a!=5
True and False or True # True car (False or True)
False and (False or True)  # True car (False and True)
```
Le mot clé `is` teste l'égalité de la référence d'une valeur
```py
homme = True
if homme is not True:
    print('Vous êtes une femme')
else:
    print('Vous êtes un homme')
```

## Les boucles


### La boucle while
```py
while condition:
    # instruction 1
    # instruction 2
```

exemple :
```py
i = 0
while i<10:
    print("tout de boucle",i)
    i+=1
```


### La boucle for

elle permet de parcourir des séquences de plusieur données
```py
for element in sequence:
```

exemple qui affiche `H` puis `e` puis `l` puis `l` et `o`
```py
chaine = "Hello"
for lettre in chaine:
    print(lettre)
```
Il est possible d'utiliser `in` dans une condition. Autre exemple qui affiche `* e * * o`
```py
chaine = "Hello"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else:
        print("*")
```

exemple en itérant de i allant de 1 à 5
```py
for i in range(1, 6):
  print(i) # affiche i de 1 à 5
```

### Les mots-clés break et continue

- **break** permet d'interromptre une boucle
- **continue** permet de passer au tour de boucle suivant sans terminer le tour de boucle en cours

exemples :
```py
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break
```

## Les listes 
- **List** collection dans lequel on peut stocker des valeurs

Création d'un tableau :
```py
my_integers = [1, 2, 3, 4, 5]
``` 

Récupération des informations de la liste :
```py
my_integers_num1 = my_integers[0] #Les indices commencent à 0
``` 

Ajout d'un élément dans une liste :
- **Apend** fonction qui permet d'ajouter un élement à une liste
```py
bookshelf = [] #Création d'une liste vide
bookshelf.append("The Effective Engineer")
print(bookshelf[0])
``` 

## Les imports de bibliothèque 

- `import lib` importe toute la librairie `lib`
```py
import random 
nombre_al = random.randint(1,2)
```

- `import lib as lib2` permet de renommer la bibliothèque lib en `lib2`
```py
import random as r
nombre_al = r.randint(1,2)
```
- `from lib import fct` permet d'importer une fonction `fct` de la bibliothèque `lib`
```py
from random import randint 
nombre_al = randint(1,2)
```

- `from lib import *` permet d'importer toutes les fonctions de la bibliothèque `lib`
```py
from random import *
nombre_al = randint(1,2)
```