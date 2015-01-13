taille = int(input())

# on utilise une liste de liste de taille (taille x taille) pour représenter
# le canevas
canvas = [[' '] * taille for _ in range(taille)]
 
def sierpinski(taille, x=0, y=0):
 
   if taille == 1:
          canvas[y][x] = '#'
   else:
      taille = taille // 2
      sierpinski(taille, x, y)
      sierpinski(taille, x + taille, y)
      sierpinski(taille, x, y + taille)
 
# dans France IOI, il n'est pas possible d'utiliser la fonction math.log2, ce qui 
# nous oblige à la bricoler ...
sierpinski(taille)
 
# affichage du canvas sur la console
for line in canvas:
   print(''.join(line))