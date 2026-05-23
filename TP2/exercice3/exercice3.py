import pandas as pd
import numpy as np
import os
import string
import random
import json




def analyse_sequences(liste, seuil=5):
    """
    - Prend une liste contenant des entiers et des sous-listes imbriquées.
    - Extrait les sous-listes dont la somme dépasse le seuil.
    - Renvoie ces sous-listes triées par longueur décroissante.
    """
    # Extraire uniquement les éléments qui sont des listes
    sous_listes = [elem for elem in liste if isinstance(elem, list)]

    # Filtrer celles dont la somme dépasse le seuil
    filtrees = [sl for sl in sous_listes if sum(sl) > seuil]

    # Trier par longueur décroissante
    filtrees.sort(key=lambda x: len(x), reverse=True)

    return filtrees


def test_exercice3():
    """Test de la fonction analyse_sequences."""
    print("\n" + "=" * 60)
    print("EXERCICE 3 — ANALYSE DE SÉQUENCES")
    print("=" * 60)

    resultat = analyse_sequences([[1, 2], [3, 4, 5], [10], [1, 1, 1, 1]], seuil=5)
    print(f"  analyse_sequences([[1,2], [3,4,5], [10], [1,1,1,1]], seuil=5)")
    print(f"  Résultat : {resultat}")
    # Attendu : [[3,4,5], [10]]

    resultat2 = analyse_sequences([[100], [1, 2, 3, 4, 5], [0], [10, 20]], seuil=10)
    print(f"\n  analyse_sequences([[100], [1,2,3,4,5], [0], [10,20]], seuil=10)")
    print(f"  Résultat : {resultat2}")
    # Attendu : [[1,2,3,4,5], [10,20], [100]]


test_exercice3()

