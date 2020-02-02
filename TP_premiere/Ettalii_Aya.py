
a=float( input ("donner a : "))

b=float(input("donner b : "))

c=float( input ("donner c : "))

if a==0 :

    if b==0:

        if c==0:

            print (" Tout rel est une solution ")

        else:

            print ( "il y a pas de solution ")

    else:

            print ( " la solution : " , -b/a )

else:

    DELTA=pow(b,2)-4*a*c 

    if DELTA>0 : 

                print (" il y a deux solutions : " , (-b-sqrt(DELTA))/(2*a ), " et " , (-b+sqrt(DELTA))/(2*a) )

    if DELTA==0 :

                print (" il y a une seule solution :" , -b/2*a)

    if DELTA<0 : 

                print (" il y a pas de solution " )