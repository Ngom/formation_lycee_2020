from math import *


def sol_degre_2(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        msg = ("Pas de solution réelle!")
    elif delta == 0:
        msg = (f"une seul solution!{round(-b/(2*a),2)}")
    else:
        x1 = -b - sqrt(delta) / 2*a
        x2 = -b + sqrt(delta) / 2*a
        msg = (f"Deux solution réelle {round(x1,2)} et {round(x2,2)}")
    return msg

a = float(input("Quelle est la valeur de a ?"))
b = float(input("Quelle est la valeur de b?"))
c = float(input("Quelle est la valeur de c"))
print(sol_degre_2(a, b, c))
