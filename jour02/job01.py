class Rectangle():
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self,Longueur):
        self.__longueur=Longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self,Largeur):
        self.__largeur=Largeur
    
rectangle1=Rectangle(10,5)
print("Mon rectangle est de longueur",rectangle1.get_longueur(),"cm et de largeur",rectangle1.get_largeur(),"cm")
rectangle1.set_longueur(30)
rectangle1.set_largeur(25)
print("Mon rectangle est de longueur",rectangle1.get_longueur(),"cm et de largeur",rectangle1.get_largeur(),"cm")