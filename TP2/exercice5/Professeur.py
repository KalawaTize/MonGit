import Utilisateur

class Professeur(Utilisateur):
    def peut_emprunter(self):
        # Limitation : 10 livres max
        return len(self.livres_empruntes) < 10

