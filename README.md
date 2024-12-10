README - Fonctions Python
Introduction
Ce projet contient une série de fonctions Python qui résolvent des problèmes algorithmiques classiques. Chaque fonction est conçue pour illustrer différentes techniques de programmation, allant du calcul du pgcd à l'implémentation de méthodes anciennes comme la multiplication égyptienne. Ce README explique brièvement chaque fonction et son fonctionnement.

Fonctionnalités
1. pgcd (Euclide)
Cette fonction calcule le plus grand commun diviseur (pgcd) de deux entiers a et b en utilisant l'algorithme d'Euclide. L'algorithme repose sur le fait que le pgcd de deux nombres peut être trouvé en remplaçant successivement le plus grand nombre par le reste de la division de ce nombre par le plus petit. Ce processus se répète jusqu'à ce que le reste soit nul, et le dernier non nul reste est le pgcd.

2. miroir
La fonction miroir renverse les chiffres d'un entier positif. Par exemple, si l'on passe 1278, la fonction retournera 8721. Elle supprime également les zéros à la fin du nombre. Ainsi, pour l'entrée 1250, le résultat sera 521. Cela permet d'inverser un nombre tout en nettoyant les zéros inutiles à la fin.

3. quotient_et_reste
Cette fonction calcule le quotient et le reste de la division entière de deux entiers a et b, en n'utilisant que des opérations d'addition et de soustraction. Le quotient est le nombre de fois que b peut être soustrait de a avant que le reste soit inférieur à b. Le reste est ce qui reste après la soustraction successive.

4. plus_grand_pair_factorielle
Cette fonction trouve le plus grand entier pair n tel que n! (la factorielle de n) soit inférieur à une limite donnée. Si la limite est inférieure ou égale à zéro, la fonction renverra 0. Cela permet de déterminer le plus grand nombre pair dont la factorielle reste sous une certaine valeur.

5. est_premier
La fonction est_premier détermine si un entier n est un nombre premier. Un nombre premier est un nombre entier plus grand que 1, qui n'est divisible que par 1 et lui-même. La fonction vérifie la divisibilité de n par tous les entiers de 2 à la racine carrée de n. Si n n'est divisible par aucun de ces entiers, alors n est premier.

6. multiplication_egyptienne
La multiplication égyptienne est une méthode ancienne de multiplication qui ne nécessite que des additions et des multiplications/divisions par 2. Elle repose sur l'idée de doubler un des facteurs et de diviser l'autre par 2, tout en ajoutant le premier facteur à chaque fois que le second facteur est impair. Cette méthode peut être utilisée pour effectuer des multiplications sans recourir à l'opérateur de multiplication traditionnel.

Conclusion
Ces fonctions montrent différentes approches pour résoudre des problèmes algorithmiques classiques. Elles couvrent des concepts comme l'algorithme d'Euclide pour le pgcd, la vérification des nombres premiers, et l'optimisation des calculs avec des techniques anciennes comme la multiplication égyptienne.
