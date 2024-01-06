class Forme():
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur

    def aire(self):
        return self.largeur*self.hauteur

rectangle1=Rectangle(2,4)
print(rectangle1.aire())
