chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Affichage de la suite pyramidale de côté
longueur_chaine = len(chaine)
nb_cotes = int((longueur_chaine * 2 - 1) ** 0.5)

caractere_index = 0
for i in range(1, nb_cotes + 1):
    ligne = chaine[caractere_index:caractere_index + i]
    print(ligne)
    caractere_index += i

