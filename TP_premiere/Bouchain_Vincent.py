from math import *


a = int(input("Choisissez la valeur de a :"))
b = int(input("Choisissez la valeur de b :"))
c = int(input("Choisissez la valeur de c :"))


def eq2(a, b, c):
    print("L'équation est : ", a, "x² + ", b, "x + ", c, ".", sep="")
    d = (b ** 2) - (4 * a * c)
    print("Delta est de ", d, ".", sep="")
    if d < 0:
        print("Il n y a pas de solution.")
    elif d == 0:
        print("Il y a une solution :")
        n = (- b) / (2 * a)
        print ("x =",n)
    else:
        print("Il y a deux solutions :")
        n = (- b - sqrt(d)) / (2 * a)
        z = (- b + sqrt(d)) / (2 * a)
        print ("x1 =",n)
        print ("x2 =",z)
eq2(a, b, c)