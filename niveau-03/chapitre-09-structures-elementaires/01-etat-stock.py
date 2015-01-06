import sys

nb_produits = int(input())
produits = [0] + list(map( int, input().split() ))
nb_operations = int(input())

for loop in range(nb_operations):
   type_produit, nb_produit = map( int, sys.stdin.readline().split() )
   produits[type_produit] += nb_produit
   
print(" ".join(map(str, produits[1:])))
