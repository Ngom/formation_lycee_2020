def sol_sec_degre(a,b,c):
  return()


a= float(input("Donnez a ="))
b= float(input("Donnez b ="))
c= float(input("Donnez c ="))
delta =(b**2)-(4*a*c)
if delta >0 :
  print("il y'a deux solutions réelles distinctes")
  x1=(-b-delta**0.5)/(2*a)
  x2=(-b+delta**0.5)/(2*a)
  print("x1=",x1)
  print("x2=",x2)
elif delta ==0:
  print("il y'a une seule solution réelle")
  x0 = (-b)/2*a
  print("x0=",x0)
else:
  print("il n'y a pas de solution réelle")