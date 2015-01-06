import sys

MAX_PRODUITS = 1000

class Queue(object):

    def __init__(self, max_size):
        self.size = 0
        self.front = 0
        self.rear = -1
        self.elements = [0] * max_size

    def min(self):
        if self.rear < self.front:
            elements = self.elements[self.front:] + self.elements[:self.rear+1]
        else:
            elements = self.elements[self.front:self.rear+1]
        return min(elements)
       
        
    def __len__(self):
        return self.size

    def enqueue_n(self, nb, element):
        
        for i in range(1, nb + 1):
           self.elements[(self.rear + i) % MAX_PRODUITS] = element
        self.rear = (self.rear + nb) % (MAX_PRODUITS)
        self.size += nb
        

    def dequeue_n(self, nb):
        element = self.elements[self.front]
        self.front = (self.front + nb) % (MAX_PRODUITS)
        self.size -= nb
        return element

    def __str__(self):
        return " ".join(map(str, self.elements[:len(self)]))

def main():
    queue = Queue(MAX_PRODUITS)
    nb_operations = int(input())
    for loop in range(nb_operations):
        quantite, date = map( int, sys.stdin.readline().split() )

        if quantite > 0:
            # on rajoute des elements au sommet de la pile (dans la file en fait)
            queue.enqueue_n(quantite, date)

        else:
            # on supprime des éléments (au bas de la pile) i.e. en tête de queue
            queue.dequeue_n(-quantite)
                
    print(queue.min())


main()
