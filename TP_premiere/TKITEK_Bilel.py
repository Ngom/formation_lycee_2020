from math import*
a = float(input("definir a:"))
b = float(input("definir b:"))
c = float(input("definir c:"))
if a==0: 
  if b==0:
    if c==0:
      print("tout reel est une solution")
    else:
      print("pas de solution")
  else: 
    print("la solution est:",-b/a)
else: 
  delta=b**2-4*a*c
  print("delta=",delta)
  if delta<0:
    print("pas de solution")
  if delta==0:
    print("la solution est:",-b/2*a)
  if delta>0:
    print("deux solutions:",(-b-sqrt(delta))/2*a,"et",(-b+sqrt(delta))/2*a)
