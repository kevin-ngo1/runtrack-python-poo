class Ville():
    def __init__(self,nom="",nombre=0):
        self.__nom=nom
        self.__nombre=nombre

class Personne():
    def __init__(self,nom="",age=0,objet=""):
        self.__nom=nom
        self.__age=age
        self.__objet=objet

    def ajouterPopulation(self):
        self.__objet._Ville__nombre +=1

ville_paris=Ville("Paris",1000000)
ville_marseille=Ville("Marseille",861635)

print("Population de la ville de Paris :",ville_paris._Ville__nombre)
print("Population de la ville de Marseille :",ville_marseille._Ville__nombre)

personne1=Personne("John",45,ville_paris)
personne2=Personne("Myrtille",4,ville_paris)
personne3=Personne("Chloe",18,ville_marseille)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print("Mise a jour de la population de la ville de Paris :",ville_paris._Ville__nombre)
print("Mise a jour de la population de la ville de Marseille :",ville_marseille._Ville__nombre)





