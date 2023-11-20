nom_produit = "Ordinateur portable"
prix_unitaire = 800  
quantite_en_stock = 50

print("Nom du produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)

quantite_acheter = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_en_stock += quantite_acheter

prix_unitaire *= 1.1  

print("\nInformations mises à jour :")
print("Nom du produit :", nom_produit)
print("Nouveau prix unitaire :", prix_unitaire)
print("Nouvelle quantité en stock :", quantite_en_stock)