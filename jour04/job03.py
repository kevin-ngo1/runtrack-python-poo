class Rectangle():
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self,new):
        self.__longueur=new
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self,new):
        self.__largeur=new

    def perimetre(self):
        return (self.__longueur+self.__largeur)*2
    
    def surface(self):
        return self.__longueur*self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self,hauteur,longueur,largeur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur=hauteur

    def volume(self):
        return self.get_longueur()*self.get_largeur()*self.hauteur
    
rectangle1=Rectangle(2.5,4)
parallelepipede1=Parallelepipede(10,2.5,4)
print("Perimètre du rectangle :",rectangle1.perimetre())
print("Surface du rectangle :",rectangle1.surface())
print("Le volume du parallelipede :",parallelepipede1.volume())
