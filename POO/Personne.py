class Personne:
    """Creation d'une classe Personne """
    def __init__(self, nom:str, age:int):
        self.__nom = nom
        self.__age = age

    def se_presenter(self):
        print(f"Bonjour, je m'apprele {self.nom} et j'ai {self.age} ans")

    def __del__(self):
        print("L'objet a ete supprime") 

    def get_nom(self):
        return 






p1 = Personne("Jean", 28)
p1.se_presenter()



