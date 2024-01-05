class Personne():
    def __init__(self,age=14):
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

class Professeur():
    def __init__(self,matiereEnseignée=""):
        self.matiereEnseignée=matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")

personne1=Personne()
eleve1=Eleve()
eleve1.afficherAge()
