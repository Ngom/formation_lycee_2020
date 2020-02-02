a =input("quel est la valeur de a") 
b =input("quel est la valeur de b") 
c =input("quel est la valeur de c") 
delta =(b*b) - (4*a*c)
if delta < 0: 
	print "pas de resolution possible dans les reels"

elif delta > 0: 
    x1 =(-b + sqrt(delta))/2a    
    x2 =(-b - sqrt(delta))/2a     
    print "les deux réponses sont:",x1, "et",x2

elif delta ==0:     
     print "une seul réponse:", -b/2a
else:
	print "erreur de programmation"