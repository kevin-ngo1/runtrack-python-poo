class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def afficherLesPoints(self):
        print("Coordonnée de x :",self.x,"\nCoordonnée de y :",self.y)

    def afficherX(self):
        print("Coordonée de x :",self.x)

    def afficherY(self):
        print("Coordonée de y :",self.y)

    def changerX(self):
        self.x = int(input("Changer la valeur de x : "))
        return self.x
    
    def changerY(self):
        self.y = int(input("Changer la valeur de y : "))
        return self.y

point1=Point(20,16)
point1.afficherLesPoints()
point1.changerX()
point1.changerY()
point1.afficherX()
point1.afficherY()
point1.afficherLesPoints()
