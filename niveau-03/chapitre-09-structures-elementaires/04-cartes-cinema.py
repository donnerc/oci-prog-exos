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

'''
# Version de France IOI

MAX_VAL = 1000 * 1000 + 1
dejaVu = [False] * MAX_VAL
 
def main():
   nbValeurs = int(input())
   valeurs = map(int, input().split())
   for valeur in valeurs:
      if dejaVu[valeur]:
         print(valeur)
         return
      dejaVu[valeur] = True
   print(-1)
 
main()
'''