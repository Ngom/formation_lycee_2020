from math import*

print("Ce programme peut calculer les racines d'un polynome du second degre")
print("Tel que f(x) = ax²+bx+c = 0")
a=int(input("Entrez la valeur de a"))
b=int(input("Entrez la valeur de b"))
c=int(input("Entrez la valeur de c"))
delta=b*b-4*a*c
print(delta) #valeur de Delta
if delta <0:
    print("Ce polynome n'a pas de solutions reelles")
if delta ==0:
    print("Ce polynome a une seule solution reelle")
    x=-b/(2*a)
    print(x) #valeur de la solution
if delta >0:
    print("Ce polynome a deux solutions reelles")
    h=-b-sqrt(delta)
    i=-b+sqrt(delta)
    n=2*a
    x1=h/n
    x2=i/n
    print(x1) #valeur de la premiere solution
    print(x2) #valeur de la seconde solution
print("Fin du Calcul !")