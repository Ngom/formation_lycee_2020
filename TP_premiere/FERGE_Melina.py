from math import *
a=float(input("donner a="))
b=float(input("donner b="))
c=float(input("donner c="))
if a==0:
	if b==0:
		if c==0:
			print("tout reel est une solution")
		else:
			print("pas de solution")
	else:
		print("la solution est:",-c/b)
else:
	D=pow(b,2)-4*a*c
	print("D=",D)
if D<0:
	print("pas de solution dans R")
if D==0:
	print("la solution est:",-b/2*a)
if D>0:
	print("deux solutions:",(-b-sqrt(D))/2*a,"et",(-b+sqrt(D))/2*a)
