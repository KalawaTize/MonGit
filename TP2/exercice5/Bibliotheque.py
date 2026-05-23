#import pandas as pd
#import numpy as np
import os
import Livre
import LivreAcademique


class Bibliotheque:


    def __init__(self, nom_fichier_save="bibliotheque_data.csv"):
        self.__nom_fichier = nom_fichier_save
        self.__catalogue = [] # Liste d'objets Livre
        
        # Chargement des données si le fichier existe
        if os.path.exists(self.__nom_fichier):
            self.charger_donnees()

    def ajouter_livre(self, livre):
        self.__catalogue.append(livre)
        self.sauvegarder_donnees()
        print(f"Le livre '{livre.titre}' a été ajouté.")

    def supprimer_livre(self, titre):
        # Recherche du livre
        livre_a_supprimer = None
        for livre in self.__catalogue:
            if livre.titre == titre:
                livre_a_supprimer = livre
                break
        
        if livre_a_supprimer:
            self.__catalogue.remove(livre_a_supprimer)
            self.sauvegarder_donnees()
            print(f"Le livre '{titre}' a été supprimé.")
        else:
            print(f"Livre '{titre}' introuvable.")

    def emprunter_livre(self, titre, utilisateur):
        if not utilisateur.peut_emprunter():
            print(f"Erreur : {utilisateur} a atteint sa limite d'emprunt.")
            return

        for livre in self.__catalogue:
            if livre.titre == titre:
                if livre.disponible:
                    livre.changer_disponibilite(False)
                    utilisateur.livres_empruntes.append(titre)
                    self.sauvegarder_donnees()
                    print(f"Succès : {utilisateur} a emprunté '{titre}'.")
                    return
                else:
                    print(f"Échec : Le livre '{titre}' est déjà emprunté.")
                    return
        print(f"Livre '{titre}' introuvable dans la bibliothèque.")

    def retourner_livre(self, titre, utilisateur):
        for livre in self.__catalogue:
            if livre.titre == titre:
                if not livre.disponible:
                    livre.changer_disponibilite(True)
                    if titre in utilisateur.livres_empruntes:
                        utilisateur.livres_empruntes.remove(titre)
                    self.sauvegarder_donnees()
                    print(f"Succès : '{titre}' a été retourné.")
                    return
                else:
                    print(f"Erreur : Le livre '{titre}' n'était pas emprunté.")
                    return
        print(f"Livre '{titre}' introuvable.")

    def afficher_catalogue(self):
        # UTILISATION DE PANDAS POUR L'AFFICHAGE
        if not self.__catalogue:
            print("Le catalogue est vide.")
            return

        # Conversion de la liste d'objets en liste de dictionnaires pour Pandas
        data = []
        for livre in self.__catalogue:
            entry = {
                "Titre": livre.titre,
                "Auteur": livre.auteur,
                "Disponible": "Oui" if livre.disponible else "Non",
                "Type": "Académique" if isinstance(livre, LivreAcademique) else "Standard"
            }
            if isinstance(livre, LivreAcademique):
                entry["Domaine"] = livre.domaine
            else:
                entry["Domaine"] = "-"
            data.append(entry)

        df = pd.DataFrame(data)
        print("\n--- CATALOGUE DE LA BIBLIOTHÈQUE ---")
        print(df.to_string(index=False)) # Affichage propre sans index
        print("------------------------------------\n")

    # Persistance des données avec Pandas
    def sauvegarder_donnees(self):
        data = []
        for livre in self.__catalogue:
            entry = {
                "titre": livre.titre,
                "auteur": livre.auteur,
                "disponible": livre.disponible,
                "type": "Academique" if isinstance(livre, LivreAcademique) else "Standard"
            }
            if isinstance(livre, LivreAcademique):
                entry["domaine"] = livre.domaine
            else:
                entry["domaine"] = None
            data.append(entry)
        
        df = pd.DataFrame(data)
        df.to_csv(self.__nom_fichier, index=False)

    def charger_donnees(self):
        try:
            df = pd.read_csv(self.__nom_fichier)
            self.__catalogue = []
            for index, row in df.iterrows():
                if row['type'] == 'Academique':
                    livre = LivreAcademique(row['titre'], row['auteur'], row['domaine'], row['disponible'])
                else:
                    livre = Livre(row['titre'], row['auteur'], row['disponible'])
                self.__catalogue.append(livre)
        except Exception as e:
            print(f"Erreur lors du chargement : {e}")

    # ==========================================
    # SURCHARGE DES OPÉRATEURS (Étape 4)
    # ==========================================
    def __add__(self, livre):
        """Permet : bibliotheque + livre"""
        self.ajouter_livre(livre)
        return self

    def __sub__(self, titre_livre):
        """Permet : bibliotheque - 'Titre du livre' """
        self.supprimer_livre(titre_livre)
        return self

# ==========================================
# MENU INTERACTIF ET TESTS
# ==========================================

def run_tests_automatiques():
    print("\n--- DÉBUT DES TESTS AUTOMATIQUES ---")
    
    # 1. Test des Classes de base
    l1 = Livre.Livre("Titre 1", "Auteur 1")
    assert l1.titre == "Titre 1", "Erreur: Attribut titre incorrect"
    assert l1.disponible == True, "Erreur: Livre doit être disponible par défaut"
    print("[OK] Classe Livre")

    # 2. Test de l'héritage (LivreAcademique)
    l2 = LivreAcademique.LivreAcademique("Titre 2", "Auteur 2", "Maths")
    assert l2.domaine == "Maths", "Erreur: Domaine incorrect"
    assert isinstance(l2, Livre), "Erreur: LivreAcademique doit hériter de Livre"
    print("[OK] Classe LivreAcademique et Héritage")

    # 3. Test de la Bibliothèque et Opérateurs
    biblio = Bibliotheque("test_temp.csv")
    
    # Test opérateur + (Ajout)
    biblio + l1
    biblio + l2
    assert len(biblio._Bibliotheque__catalogue) == 2, "Erreur: Ajout via + échoué"
    print("[OK] Opérateur + (Ajout)")

    # Test opérateur - (Suppression)
    biblio - "Titre 1"
    assert len(biblio._Bibliotheque__catalogue) == 1, "Erreur: Suppression via - échoué"
    print("[OK] Opérateur - (Suppression)")

    # 4. Test Emprunt / Disponibilité
    user = Etudiant("Test", "User")
    # On réajoute le livre pour tester l'emprunt
    biblio + l1 
    biblio.emprunter_livre("Titre 1", user)
    
    # Vérifier que le livre n'est plus disponible
    livre_emprunte = None
    for l in biblio._Bibliotheque__catalogue:
        if l.titre == "Titre 1": livre_emprunte = l
    
    assert livre_emprunte.disponible == False, "Erreur: Le livre devrait être indisponible"
    assert "Titre 1" in user.livres_empruntes, "Erreur: Le livre devrait être dans la liste de l'user"
    print("[OK] Emprunt et Changement de statut")

    # 5. Test Persistence (CSV)
    assert os.path.exists("test_temp.csv"), "Erreur: Le fichier CSV n'a pas été créé"
    print("[OK] Sauvegarde CSV (Pandas)")

    # Nettoyage du fichier test
    os.remove("test_temp.csv")

    print("--- TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS ---\n")

# Pour lancer les tests, décommente la ligne ci-dessous :
run_tests_automatiques()
