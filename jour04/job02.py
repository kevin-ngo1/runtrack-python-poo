class Personne():
    def __init__(self,age):
        self.age=age
    
    def afficherAge(self):
        print("Age :",self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self,new_age):
        self.age=new_age

class Eleve(Personne):
    def __init__(self,age=14):
        Personne.__init__(self,age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai",self.age,"ans")

class Professeur(Personne):
    def __init__(self,matiereEnseignée,age=14):
        Personne.__init__(self,age)
        self.matiereEnseignée=matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")


eleve1=Eleve()
professeur1=Professeur("SVT")
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()
professeur1.modifierAge(40)
professeur1.bonjour()
professeur1.enseigner()


