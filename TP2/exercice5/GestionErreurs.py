def LivreNonTrouveError(Exception):
    """Levée quand un livre n'est pas trouvé dans le catalogue."""
    pass

def LivreIndisponibleError(Exception):
    """Levée quand un livre est déjà emprunté."""
    pass

def LimitePretAtteinte(Exception):
    """Levée quand un utilisateur dépasse sa limite d'emprunts."""
    pass
