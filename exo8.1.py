def saisieEntier() :
    
    x = int(input("Longueur de la suite : "))
    L = []
    y = int(input("Entrez un entier : "))
    L.append(y)
    x = x - 1

    while x > 0 :

        y = int(input("Entrez un entier : "))
        L.append(y)
        x = x - 1
    
    return L


def valRemarquable(L) :

    somme = 0
    val = L[0]
    valmin = L[0]
    valmax = L[0]

    for i in range(len(L)) :

        somme = L[i] + somme

        if valmin > L[i] :
            valmin = L[i]
        else :
            valmin = valmin

        if valmax < L[i] :
            valmax = L[i]
        else :
            valmax = valmax
    
    moyenne = somme / len(L)

    return moyenne,valmin,valmax

# Programme principal
L = saisieEntier()

moyenne,min,max = valRemarquable(L)

print("Liste =",L)

print("Min =", min,", max =", max,",moyenne =",round(moyenne, 2))