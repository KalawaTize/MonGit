import random
import Carte



class Paquet:
    """Représente un paquet de cartes."""

    def __init__(self, cartes=None):
        if cartes is None:
            self.cartes = []
        else:
            self.cartes = list(cartes)

    def __str__(self):
        if not self.cartes:
            return ""
        return "".join(str(c) + " ; " for c in self.cartes)

    def __len__(self):
        return len(self.cartes)

    def ajoute_carte(self, carte):
        """Ajoute une carte à la fin du paquet."""
        self.cartes.append(carte)

    def enleve_carte(self, carte):
        """Supprime une carte du paquet."""
        self.cartes.remove(carte)

    def repositionne_carte(self):
        """Déplace la première carte du paquet à la fin."""
        if self.cartes:
            carte = self.cartes.pop(0)
            self.cartes.append(carte)

    def premiere_carte(self):
        """Retourne la première carte sans la retirer."""
        if self.cartes:
            return self.cartes[0]
        return None

    def piocher(self):
        """Retire et retourne la première carte du paquet."""
        if self.cartes:
            return self.cartes.pop(0)
        return None


def creer_jeu_complet():
    """Crée un jeu complet de 52 cartes."""
    motifs = ["coeur", "carreau", "pique", "trèfle"]
    jeu = []
    for motif in motifs:
        for valeur in range(2, 15):  # 2 à 14 (as)
            jeu.append(Carte.Carte(valeur, motif))
    return jeu


def distribuer_cartes():
    """Distribue 8 cartes à chaque joueur."""
    jeu = creer_jeu_complet()
    random.shuffle(jeu)
    paquet_joueur = Paquet(jeu[:8])
    paquet_ordi = Paquet(jeu[8:16])
    return paquet_joueur, paquet_ordi


def jouer_bataille():
    """Lance une partie de bataille simplifiée."""
    print("\n" + "=" * 60)
    print("JEU DE BATAILLE SIMPLIFIÉ")
    print("=" * 60)

    paquet_joueur, paquet_ordi = distribuer_cartes()
    print(f"\nVotre paquet  : {paquet_joueur}")
    print(f"Paquet ordi   : {paquet_ordi}")
    print("-" * 60)
    input("Appuyer sur Entrée pour commencer les combats...")

    for combat in range(1, 11):
        print(f"\n--- Combat {combat} ---")

        carte_joueur = paquet_joueur.piocher()
        carte_ordi = paquet_ordi.piocher()

        if carte_joueur is None or carte_ordi is None:
            print("Un des joueurs n'a plus de cartes !")
            break

        print(f"  Vous jouez  : {carte_joueur}")
        print(f"  Ordi joue   : {carte_ordi}")

        if carte_joueur == carte_ordi:
            print(" Égalité ! Chacun récupère sa carte.")
            paquet_joueur.ajoute_carte(carte_joueur)
            paquet_ordi.ajoute_carte(carte_ordi)
        elif carte_joueur < carte_ordi:
            print("L'ordinateur gagne ce combat !")
            paquet_ordi.ajoute_carte(carte_ordi)
            paquet_ordi.ajoute_carte(carte_joueur)
        else:
            print("Vous gagnez ce combat !")
            paquet_joueur.ajoute_carte(carte_joueur)
            paquet_joueur.ajoute_carte(carte_ordi)

        print(f"  Cartes restantes — Vous : {len(paquet_joueur)} | Ordi : {len(paquet_ordi)}")
        input("Appuyer sur Entrée pour continuer...")

    # Résultat final
    print("\n" + "=" * 60)
    print("RÉSULTAT FINAL")
    print(f"  Vos cartes  : {len(paquet_joueur)}")
    print(f"  Cartes ordi : {len(paquet_ordi)}")

    if len(paquet_joueur) > len(paquet_ordi):
        print("VOUS AVEZ GAGNÉ !")
    elif len(paquet_joueur) < len(paquet_ordi):
        print("L'ORDINATEUR A GAGNÉ !")
    else:
        print("MATCH NUL !")
    print("=" * 60)
