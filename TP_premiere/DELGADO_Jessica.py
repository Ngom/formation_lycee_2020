from math import *
print("")
a = float(input("Donner la valeur de a: a="))
b = float(input("Donner la valeur de b: b="))
c = float(input("Donner la valeur de c: c="))
print("")
print("Le polynôme est donnée par: P(x) =", a , "x^2 +",b ,"x +",c, "=0")
print("")
Delta = b**2 - 4*a*c
print("Delta=", Delta)
print("")
if Delta > 0:
	print("Alors, l'équation du polynôme admet 2 solutions réelles distinctes:")
	x1 = (-b-sqrt(Delta))/2*a
	x2 = (-b+sqrt(Delta))/2*a
	print("x1 = ",x1," et x2 = ",x2)
if Delta==0:
	print("Alors, l'équation du polynôme admet une unique solution réelle:")
	x0=-b/(2*a)
	print("x0 = ",x0)
if Delta<0:
print ("Alors, l'équation du polynôme n'amet pas de solution réelle.")