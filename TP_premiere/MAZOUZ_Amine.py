
from math import *
print("soit ax**2+bx+c une fontion de degré 2 avec")
a=int(input("a "))
b=int(input("b "))
c=int(input("c "))
delta=int(b*b-(4*a*c))
print("delta vaut",delta)
    if delta==0: 
      x=-b/2*a 
      print("x vaut",x)
    elif delta>0:
        x1=(-b-(sqrt(delta)))/2*a 
        x2=(-b+(sqrt(delta)))/2*a 
 print("x1 et x2 vallent",x1,"et",x2)
elif delta<0:
      print("il n'y a pas de solutions")