import Utilisateur

class Etudiant(Utilisateur):
    def peut_emprunter(self):
        # Limitation : 3 livres max
        return len(self.livres_empruntes) < 3
    
    