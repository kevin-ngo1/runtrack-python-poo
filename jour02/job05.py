class Voiture():
    def __init__(self, marque,modele,annee,kilometrage,en_marche=True,reservoir=50):
        self.__marque=marque
        self.__modele=modele
        self.__annee=annee
        self.__kilometrage=kilometrage
        self.__en_marche=en_marche
        self.__reservoir=reservoir


    def get_marque(self):
        return self.__marque
    
    def set_marque(self,Marque):
        self.__marque=Marque

    def get_modele(self):
        return self.__modele
    
    def set_modele(self,Modele):
        self.__modele=Modele 

    def get_annee(self):
        return self.__annee
    
    def set_annee(self,Annee):
        self.__annee=Annee  

    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_annee(self,Kilometrage):
        self.__kilometrage=Kilometrage

    def get_en_marche(self):
        return self.__en_marche
    
    def set_en_marche(self,En_marche):
        self.__en_marche=En_marche    

    def demarrer(self):
        if self.__verifier_plein() >5:
            self.__en_marche = True
            return "La voiture a démarré"
        else :
            return "La voiture a un réservoir trop bas pour démarrer"

    def arreter(self):
        self.__en_marche = False
        return "La voiture est arreté"

    def __verifier_plein(self):
        return self.__reservoir
    
voiture1=Voiture("Fiat","Panda Hybrid","2020",10000)

print("Voiture :",voiture1.get_marque(),voiture1.get_modele(),"\nAnnée :",voiture1.get_kilometrage(),"\nKilometrage :",voiture1.get_annee(),"\nReservoir :",voiture1._Voiture__verifier_plein(),"\nEn marche :",voiture1.get_en_marche())
print(voiture1.demarrer())
print(voiture1.arreter())
print("Voiture :",voiture1.get_marque(),voiture1.get_modele(),"\nAnnée :",voiture1.get_kilometrage(),"\nKilometrage :",voiture1.get_annee(),"\nReservoir :",voiture1._Voiture__verifier_plein(),"\nEn marche :",voiture1.get_en_marche())
