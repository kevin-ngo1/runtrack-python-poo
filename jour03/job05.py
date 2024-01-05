import random

class Personnage():
    def __init__(self, nom="", vie=0):
        self.nom = nom
        self.vie = vie

    def attaquer(self, personnage):
        degats = random.randint(5, 10)
        print(self.nom,"attaque",personnage.nom,"et lui inflige",degats,"points de dégâts.")
        personnage.vie -= degats

class Jeu():
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Niveau de difficulté (1,2,3) : "))

    def lancerJeu(self):
        niveaux_vie = {1:50, 2:75, 3:100}
        vie_joueur = niveaux_vie[self.niveau]
        vie_ennemi = niveaux_vie[self.niveau]

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print("Vous avez tué l'ennemi, BRAVO !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print("Vous avez perdu, NUL !")
                break

        print("FIn du conbat, Votre vie :",joueur.vie,"Ennemi Vie :",ennemi.vie)

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
