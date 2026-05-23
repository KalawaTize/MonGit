import Livre

class LivreAcademique(Livre):
    
    def __init__(self, titre, auteur, domaine, disponible=True):
        super().__init__(titre, auteur, disponible)
        self.domaine = domaine

    def afficher_info(self):
        # Surcharge pour inclure le domaine
        base_info = super().afficher_info()
        return f"{base_info} - Domaine: {self.domaine}"