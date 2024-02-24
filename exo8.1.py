def saisieEntier() :
    
    x = int(input("Longueur de la suite : "))
    L = []
    y = int(input("Entrez un entier : ")) #Saisi un entier
    L.append(y)                           #Puis l'ajoute à la liste
    x = x - 1

    while x > 0 : #Boucle jusqu'à que la liste fasse la bonne longueur

        y = int(input("Entrez un entier : "))
        L.append(y)
        x = x - 1
    
    return L


def valRemarquable(L) :

    somme = 0
    val = L[0]
    valmin = L[0]
    valmax = L[0]

    for i in range(len(L)) : #Parcours toute la liste

        somme = L[i] + somme #Fait la somme de chaque entier

        if valmin > L[i] :
            valmin = L[i]
        else :
            valmin = valmin

        if valmax < L[i] :
            valmax = L[i]
        else :
            valmax = valmax
    
    moyenne = somme / len(L) #Calcul la moyenne grâceà la fonction len qui indique la longueur (nombre d'entier dans la liste) de la liste

    return moyenne,valmin,valmax

# Programme principal
L = saisieEntier()

moyenne,min,max = valRemarquable(L)

print("Liste =",L)

print("Min =", min,", max =", max,",moyenne =",round(moyenne, 2)) #On arrondit la moyenne histoire d'avoir des valeurs pas trop moche
