from math import *
a=float(input("donner la valeur de a :"))
b=float(input("donner la valeur de b :"))
c=float(input("donner la valeur de c :"))
if a==0:
    if b==0:
        if c==0:
            print("tous reel est une solution")
        else:
            print("pas de solution")
    else:
        print("la solution est :",-b/a)
else:
    D=pow(b,2)-4*a*c
    print(D)
    if D<0:
        print("pas de solution dans l'ensemble R")
    if D==0:
        print("la solution est :",-b/2*a)
    if D>0:
        print("il y a deux solutions :",(-b-sqrt(D))/2*a,"et aussi ",(-b+sqrt(D))/2*a)
