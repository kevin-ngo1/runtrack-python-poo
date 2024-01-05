class Joueur():
    def __init__(self,nom,numero,position,buts_marqués,passe_d,carton_jaune,carton_rouge):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts_marqués=buts_marqués
        self.passe_d=passe_d
        self.carton_jaune=carton_jaune
        self.carton_rouge=carton_rouge

    def marquerUnBut(self):
        self.buts_marqués+=1

    def effectuerUnePasseDecisive(self):
        self.passe_d+=1

    def recevoirUnCartonJaune(self):
        self.carton_jaune+=1

    def recevoirUnCartonRouge(self):
        self.carton_rouge+=1

    def afficherStatistiques(self):
        return f"Le joueur : {self.nom} \nNuméro : {self.numero} \nPosition : {self.position} \nStatistiques : {self.buts_marqués} buts / {self.passe_d} passes décisives / {self.carton_jaune} cartons jaunes / {self.carton_rouge} cartons rouges"
    
class Equipe():
    def __init__(self,nom_equipe):
        self.nom_equipe=nom_equipe
        self.liste_joueur=[]

    def ajouterJoueur(self,new_joueur):
        self.liste_joueur.append(new_joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueur:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self,player_edit):
        for joueur in self.liste_joueur:
            if joueur == player_edit:
                joueur.marquerUnBut()
                joueur.recevoirUnCartonJaune()

joueur1 = Joueur("Messi", 10, "Attaquant", 746, 1000, 47, 1)
joueur2 = Joueur("Ronaldo", 7, "Attaquant", 829, 500, 30, 2)
joueur3 = Joueur("Griezmann", 7, "Attaquant", 462, 652, 20, 3)
joueur4 = Joueur("Mbappé", 9, "Attaquant", 758, 500, 10, 1)

equipe1 = Equipe("OM")
equipe2 = Equipe("PSG")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

joueur1.marquerUnBut()
joueur2.recevoirUnCartonRouge()
joueur3.effectuerUnePasseDecisive()
joueur4.recevoirUnCartonJaune()

equipe1.mettreAJourStatistiquesJoueur(joueur1)
equipe1.mettreAJourStatistiquesJoueur(joueur2)
equipe2.mettreAJourStatistiquesJoueur(joueur3)
equipe2.mettreAJourStatistiquesJoueur(joueur4)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

