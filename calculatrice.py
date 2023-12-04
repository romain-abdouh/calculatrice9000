def saisir_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def saisir_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez l'opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Non valide, choisir  +, -, *, /.")

def calculer_resultat(nombre1, nombre2, operation):
    if operation == '+':
        return nombre1 + nombre2
    elif operation == '-':
        return nombre1 - nombre2
    elif operation == '*':
        return nombre1 * nombre2
    elif operation == '/':
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            print("Erreur : Division par zéro.")
            return None

def afficher_historique(historique):
    if not historique:
        print("Historique vide.")
    else:
        print("Historique des calculs :")
        for index, calcul in enumerate(historique, start=1):
            print(f"{index}. {calcul}")

def calculatrice():
    print("Calculatrice:")
    historique = []

    while True:
        nombre1 = saisir_nombre()
        operation = saisir_operation()
        nombre2 = saisir_nombre()

        resultat = calculer_resultat(nombre1, nombre2, operation)

        if resultat is not None:
            calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
            historique.append(calcul)
            print(f"Le résultat de {calcul}")

        afficher_historique(historique)

        continuer = input("Voulez-vous effectuer un autre calcul ? (o/n) : ").lower()
        if continuer != 'o':
            print("Fin de la calculatrice.")
            break


calculatrice()