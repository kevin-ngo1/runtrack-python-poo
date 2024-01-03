class Student():
    def __init__(self,prenom="",nom="",numero_etudiant=0,nombre_credit=0):
        self.__nom=nom
        self.__prenom=prenom
        self.__numero_etudiant=numero_etudiant
        self.__nombre_credit=nombre_credit
        self.__level=self.__studentEval()

    def add_credits(self,add):
        if add > 0:
            self.__nombre_credit+= add
        else:
            print("Ajouter un nombre de crédits valide (supérieur à 0)")

    def __studentEval(self):
        if self.__nombre_credit >= 90:
            return "Excellent"
        elif self.__nombre_credit >= 80:
            return "Très bien"
        elif self.__nombre_credit >= 70:
            return "Bien"
        elif self.__nombre_credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print("Nom =",self.__nom,"\nPrénom =",self.__prenom,"\nid =",self.__numero_etudiant,"\nNiveau =",self.__level)


    

    
student1=Student("Doe","John",145)
student1.add_credits(10)
student1.add_credits(10)
student1.add_credits(10)
print("Le nombre de crédits de",student1._Student__nom,student1._Student__prenom,"est de",student1._Student__nombre_credit)
student1.studentInfo()



    
