def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur: Modulo par zéro"
    else:
        return "Opérateur non pris en charge"


resultat_addition = calcule(5, '+', 3)
resultat_multiplication = calcule(10, '*', 2)


print("Résultat de l'addition:", resultat_addition)
print("Résultat de la multiplication:", resultat_multiplication)
