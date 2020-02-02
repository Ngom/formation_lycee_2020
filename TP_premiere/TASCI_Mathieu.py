from math import *


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))


def equation(a, b, c):
    print("L'équation est : ", a, "x² + ", b, "x + ", c)
    Delta = (b ** 2) - (4 * a * c)
    print("Delta =", Delta)
    if Delta < 0:
        print("Le discriminant est inférieur à 0, il n y a pas de solution.")
    elif Delta == 0:
        print("Le discriminant est égal à 0, il y a une solution:")
        x0 = (- b) / (2 * a)
        print ("x0 =", x0)
    else:
        print("Le discriminant est supérieur à 0, il y a deux solutions:")
        x1 = (- b - sqrt(Delta)) / (2 * a)
        x2 = (- b + sqrt(Delta)) / (2 * a)
        print ("x1 =", x1)
        print ("x2 =", x2)
equation(a, b, c)