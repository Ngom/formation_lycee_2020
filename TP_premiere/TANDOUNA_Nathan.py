from math import *
a=float(input("Donner la valeur de a : "))
b=float(input("Donner la valeur de b : "))
c=float(input("Donner la valeur de c : "))
if a==0:
    if b==0:
        if c==0:
            print("Tout réel est une solution")
        else:
            print("Pas de solution")
    else:
    	print("La solution est : ",-b/a)
else:
    Delta=pow(b,2)-4*a*c
    print("Delta = ",Delta)
    if Delta<0:
	    print("Il n'y a pas de solution dans R")
    if Delta==0:
	    print("La solution est : ",-b/2*a)
    if Delta>0:
	    print("Deux solutions : ",(-b-sqrt(Delta))/2*a," et ",(-b-b+sqrt(Delta))/2*a)
	    
