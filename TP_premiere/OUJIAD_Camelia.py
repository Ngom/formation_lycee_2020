from math import * # star oublie  par l'eleve.

print("")

a=float(input("inserer la valeur de a: a="))

b=float(input("inserer la valeur de b: b="))

c= float(input("insererla valeur de c: c="))

print("")

print("ce polynôme est exprimée par: P(x) =", a , "x^2 +",b ,"x +",c, "=0")

print("")

Delta=b**2 - 4*a*c

print("Delta=", Delta)

print("")

if Delta>0:

print("Alors cette équation du polynôme admet 2 solutions réelles distinctes:")

x1=(-b-sqrt(Delta))/2*a

x2=(-b+sqrt(Delta))/2*a

print("x1 = ",x1," et x2 = ",x2)

if Delta(==0):

print("Alors cette equation du polynôme admet une seule et unique solution réelle:")

x0=-b/(2*a)

print("x0 = ",x0)

if Delta<0:

print("Alors cette equation du polynôme n'amet aucune solution réelle.")