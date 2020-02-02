
from math import *

a=float(input("Donner la valeur de a"))
b=float(input("Donner la valeur de b"))
c=float(input("Donner la valeur de c"))
delta=b**2-4*a*c
print("delta =",delta)
if delta==0:
    print("il y a une solution reelle distincte:",-b/2*a)
    if delta < 0:
        print("il n'y a pas de solution reelle")
        if delta > 0:
            print("il y a 2 solutions reelles distinctes:",(-b+math.sqrt(delta))/2*a,"et",(-b-math.sqrt(delta))/2*a)