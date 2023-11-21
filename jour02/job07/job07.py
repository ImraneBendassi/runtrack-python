chaine = "abcdefghijklmnopqrstuvwxyz" * 10


longueur_chaine = len(chaine)
nb_lignes = int((longueur_chaine * 2 - 1) ** 0.5)

caractere_index = 0
for i in range(1, nb_lignes + 1):
    espace = " " * (nb_lignes - i)
    ligne = espace + chaine[caractere_index:caractere_index + i * 2 - 1] + espace
    print(ligne)
    caractere_index += i * 2 - 1
