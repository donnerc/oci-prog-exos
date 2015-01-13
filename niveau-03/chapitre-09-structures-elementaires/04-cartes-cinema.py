### Cartes de cinéma
### France IOI, partie 4, chapitre 9, problème 4
import sys

nb_clients = int(input())

visites = {}

def check(nb_clients):

    cartes = map(int, sys.stdin.readline().split())

    for no_carte in cartes:
        
        if no_carte in visites:
            return no_carte
            
        else:
            visites[no_carte] = True
            
    return -1
    
print(check(nb_clients))
