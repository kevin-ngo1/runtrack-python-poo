class Tache():
    def __init__(self, titre="", description="", statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches():
    def __init__(self):
        self.taches = []

    def ajouterTache(self, new_tache):
        self.taches.append(new_tache)

    def supprimerTache(self, remove_tache):
        self.taches.remove(remove_tache)

    def marquerCommeFinie(self, fini_tache):
        if fini_tache.statut == "à faire":
            fini_tache.statut="terminée"

    def afficherListe(self):
        affichage=[(tache.titre, tache.description, tache.statut) for tache in self.taches]
        return affichage

    def filterListe(self, statut):
        filtrer = [(tache.titre, tache.description, tache.statut) for tache in self.taches if tache.statut == statut]
        return filtrer

tache1 = Tache("Ménage", "Faire le ménage de ta chambre")
tache2 = Tache("Code", "Reviser le code")
tache3 = Tache("Achat", "Acheter un téléphone")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("\nListe complète des tâches :\n",liste_taches.afficherListe())

liste_taches.supprimerTache(tache2)
liste_taches.marquerCommeFinie(tache3)

print("\nListe complète des tâches :\n",liste_taches.afficherListe())

print("\nListe complète des tâches filtré par 'à faire' :\n",liste_taches.filterListe("à faire"))



    

    

