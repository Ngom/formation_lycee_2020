from math import *
a=float(input("donner a:"))
b=float(input("donner b:"))
c=float(input("donner c:"))
x1=float()
x2=float()
D=(b**2)-(4*a*c)
print("Delta=",D)
if D<0:
    print("il n'y a pas de solution réelle.")
if D==0:
    print("Il y a une solution réelle :")
    x0=(-b)/(2*a)
    print("x0=",x0)
if D>0:
    print("Il y a deux solutions réelles :")
    x1=(-b-sqrt(D))/(2*a)
    x2=(-b+sqrt(D))/(2*a)
    print("x1=",x1)
    print("x2=",x2)