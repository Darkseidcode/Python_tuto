

#--- DEFINITION ---
'''
Dans toutes les methode d'instance, 
il faut mettre self en parametre et 
. pour appeler les variables d'instance
'''
class Personne: #Convention P en majuscule
    def __init__(self, nom: str = "", age: int = 0): #Constructeur
        self.nom = nom # on def la variable d'instance self.la variable = à la varible pour pouvoir la réutiliser dans la classe
        self.age = age # Création de variable d'instance age
        if nom == "":
            self.DemanderLeNom()
            print("Constructeur personne : " + self.nom)

        if age == 0:
            self.Demanderage()
            print("Constructeur personne : " + str(self.age))



    def SePresenter(self): 
        info_personne = "Bonjour, je m'appelle " + self.nom #concatenation de chaine de caractère
        if self.age != 0 : #si l'age est different de 0 alors on affiche l'age
            info_personne += " et j'ai " + str(self.age) + " ans" #concatenation de chaine de caractère
        print(info_personne) #affichage des informations
        print("Je suis majeur" if self.Estmajeur() else "Je suis mineur") #affichage si la personne est majeur ou mineur
        print("--"*20) #delimiteur

    def Estmajeur(self):
        return self.age >= 18 # retour True si age >= 18 sinon False

    def DemanderLeNom(self):
        self.nom = input("Quel est votre nom ? ") #demande le nom de la personne

    def Demanderage(self):
        self.age = int(input("Quel est votre age ? ")) #demande l'age de la personne

# --- UTILISATION ---
'''Creation de personnes, nous allons creer plusieur personnes
Les infos qui sont dans les parenthèses sont les parametres de la methode __init__

A la place de input, on peut mettre des variable 
ou autre pour definir les parametres,
provenant d'une base de donnée par exemple 
ou d'un information utilisateur d'une interface etc...

Donc la création de personnes permet de mettre les information des personnes
dans les variables d'instance de la classe Personne dans les parametres __init__, le construteur.

Ensuite on utilise la methode SePresenter pour afficher les informations des personnes
dans la console.

'''

personne1 = Personne() #Creation personne
# personne2 = Personne() #Creation personne

# personne3 = Personne()

''''Presentation des personnes'''
personne1.SePresenter()
# personne2.SePresenter() #methode d'instance
# personne3.SePresenter()