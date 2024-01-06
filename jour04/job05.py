from math import pi

class Forme():
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur

    def aire(self):
        return self.largeur*self.hauteur
    
class Cercle(Forme):
    def __init__(self,radius):
        self.radius=radius

    def aire(self):
        return pi*self.radius**2


rectangle1=Rectangle(2,4)
cercle1=Cercle(5)
print("Aire du rectangle :",rectangle1.aire())
print("Aire du cercle :",cercle1.aire())
