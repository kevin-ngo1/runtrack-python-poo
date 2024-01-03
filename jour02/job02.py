class Livre():
    def __init__(self,titre="",auteur="",nombre=0):
        self.__titre=titre
        self.__auteur=auteur
        self.__nombre=nombre

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

livre1=Livre("Berlin","Kevin",32)
print("Le livre s'appelle",livre1.get_titre(),"par",livre1.get_auteur(),"avec",livre1.get_nombre(),"pages")
livre1.set_auteur("Mowgli")
livre1.set_titre("Oui-Oui")
livre1.set_nombre(-10)
print("Le livre s'appelle",livre1.get_titre(),"par",livre1.get_auteur(),"avec",livre1.get_nombre(),"pages")
livre1.set_nombre(12)
print("Le livre s'appelle",livre1.get_titre(),"par",livre1.get_auteur(),"avec",livre1.get_nombre(),"pages")