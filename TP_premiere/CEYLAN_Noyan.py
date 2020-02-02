from math import *
a=float(input("donner a :"))
b=float(input("donner b :"))
c=float(input("donner c :"))
if a==0:
     if b==0:
           if c==0:
                print("tout réel est une solution")
           else:
                 print("pas de solution")
     else:
            print("la solution est :",-c/b)
else:
      d=pow(b,2)-4*a*c
      print("d=",d)
      if d<0:
            print("pas de solution dans R")
      if d==0:
            print("la solution est :",-b/2*a)
      if d>0:
            print("deux solution :",(-b-sqrt(d))/2*a," et ",(-b+sqrt(d))/2*a)