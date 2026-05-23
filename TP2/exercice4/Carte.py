
class Carte:
    """Représente une carte à jouer."""

    """Dictionnaire pour les valeurs spéciales des cartes."""
    NOMS_SPECIAUX = {11: "valet", 12: "dame", 13: "roi", 14: "as"}

    """Initialisation de la carte avec une valeur et un motif."""
    def __init__(self, valeur, motif):
        self.valeur = valeur
        self.motif = motif

    """Représentation textuelle de la carte."""
    def __str__(self):
        nom_valeur = self.NOMS_SPECIAUX.get(self.valeur, str(self.valeur))
        return f"{nom_valeur} de {self.motif}"

    """Comparaison de cartes basée sur leur valeur."""
    def __lt__(self, other):
        return self.valeur < other.valeur
    
    """Égalité de cartes basée sur leur valeur."""
    def __eq__(self, other):
        return self.valeur == other.valeur

    """Représentation officielle de la carte (identique à la représentation textuelle)."""
    def __repr__(self):
        return self.__str__()
