import random

class Carte():
    def __init__(self,valeur,couleur,only_player=None):
        self.valeur=valeur
        self.couleur=couleur
        self.only_player=only_player
        self.as_traite=False
    
    def valeur_carte(self):
        valeur_cartes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

        if self.valeur == 'A' and not self.as_traite and self.only_player == 'joueur':
            as_choice = input("Vous voulez 1 ou 11 pour l'As ? ")
            if as_choice == '1':
                self.as_traite=True
                return 1
            else:
                self.as_traite=True
                return 11
        return valeur_cartes[self.valeur]
    
class Jeu():
    def __init__(self,paquet=[],main_joueur=[],main_croupier=[]):
        self.paquet=paquet
        self.main_joueur=main_joueur
        self.main_croupier=main_croupier
        self.start_paquet()
        self.start_game()

    def start_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def start_game(self):
        for i in range(2):
            self.piocher(self.main_joueur)

        total = sum(carte.valeur_carte() for carte in self.main_joueur)

        print("Voici votre jeu :", [f"{carte.valeur} de {carte.couleur}" for carte in self.main_joueur], "\nLa valeur de votre main est :", total)

        
        while True:
            add_carte=input("Voulez vous piocher ? (Y/N) ")
            if add_carte == "Y":
                self.piocher(self.main_joueur)
                total = sum(carte.valeur_carte() for carte in self.main_joueur)
                print("Voici votre jeu :", [f"{carte.valeur} de {carte.couleur}" for carte in self.main_joueur], "\nLa valeur de votre main est :", total)

            else :
                total_croupier=self.croupier()
                break

        if total_croupier>21:
            print("Vous avez gagné le croupier a depassé les 21")
        else :
            if total_croupier>total:
                print("Vous avez perdu ! Le croupier a une plus grande valeur que vous")
            else : 
                print("Vous avez gagné ! Votre valeur est plus grande que celle du croupier")

    def piocher(self,who):
        carte_tiree = random.choice(self.paquet)
        self.paquet.remove(carte_tiree)
        who.append(carte_tiree)

    def croupier(self):
        total_croupier=0
        while total_croupier <= 17:
            self.piocher(self.main_croupier)
            total_croupier = sum(carte.valeur_carte() for carte in self.main_croupier)
        else :
            print("Le jeu du croupier :", [f"{carte.valeur} de {carte.couleur}" for carte in self.main_croupier], "\nLa valeur du croupier est :", total_croupier)
            return total_croupier

jeu_blackjack = Jeu()


