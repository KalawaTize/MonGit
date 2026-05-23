
class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.livres_empruntes = []

    def peut_emprunter(self):
        # Méthode par défaut, sera surchargée
        return len(self.livres_empruntes) < 5

    def __str__(self):
        return f"{self.prenom} {self.nom}"
