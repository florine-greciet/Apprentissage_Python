#Mini projet pour les listes :

#Demander à l'utilisateur d'entrer des noms de films
#Ajouter ces films dans une liste 
#Gérer les doublons
#Classer les films par ordre alphabétique
#Afficher la liste
#Tuple pour associer une note de 1 à 5 pour chaque film.

liste_film = []
continuer = True

while continuer:
    #L'utilisateur rentre un nom de film
    titre_film = input("Saisissez le nom d'un film ")
    
    liste_film_en_minuscule = [film[0].lower() for film in liste_film]
    if(titre_film.lower() not in liste_film_en_minuscule):
        note = int(input("entrez une note sur 5 sur ce film "))
        liste_film.append((titre_film,note))
    else :
        print("{0} se trouve déjà dans la liste" .format(titre_film) )
    
    recommencer = input("souhaitez vous continuer ? (o/n) ")
    if(recommencer.lower() != "o"):
        continuer = False
    
liste_film.sort()
print(liste_film)
   