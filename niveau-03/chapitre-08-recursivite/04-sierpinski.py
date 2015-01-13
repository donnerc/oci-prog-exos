n = int(input())

def developper(n):
   if n == 0:
      # base de case
      return "0"
   else:
      # cas récursif
      return  "(" + developper(n-1) + " + " + developper(n-1) + ")"
      
print("0 = ", developper(n))
