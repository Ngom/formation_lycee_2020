
# coding: utf-8

# # Correction du TP du second degré.

# AHMAD Farhan : Note de l'élève = 9/10.

# In[11]:


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

# Commentaire de correction : Le programme ne tient pas de la valeur a != 0.


# ALITOU Bilel : Note de l'élève = 9/10.

# In[10]:


from math import *
a=float(input("donner la valeur de a :"))
b=float(input("donner la valeur de b :"))
c=float(input("donner la valeur de c :"))
if a==0:
    if b==0:
        if c==0:
            print("tous reel est une solution")
        else:
            print("pas de solution")
    else:
        print("la solution est :",-b/a)
else:
    D=pow(b,2)-4*a*c
    print(D)
    if D<0:
        print("pas de solution dans l'ensemble R")
    if D==0:
        print("la solution est :",-b/2*a)
    if D>0:
        print("il y a deux solutions :",(-b-sqrt(D))/2*a,"et aussi ",(-b+sqrt(D))/2*a)
        
# Commentaire de correction : Le programme ne tient pas de la valeur a != 0.


# ALITOU Ines : Note de l'élève = 9/10.

# In[23]:


from math import *


def sol_degre_2(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        msg = ("Pas de solution réelle!")
    elif delta == 0:
        msg = (f"une seul solution!{round(-b/(2*a),2)}")
    else:
        x1 = (-b - sqrt(delta))/2*a
        x2 = (-b + sqrt(delta))/2*a
        msg = (f"Deux solution réelle {round(x1,2)} et {round(x2,2)}")
    return msg

a = float(input("Quelle est la valeur de a ?"))
b = float(input("Quelle est la valeur de b?"))
c = float(input("Quelle est la valeur de c"))
print(sol_degre_2(a, b, c))

  return()
# Commentaire de correction : Très bien d'uliser une fonction mais le programme buge si on introduit a = 0.


# AVCI Zeynel : Note de l'élève = 8/10.

# In[28]:


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

# Commentaire de correction : Le programme ne tient pas de la valeur a = 0 et les deux première lignes
# du code sont inutiles car il n'y a rien dans fonction.


# BOUCHAIN Vincent : Note de l'élèves = 9/10.

# In[33]:


from math import *


a = int(input("Choisissez la valeur de a :"))
b = int(input("Choisissez la valeur de b :"))
c = int(input("Choisissez la valeur de c :"))


def eq2(a, b, c):
    print("L'équation est : ", a, "x² + ", b, "x + ", c, ".", sep="")
    d = (b ** 2) - (4 * a * c)
    print("Delta est de ", d, ".", sep="")
    if d < 0:
        print("Il n y a pas de solution.")
    elif d == 0:
        print("Il y a une solution :")
        n = (- b) / (2 * a)
        print ("x =",n)
    else:
        print("Il y a deux solutions :")
        n = (- b - sqrt(d)) / (2 * a)
        z = (- b + sqrt(d)) / (2 * a)
        print ("x1 =",n)
        print ("x2 =",z)
eq2(a, b, c)

# Commentaire de correction : Très bien d'uliser une fonction mais le programme buge si on introduit a = 0.


# BOUSSOUL Imael : Note de l'élève = 9/10.

# In[38]:


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

# Commentaire de correction : le programme buge si on introduit a = 0.


# CEYLAN Yoyan : Note de l'élève = 9.5/10

# In[44]:


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
            
# Commentaire de correction : Ton code tient bien du cas a = 0 mais ne précise qu'on se ramène au 
# premier degré.


# CANAI Othmane : Note de l'élève = 9/10.

# In[49]:


from math import* #importer les fonctions mathématiques à utiliser
#ax^2+bx+c

a = float(input("Donner la valeur de a="))#Valeur de a
b = float(input("Donner la valeur de b="))#Valeur de b
c = float(input("Donner la valeur de c="))#Valeur de c
if a == 0:
    if b == 0:
        if c == 0:
            print("La solution est impossible dans l'ensemble IR")
else :
  Delta = b**2-(4*a*c)
  print("Delta=",Delta)
if (Delta<0) :
  print("pas de solutions réelles possibles")
if (Delta==0):
  print("une seule solutuion possible:")
  X0 = -b/2*a
  print(X0)
if (Delta>0):
  print("deux solutions réelles possibles")
  X1 = (-b-sqrt(Delta))/2*a
  X2 = (-b+sqrt(Delta))/2*a
  print(X1,X2)

# Commentaire de correction : le programme ne tient pas compte a = 0.


# CHHEM Nérilyne : Note de l'élève = 6/10.

# In[56]:



from math import *

a=float(input("Donner la valeur de a"))
b=float(input("Donner la valeur de b"))
c=float(input("Donner la valeur de c"))
delta=b**2-4*a*c
print("delta =",delta)
if delta==0:
    print("il y a une solution reelle distincte:",-b/2*a)
# allignement des if's !
if delta < 0:
        print("il n'y a pas de solution reelle")
if delta > 0:
            print("il y a 2 solutions reelles distinctes:",(-b+sqrt(delta))/2*a,"et",(-b-sqrt(delta))/2*a)
            
# Commentaire de coorection : Le code ne donne pas d'informations si Delta < 0 et Delta > 0.
# Il ne tient pas compte également de la valeur a = 0.
# Le premier problème se règle en alignant les deux derniers "if".
# Si tu importes *, tu n'as besoin de "math.sqrt(...)".


# DELGADO Jessica : Note de l'élève = 9/10.

# In[63]:


from math import *
print("")
a = float(input("Donner la valeur de a: a="))
b = float(input("Donner la valeur de b: b="))
c = float(input("Donner la valeur de c: c="))
print("")
print("Le polynôme est donnée par: P(x) =", a , "x^2 +",b ,"x +",c)
print("")
Delta = b**2 - 4*a*c
print("Delta=", Delta)
print("")
if Delta > 0:
    print("Alors, l'équation du polynôme admet 2 solutions réelles distinctes:")
    x1 = (-b-sqrt(Delta))/2*a
    x2 = (-b+sqrt(Delta))/2*a
    print("x1 = ",x1," et x2 = ",x2)
if Delta==0:
    print("Alors, l'équation du polynôme admet une unique solution réelle:")
    x0=-b/(2*a)
    print("x0 = ",x0)
if Delta<0:
    print("Alors, l'équation du polynôme n'amet pas de solution réelle.")

# Commentaire de correction : Le code ne tent pas de la valeur a = 0.


# DUFONT Fléna : Note de l'élève = 4/10.

# In[71]:


from math import *
def equation(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta<0:
        msg = "il n'y a pas de solution" # mettre le message ici d'abord !
        return msg # retourne msg après.
    x=(-b-delta**0.5)/(2*a)
    y=(-b+delta**0.5)/(2*a)
    if delta>0:
        return(x,y)
    if delta==0:
        x = -b/2*a # cette ligne d'abord, sinon
        return(x)  # que contient la variable x ici ?

a=float(input("mettre a:")) # float(input (....)) pour préciser le type réel de : a
b=float(input("mettre b:")) # float(input (....)) pour préciser le type réel de : b
c=float(input("mettre c:")) # float(input (....)) pour préciser le type réel de : c

# print(equation(-4,6,9)) # A l'appel de la fonction, mettre a, b , c pas de valeurs que les trois variables.

print(equation(a,b,c)) # comme ça !

# En plus des commentaires sur code, il faut noter qu'il tient pas compte de a = 0.


# ETTALII Aya : Note de l'élève = 8/10.

# In[76]:


from math import * # line oublé dans le code mais obligatoire ! 

a=float( input ("donner a : "))
b=float(input("donner b : "))
c=float( input ("donner c : "))

if a==0 :
    if b==0:
        if c==0:
            print(" Tout rel est une solution ")
        else:
            print("il y a pas de solution ")
    else:
            print(" la solution : " , -b/a )
else:
    DELTA=pow(b,2)-4*a*c 
    if DELTA>0: 
        print (" il y a deux solutions : " , (-b-sqrt(DELTA))/(2*a ), " et " , (-b+sqrt(DELTA))/(2*a) )
    if DELTA==0 :
        print(" il y a une seule solution :" , -b/2*a)
    if DELTA<0 : 
        print(" il y a pas de solution " )
# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme !


# FERGE Mélina : Note de l'élève = 9.5/10.

# In[92]:


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
    
#La valeur de a = 0 prise en compte mais tu ne précises pas que tu passes au premier degré.


# FREIRRA Thomas : Note de l'élève = 9/10

# In[97]:


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

# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme !


# BENZAOUIA Nassim : Note de l'élève = 3/10.

# In[106]:


from math import * # oublié mais obligatoire !

a =float(input("quel est la valeur de a")) # float(input (....)) pour préciser le type réel de : a
b =float(input("quel est la valeur de b")) # float(input (....)) pour préciser le type réel de : b
c =float(input("quel est la valeur de c")) # float(input (....)) pour préciser le type réel de : c
delta =(b*b) - (4*a*c)
if delta < 0: 
	print("pas de resolution possible dans les reels")

elif delta > 0: 
    x1 =(-b + sqrt(delta))/2*a # 2*a au de 2a     
    x2 =(-b - sqrt(delta))/2*a # 2*a au de 2a     
    print("les deux réponses sont:",x1, "et",x2)

elif delta ==0:     
     print("une seul réponse:", -b/2*a) # 2*a au lieu de 2a.
else:
	print("erreur de programmation")

# En plus des commentaires sur code, il faut noter qu'il tient pas compte de a = 0.


# MAHIOUS Rayan : Note de l'élève = 9/10.

# In[112]:


from math import *
a=float(input("donner a:"))
b=float(input("donner b:"))
c=float(input("donner c:"))
x1=float()
x2=float()
D=(b**2)-(4*a*c)
print("Delta=",D)
if D<0:
    print("il n'y a pas de solution réelle.")
if D==0:
    print("Il y a une solution réelle :")
    x0=(-b)/(2*a)
    print("x0=",x0)
if D>0:
    print("Il y a deux solutions réelles :")
    x1=(-b-sqrt(D))/(2*a)
    x2=(-b+sqrt(D))/(2*a)
    print("x1=",x1)
    print("x2=",x2)

# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme !


# MAZOUZ Amine : Note de l'élève = 8/10.

# In[119]:


from math import *
print("soit ax**2+bx+c une fontion de degré 2 avec")
a=int(input("a "))
b=int(input("b "))
c=int(input("c "))
delta=int(b*b-(4*a*c))
print("delta vaut",delta)
if delta==0: 
      x=-b/2*a 
      print("x vaut",x)
elif delta>0:
        x1=(-b-(sqrt(delta)))/2*a 
        x2=(-b+(sqrt(delta)))/2*a 
        print("x1 et x2 vallent",x1,"et",x2)
elif delta<0:
      print("il n'y a pas de solutions")

# Commentaire de correction : Attention à l'allignement des conditions if.
# Tenir compte de la valeur a = 0 dans le programme !


# OUJIAD Camélia : Note de l'élève = 5/10.

# In[126]:


from math import * # * oublie  par l'eleve mais obligatoire ici.

print("")

a=float(input("inserer la valeur de a: a="))

b=float(input("inserer la valeur de b: b="))

c= float(input("insererla valeur de c: c="))

print("")

print("ce polynôme est exprimée par: P(x) =", a , "x^2 +",b ,"x +",c, "=0")

print("")

Delta=b**2 - 4*a*c

print("Delta=", Delta)

print("")

if Delta>0:

    print("Alors cette équation du polynôme admet 2 solutions réelles distinctes:")

    x1=(-b-sqrt(Delta))/2*a

    x2=(-b+sqrt(Delta))/2*a

    print("x1 = ",x1," et x2 = ",x2)

if Delta==0 : # pas de parenthèses entre Delta et == : Delta(==0)

    print("Alors cette equation du polynôme admet une seule et unique solution réelle:")

    x0=-b/(2*a)

    print("x0 = ",x0)

if Delta<0:

    print("Alors cette equation du polynôme n'amet aucune solution réelle.")
    
# Commentaire de correction : Aucun alinéas respecté apès la condition if = problème de stucture !
# En plus des commentaires sur le code, il ne tient pas compte de la valeur a = 0.


# TANDOUNA Nathan : Note de l'élève = 8/10.

# In[133]:


from math import *
a=float(input("Donner la valeur de a : "))
b=float(input("Donner la valeur de b : "))
c=float(input("Donner la valeur de c : "))
if a==0:
    if b==0:
        if c==0:
            print("Tout réel est une solution")
        else:
            print("Pas de solution")
    else:
    	print("La solution est : ",-b/a)
else:
    Delta=pow(b,2)-4*a*c
    print("Delta = ",Delta)
    if Delta<0:
	    print("Il n'y a pas de solution dans R")
    if Delta==0:
	    print("La solution est : ",-b/2*a)
    if Delta>0:
	    print("Deux solutions : ",(-b-sqrt(Delta))/2*a," et ",(-b+sqrt(Delta))/2*a) # Deux fois -b là --> (-b-b+sqrt(Delta))/2*a) 
        
# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme !


# TASCI Mathieu : Note de l'élève = 9/10.

# In[138]:


from math import *


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))


def equation(a, b, c):
    print("L'équation est : ", a, "x² + ", b, "x + ", c)
    Delta = (b ** 2) - (4 * a * c)
    print("Delta =", Delta)
    if Delta < 0:
        print("Le discriminant est inférieur à 0, il n y a pas de solution.")
    elif Delta == 0:
        print("Le discriminant est égal à 0, il y a une solution:")
        x0 = (- b) / (2 * a)
        print ("x0 =", x0)
    else:
        print("Le discriminant est supérieur à 0, il y a deux solutions:")
        x1 = (- b - sqrt(Delta)) / (2 * a)
        x2 = (- b + sqrt(Delta)) / (2 * a)
        print ("x1 =", x1)
        print ("x2 =", x2)
equation(a, b, c)

# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme sinon il va buger !


# TKITEK bilel : Note de l'élève = 9/10.

# In[144]:


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
    
# Commentaire de correction : Tenir compte de la valeur a = 0 dans le programme sinon il va buger !


# # Correction du projet rendu : TP du chapitre 1 (Second degré).

# In[1]:


from math import *
print("")
a = float(input('valeur de a = '))
b = float(input('valeur de b = '))
c = float(input('valeur de c = '))
if a != 0:
    print("")
    print("Le polynôme est donné par : P(x) = ",a,'x^2 + ',b,'x + (',c,")")
    print("")
    Delta = b**2 - 4*a*c
    print("Delta = ",Delta)
    print("")
    if Delta < 0:
        print('Pas de solutions réelles.')
    elif Delta == 0:
        x_0 = -b/(2*a)
        print('Une unique soluttion.')
        print("")
        print('x_0 =',x_0)
    else:
        print('Deux solutions réelles distinctes.')
        x_1 = (-b - sqrt(Delta))/(2*a)
        x_2 = (-b + sqrt(Delta))/(2*a)
        print("")
        print("x_1 = ",x_1," et x_2 = ",x_2)
else:
    print('')
    print('La valeur de a doit être différent de zéro.')


# # Jeux du nombre magique (code amélioré)

# Description : Deviner le nombre magique donné par l'ordinateur entre 1 et 20.

# In[ ]:


from random import randint # randint genere aleatoirement un nombre entier 

magic_number = randint(1,20) # Donner un entier au hasard entre 1 et 20.
guess_number = int(input("Devine le nombre magic ? \n magic_number = "))
while guess_number != magic_number :
    print(" Ouppps !!!")
    print("")
    if magic_number <= guess_number :
        print("Donne une valeur plus petie ?")
        guess_number = int(input("Devine encore ? \n magic_number = "))
    else:
        print("Donne une valeur plus grande ?")
        guess_number = int(input("Devine encore ? \n magic_number = "))
    print("")

