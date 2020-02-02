from math import *
def equation(a,b,c):
delta=(b**2)-(4*a*c)
if delta<0:return("il n'y a pas de solution")
x=(-b-delta**0.5)/(2*a)
y=(-b+delta**0.5)/(2*a)
if delta>0:return(x,y)
if delta==0:return(x)

a=input("mettre a:")
b=input("mettre b:")
c=input("mettre c:")

print(equation(-4,6,9))