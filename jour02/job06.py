class Commande:
    def __init__(self, numero_commande=0, liste_plat={}, statut=""):
        self.__numero_commande = numero_commande
        self.__liste_plat = liste_plat
        self.__statut = statut

    def add_plat(self, nom, prix):
        if self.__statut == "en cours":
            self.__liste_plat[nom] = prix

    def canceled_commande(self):
        self.__statut = "annulée"
        print("Vous avez annulé la commande")

    def __total_prix(self):
        return sum(self.__liste_plat.values())

    def afficher_commande(self):
        print("Numéro de commande:",self.__numero_commande,"\nLes plats commandés :")
        for plat, prix in self.__liste_plat.items():
            print(plat,"~",prix,"euros")
        print("Prix total avec TVA de 20% :",self.__total_prix()+self.tva(),"euro \nStatut :",self.__statut)

    def tva(self):
        return self.__total_prix()*0.2
    

    
commande_1 = Commande(1, {}, "en cours")

commande_1.add_plat("Pizza", 7)
commande_1.add_plat("Salade", 3)

commande_1.afficher_commande()
commande_1.canceled_commande()
commande_1.add_plat("Patate", 2)
commande_1.afficher_commande()


