from math import*
A=eval(input('A='))
B=eval(input('B='))
C=eval(input('C='))
delta=B**2-4*A*C
print('delta=',delta)
if delta<0:
	print('Pas de solution')
if delta==0:
	print('une solution')
	x=-B/(2*A)
	print('x=',x)
if delta>0:
	print('Deux solutions')
	x1=(-B-sqrt(delta))/(2*A)
	x2=(-B+sqrt(delta))/(2*A)
	print('x1=',x1)
	print('x2=',x2)
print('Equation Terminer avec succes!')
