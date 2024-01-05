class CompteBancaire():
    def __init__(self,numero,nom,prenom,solde,decouvert=True):
        self.__numero=numero
        self.__nom=nom
        self.__prenom=prenom
        self.__solde=solde
        self.__decouvert=decouvert

    def afficher(self):
        print("Numéro du compte :",self.__numero,"\nNom :",self.__nom,"\nPrénom :",self.__prenom,"\nSolde :",self.__solde)

    def afficherSolde(self):
        print("Solde du compte :",self.__solde)

    def versement(self,add_solde):
            self.__solde+=add_solde

    def retrait(self,take_solde):
        if self.__solde >= take_solde or self.__decouvert:
            self.__solde-=take_solde
        else :
            print("Vous n'avez pas assez d'argent pour retirer",take_solde,"euros")

    def agios(self):
        if self.__solde <0:
            self.__solde*=1.05

    def virement(self,reference,destinataire,montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            destinataire.versement(montant)
            print("Un virement de",montant,"euros a été effectué au destinataire :",destinataire.__prenom,destinataire.__nom,"\nRéférence :",reference)
        else:
            print("Impossible de faire un virement, vous n'avez pas assez d'argent")

compte1 = CompteBancaire("123456789", "Dupont", "Alice", 500)
compte2 = CompteBancaire("987654321", "Smith", "John", -300)

compte1.afficher()
compte2.afficher()
compte1.retrait(100)
compte1.agios()
compte2.agios()
compte1.afficherSolde()
compte1.virement("Remboursement",compte2, 315)
compte1.afficherSolde()
compte2.afficherSolde()

        
            
        



    

        