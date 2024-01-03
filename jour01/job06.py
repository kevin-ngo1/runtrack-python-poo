class Animal():
    def __init__(self, prenom="",age=0):
        self.age=age
        self.prenom=prenom

    def vieillir(self):
        self.age=int(input("Quel est l'age de votre animal ? "))
        print("L'age de l'animal ",self.age)
        self.age += 1
        print("L'animal a vielli, l'age de l'animal",self.age,"ans")

    def nommer(self):
        self.prenom=input("Entrez le nom de votre animal : ")
        print("L'animal se nomme",self.prenom)
        

mon_animal = Animal()
mon_animal.vieillir()
mon_animal.nommer()

    