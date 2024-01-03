#1ere méthode
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        res=self.nombre1+self.nombre2
        return res

test = Operation(12,3)
print("Le resultat est",test.addition())

#2eme méthode
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        res=self.nombre1+self.nombre2
        print("Le resultat est",res)

test = Operation(12,3)
test.addition()