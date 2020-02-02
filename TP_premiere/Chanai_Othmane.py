from math import* #importer les fonctions mathématiques à utiliser
#ax^2+bx+c

a = float(input("Donner la valeur de a="))#Valeur de a
b = float(input("Donner la valeur de b="))#Valeur de b
c = float(input("Donner la valeur de c="))#Valeur de c
if a == 0:
    if b == 0:
        if c == 0:
            print("La solution est impossible dans l'ensemble IR")
else :
  Delta = b**2-(4*a*c)
  print("Delta=",Delta)
if (Delta<0) :
  print("pas de solutions réelles possibles")
if (Delta==0):
  print("une seule solutuion possible:")
  X0 = -b/2*a
  print(X0)
if (Delta>0):
  print("deux solutions réelles possibles")
  X1 = (-b-sqrt(Delta))/2*a
  X2 = (-b+sqrt(Delta))/2*a
  print(X1,X2)
