                                                                                                                     
def analyse_texte(texte):
    """
    Analyse un texte donné :
    1. Compte le nombre total de mots.
    2. Identifie le mot le plus fréquent et son nombre d'occurrences.
    3. Retourne un dictionnaire contenant la fréquence de chaque mot.
    4. Ignore la ponctuation et la casse.
    """
    # Nettoyage : mise en minuscules et suppression de la ponctuation
    texte_nettoye = texte.lower()
    for char in string.punctuation:
        texte_nettoye = texte_nettoye.replace(char, "")

    # Découpage en mots
    mots = texte_nettoye.split()

    # 1. Nombre total de mots
    nombre_total = len(mots)

    # 3. Fréquence de chaque mot (dictionnaire)
    frequence = {}
    for mot in mots:
        frequence[mot] = frequence.get(mot, 0) + 1

    # 2. Mot le plus fréquent
    mot_plus_frequent = max(frequence, key=frequence.get)
    occurrences_max = frequence[mot_plus_frequent]

    # Affichage des résultats
    print("\n" + "=" * 60)
    print("ANALYSE DE TEXTE")
    print("=" * 60)
    print(f"  # Nombre total de mots : {nombre_total}")
    print(f"  # Mot le plus fréquent : '{mot_plus_frequent}' ({occurrences_max} fois)")
    print(f"  # Fréquence des mots : {frequence}")

    return frequence





def test_exercice2():
    """Test de la fonction analyse_texte."""

    texte = "Python est génial. Python est puissant. Apprendre Python est intéressant!"
    analyse_texte(texte)


test_exercice2()


