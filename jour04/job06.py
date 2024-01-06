class Vehicule():
    def __init__(self,marque="",modele="",annee=0,prix=0):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :",self.marque,"\nModèle :",self.modele,"\nAnnée :",self.annee,"\nPrix :",self.prix)

class Voiture(Vehicule):
    def __init__(self,marque="",modele="",annee=0,prix=0,portes=4):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.portes=portes

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de portes :",self.portes)

class Moto(Vehicule):
    def __init__(self,marque="",modele="",annee=0,prix=0,roue=2):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.roue=roue

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de roues :",self.roue)


voiture1=Voiture("Mazda", "RX-7", 1996, 50000)
moto1=Moto("Kawasaki","Ninja ZX-10R",2024,21000)
voiture1.informationsVehicule()
moto1.informationsVehicule()

