# Exercice 2.1 (Euclide)
# Fonction qui calcule le pgcd de 2 entiers a et b en utilisant l'algorithme d'Euclide
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b  # Remplacer a par b et b par le reste de a divisé par b
    return a  # Lorsque b devient 0, a est le pgcd

# Exercice 2.2 (Miroir)
# Fonction qui donne le "miroir" d'un entier passé en paramètre s'il est positif
def miroir(n):
    if n <= 0:
        return None  # Si n n'est pas positif, on ne retourne rien (ou peut-être une erreur)
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10  # Ajouter le dernier chiffre à l'inversé
        n = n // 10  # Supprimer le dernier chiffre de n
    return reversed_number

# Exercice 2.3 (Quotient)
# Fonction qui calcule le quotient entier de a sur b, ainsi que le reste, en n’utilisant que des opérateurs + et -
def quotient_et_reste(a, b):
    quotient = 0
    reste = a
    while reste >= b:
        reste = reste - b
        quotient += 1
    return quotient, reste

# Exercice 2.4 (Factorielle calculable ?)
# Fonction qui calcule le plus grand entier pair n tel que n! < limite
def plus_grand_pair_factorielle(limite):
    if limite <= 0:
        return 0  # Si la limite est inférieure ou égale à 0, on retourne 0
    fact = 1
    n = 2
    while fact * n <= limite:
        fact *= n
        n += 2  # On incrémente n de 2 pour garder n pair
    return n - 2  # On retourne le dernier n pair dont la factorielle est inférieure à la limite

# Exercice 2.5 (Nombre premier)
# Fonction qui vérifie si un entier strictement supérieur à 1 est premier ou non
def est_premier(n):
    if n <= 1:
        return False  # Les nombres inférieurs ou égaux à 1 ne sont pas premiers
    for i in range(2, int(n**0.5) + 1):  # Vérification jusqu'à la racine carrée de n
        if n % i == 0:
            return False  # Si n est divisible par i, ce n'est pas un nombre premier
    return True

# Exercice 2.6 (Bonus : Multiplication égyptienne)
# Fonction qui calcule x * y en utilisant des additions, des multiplications par 2 et des divisions par 2
def multiplication_egyptienne(x, y):
    resultat = 0
    while y > 0:
        if y % 2 != 0:  # Si y est impair
            resultat += x  # On ajoute x au résultat
        x *= 2  # On double x
        y //= 2  # On divise y par 2 (division entière)
    return resultat

# Exemple d'utilisation pour tester les fonctions
if __name__ == "__main__":
    # Test de pgcd
    print("pgcd(48, 18) =", pgcd(48, 18))  # Devrait afficher 6

    # Test de miroir
    print("miroir(1278) =", miroir(1278))  # Devrait afficher 8721
    print("miroir(1250) =", miroir(1250))  # Devrait afficher 521

    # Test de quotient_et_reste
    q, r = quotient_et_reste(17, 4)
    print("quotient_et_reste(17, 4) = quotient:", q, "reste:", r)  # Devrait afficher quotient: 4, reste: 1

    # Test de plus_grand_pair_factorielle
    print("plus_grand_pair_factorielle(150) =", plus_grand_pair_factorielle(150))  # Devrait afficher 4

    # Test de est_premier
    print("est_premier(7) =", est_premier(7))  # Devrait afficher True
    print("est_premier(10) =", est_premier(10))  # Devrait afficher False

    # Test de multiplication_egyptienne
    print("multiplication_egyptienne(10, 13) =", multiplication_egyptienne(10, 13))  # Devrait afficher 130
    print("multiplication_egyptienne(11, 13) =", multiplication_egyptienne(11, 13))  # Devrait afficher 143
