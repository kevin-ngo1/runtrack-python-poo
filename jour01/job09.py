class Produit():
    def __init__(self, nom="",prixHT=0,TVA=0):
        self.nom=nom
        self.prixHT=prixHT
        self.TVA=TVA

    def CalculerPrixTTC(self):
        return self.prixHT*(1+(self.TVA/100))

    def afficher(self):
        return f"Le nom du produit : {self.nom}\nLe prix HT : {self.prixHT} euros\nLa TVA : {self.TVA}% \nLe prix TTC : {self.CalculerPrixTTC()} euros"

    def modifierNom(self):
        self.nom=input("Entrez le nom du produit : ")
        return self.nom
    
    def afficherNom(self):
        return self.nom
    
    def modifierPrix(self):
        self.prixHT=int(input("Entrez le prix du produit : "))
        return self.prixHT

    def afficherPrix(self):
        return self.prixHT
    
produit1=Produit("Biberon",10,20)
print(produit1.afficher())
produit1.modifierNom()
produit1.modifierPrix()
print(produit1.afficher())



    

    

