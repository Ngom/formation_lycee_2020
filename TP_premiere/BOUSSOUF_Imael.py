from math import*



a=float(input('donner la valeur de a'))

b=float(input('donner la valeur de b'))

c=float(input('donner la valeur de c'))



if a==0:

    if b==0:

        if c==0:

            print('Solution impossible dans IR')

else:

    delta = (b**2)-4*a*c



if delta <0:

    print('Nadmet pas de solution')



if delta >0:

    print('Admet 2 solutions')

    x1 = (-b-sqrt(delta))/2*a

    x2 = (-b+sqrt(delta))/2*a

    print(x1,x2)

    

if delta==0:

    print('il y a une seul solution')

    #-b/2*a

    print(-b/2*a)