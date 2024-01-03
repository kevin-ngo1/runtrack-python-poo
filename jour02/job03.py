class Livre():
    def __init__(self,titre="",auteur="",nombre=0,disponible=True):
        self.__titre=titre
        self.__auteur=auteur
        self.__nombre=nombre
        self.__disponible=disponible

    def get_titre(self):
        return self.__titre
    
    def set_titre(self,Titre):
        self.__titre=Titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self,Auteur):
        self.__auteur=Auteur

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,Nombre):
        if Nombre > 0:
            self.__nombre=Nombre
        else :
            print("Le nombre de page doit être supérieur à 0")

    def verification(self):
        if self.__disponible:
            return True
        return False

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre est disponible, Vous avez emprunté le livre")
            return True
        print("Le livre n'est pas disponible, vous ne pouvez pas emprunter")
        return False

    def rendre(self):
        if self.emprunter() == False:
            self.__disponible=True
            print("Vous avez rendu le livre")
        else :
            print("Vous n'avez pas de livre à rendre")


livre1=Livre("Berlin","Kevin",32)
print("Le livre s'appelle",livre1.get_titre(),"par",livre1.get_auteur(),"avec",livre1.get_nombre(),"pages")
livre1.emprunter()
print("Le livre s'appelle",livre1.get_titre(),"par",livre1.get_auteur(),"avec",livre1.get_nombre(),"pages")
livre1.rendre()
livre1.emprunter()

