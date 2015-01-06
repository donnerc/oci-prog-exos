nb_operations = int(input())

MAX_SIZE = 1000

# On définit une pile spécialisée qui permet d'ajouter
# plusieurs éléments identiques à la fois. De plus, il est important
# d'allouer une taille fixe de MAX_SIZE au début pour des raisons de performance
class Stack(object):
   
   def __init__(self, max_size):      
      self.elements = [0] * max_size
      self.peek = -1
      
   def n_push(self, nb_elements, date):
      for loop in range(nb_elements):
         self.peek += 1
         self.elements[self.peek] = date
         
   def n_pop(self, nb_elements):
      self.peek -= nb_elements
      
   def peek(self):
      return self.peek
      
   def find_min(self):
      return min(self.elements[:self.peek+1])

s = Stack(MAX_SIZE)

for loop in range(nb_operations):
   delta, date = (int(n) for n in input().split(" "))
   if delta > 0:
      s.n_push(delta, date)
   else:
      s.n_pop(-delta)
      
print(s.find_min())
   