# Exercice 1.1 (Zorglub)
# Fonction zorglub qui calcule la somme des produits successifs des entiers de 1 à n
def zorglub(n):
    # Initialisation des variables
    j = 1  # Le produit des entiers jusqu'à i
    k = 0  # La somme des produits successifs
    i = 1  # Compteur pour les itérations

    # Tant que i est inférieur ou égal à n
    while i <= n:
        j = i * j  # On met à jour le produit
        k = k + j  # On ajoute le produit à la somme
        i = i + 1  # On incrémente le compteur

    return k  # On retourne la somme des produits successifs

# Exercice 1.2 (Multiplication)
# 1. Fonction qui calcule x * y en n’utilisant que les opérateurs + et -
def multiplication(x, y):
    result = 0  # Variable pour stocker le résultat de la multiplication
    # Vérification du signe de y
    if y < 0:
        # Si y est négatif, on inverse le signe de x et on rend y positif en le transformant en positif.
        x = -x
        y = -y
    for _ in range(y):  # On répète y fois (notez que y est maintenant positif)
        result += x  # On ajoute x à result à chaque itération
    return result

# 2. Fonction qui calcule x * y avec (x, y) ∈ Z (entiers négatifs autorisés)
def multiplication_z(x, y):
    result = 0  # Variable pour stocker le résultat
    # Vérification du signe de y
    if y < 0:
        # Si y est négatif, on inverse le signe de x et on rend y positif en le transformant en positif.
        x = -x
        y = -y
    for _ in range(y):  # On répète y fois (notez que y est maintenant positif)
        result += x  # On ajoute x à result à chaque itération
    return result

# Exercice 1.3 (Puissance)
# Fonction qui calcule x^n (x puissance n) pour x ∈ R et n ∈ N
def puissance(x, n):
    result = 1  # Initialisation à 1 (car toute puissance de 0 donne 1)
    for _ in range(n):  # Répéter n fois
        result *= x  # Multiplier par x à chaque itération
    return result

# Exercice 1.4 (Fibonacci)
# Fonction itérative pour calculer le n-ième terme de la suite de Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:  # Cas de base : fibonacci(0) = 1 et fibonacci(1) = 1
        return 1
    a, b = 1, 1  # Initialisation des deux premiers termes
    for i in range(2, n+1):  # Calcul des termes suivants
        a, b = b, a + b  # Mise à jour des termes de Fibonacci
    return b  # Retourne le n-ième terme de Fibonacci

# Exercice 1.5 (Suite)
# 1. Fonction qui retourne la somme des n premiers termes de la suite u
def somme_suite(n, u):
    total = 0
    for i in range(1, n + 1):  # On fait la somme des n premiers termes
        total += u(i)  # On ajoute u(i) à la somme
    return total

# 2. Fonction qui calcule la somme de toutes les sommes des premiers termes jusqu'à n
def somme_sommes_suite(n, u):
    total = 0
    for i in range(1, n + 1):  # On fait la somme des Si (sommes des premiers termes jusqu'à i)
        total += somme_suite(i, u)  # On ajoute la somme des i premiers termes de u
    return total

# 3. Fonction avec une seule boucle pour calculer la somme des sommes
def somme_sommes_suite_optimisee(n, u):
    total = 0
    current_sum = 0  # Initialisation de la somme partielle
    for i in range(1, n + 1):  # On calcule chaque somme de 1 à n en une seule boucle
        current_sum += u(i)  # On ajoute u(i) à la somme partielle
        total += current_sum  # On ajoute la somme partielle à la somme totale
    return total

# Exemple de fonction u qui pourrait être utilisée dans les exercices 1.5
def u(n):
    # Exemple : u(n) = n (la suite est simplement l'entier n)
    return n

# Code d'exemple pour tester toutes les fonctions
if __name__ == "__main__":
    # Test de zorglub
    print("zorglub(5) =", zorglub(5))  # Devrait afficher la somme des produits des entiers de 1 à 5

    # Test de multiplication
    print("multiplication(3, 4) =", multiplication(3, 4))  # 3 * 4 = 12
    print("multiplication_z(3, -4) =", multiplication_z(3, -4))  # 3 * (-4) = -12

    # Test de puissance
    print("puissance(2, 3) =", puissance(2, 3))  # 2^3 = 8

    # Test de Fibonacci
    print("fibonacci(6) =", fibonacci(6))  # Fibonacci de 6 => 13

    # Test de la somme des n premiers termes de la suite u
    print("somme_suite(3, u) =", somme_suite(3, u))  # Devrait afficher 6 (1 + 2 + 3)

    # Test de la somme des sommes des premiers termes jusqu'à n
    print("somme_sommes_suite(3, u) =", somme_sommes_suite(3, u))  # Devrait afficher 20

    # Test de la somme des sommes avec une seule boucle
    print("somme_sommes_suite_optimisee(3, u) =", somme_sommes_suite_optimisee(3, u))  # Devrait afficher 20
