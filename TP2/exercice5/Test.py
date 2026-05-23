
import Bibliotheque
import Etudiant
import Professeur




def main():
    biblio = Bibliotheque()
    
    # Création de quelques utilisateurs pour le test
    user1 = Etudiant("Dupont", "Jean")
    user2 = Professeur("Martin", "Sophie")

    while True:
        print("\n=== GESTION BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre (Standard)")
        print("2. Ajouter un livre (Académique)")
        print("3. Afficher le catalogue (Pandas)")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("6. Supprimer un livre (Opérateur -)")
        print("7. Stats rapides (Numpy)")
        print("8. Quitter")
        
        choix = input("Votre choix : ")

        if choix == '1':
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            biblio + Livre(titre, auteur) # Utilisation de l'opérateur +

        elif choix == '2':
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            domaine = input("Domaine : ")
            biblio + LivreAcademique(titre, auteur, domaine)

        elif choix == '3':
            biblio.afficher_catalogue()

        elif choix == '4':
            titre = input("Titre du livre à emprunter : ")
            print("Qui emprunte ? (1: Etudiant, 2: Professeur)")
            u_choix = input("> ")
            user = user1 if u_choix == '1' else user2
            biblio.emprunter_livre(titre, user)

        elif choix == '5':
            titre = input("Titre du livre à retourner : ")
            print("Qui retourne ? (1: Etudiant, 2: Professeur)")
            u_choix = input("> ")
            user = user1 if u_choix == '1' else user2
            biblio.retourner_livre(titre, user)

        elif choix == '6':
            titre = input("Titre du livre à supprimer : ")
            biblio - titre # Utilisation de l'opérateur -

        elif choix == '7':
            # Exemple d'utilisation de Numpy pour des stats simples
            if len(biblio._Bibliotheque__catalogue) > 0:
                # Compter les livres disponibles vs empruntés
                disponibles = [1 for l in biblio._Bibliotheque__catalogue if l.disponible]
                empruntes = [0 for l in biblio._Bibliotheque__catalogue if not l.disponible]
                
                arr = np.array(disponibles + empruntes)
                print(f"Total livres : {np.count_nonzero(arr == 1) + np.count_nonzero(arr == 0)}")
                print(f"Disponibles : {np.count_nonzero(arr == 1)}")
            else:
                print("Catalogue vide.")

        elif choix == '8':
            print("Sauvegarde finale...")
            biblio.sauvegarder_donnees()
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


    if __name__ == "__main__":
        main()
def run_tests_automatiques():
    print("\n--- DÉBUT DES TESTS AUTOMATIQUES ---")
    
    # 1. Test des Classes de base
    l1 = Livre("Titre 1", "Auteur 1")
    assert l1.titre == "Titre 1", "Erreur: Attribut titre incorrect"
    assert l1.disponible == True, "Erreur: Livre doit être disponible par défaut"
    print("[OK] Classe Livre")

    # 2. Test de l'héritage (LivreAcademique)
    l2 = LivreAcademique("Titre 2", "Auteur 2", "Maths")
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
# run_tests_automatiques()

