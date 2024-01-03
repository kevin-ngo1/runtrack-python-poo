from math import pi

class Cercle():
    def __init__(self,rayon):
        self.rayon=rayon

    def changerRayon(self):
        self.rayon=int(input("Entrez le nouveau rayon : "))
        return self.rayon
    
    def afficherInfos(self):
        print("Rayon :",self.rayon,"\nCirconférence :",self.circonférence(),"\nAire :",self.aire(),"\nDiamètre :",self.diametre())

    def circonférence(self):
        return 2*pi*self.rayon
    
    def aire(self):
        return pi*(self.rayon**2)

    def diametre(self):
        return 2*self.rayon
    
cercle1=Cercle(4)
cercle1.afficherInfos()
cercle1.changerRayon()
cercle1.afficherInfos()
        