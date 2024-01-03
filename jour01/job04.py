class Personne():
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return self.prenom, self.nom
    
personne1=Personne("John","Doe")
personne2=Personne("Jean","Dupond")
print("Je suis",*personne1.SePresenter())
print("Je suis",*personne2.SePresenter())