def afficher_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée.")

afficher_aliments("fruits", "hiver")
afficher_aliments("fruits", "ete")
afficher_aliments("legume", "hiver")
afficher_aliments("legume", "ete")
afficher_aliments("poisson", "printemps")
