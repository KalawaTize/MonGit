# ============================================================
# FICHIER DE TEST COMPLET - EXERCICE 5
# ============================================================

# Importer les classes depuis votre fichier principal
# (adaptez le nom selon votre fichier)
import os
import json
import Livre
import LivreAcademique

# Supprime l'ancien catalogue pour repartir de zéro
if os.path.exists("catalogue.json"):
    os.remove("catalogue.json")
    print("🗑️  Ancien catalogue supprimé\n")

# ---- Copier/coller ici toutes vos classes OU faire : ----
# from hawa_lom_TP2 import Livre, LivreAcademique, Bibliotheque, Etudiant, Professeur

# ============================================================
# TEST 1 : Création d'objets Livre
# ============================================================
print("=" * 50)
print("TEST 1 : Création de Livres")
print("=" * 50)

l1 = Livre.Livre("Les Misérables", "Victor Hugo")   
l2 = Livre.Livre("1984", "George Orwell")
l3 = LivreAcademique.LivreAcademique("Introduction aux algorithmes",
                      "Cormen et al.", "Informatique")

print(l1)
print(l2)
print(l3)

# Vérifications
assert l1.titre == "Les Misérables"
assert l1.auteur == "Victor Hugo"
assert l1.disponible == True           # disponible par défaut
assert l3.domaine == "Informatique"

print("✅ TEST 1 PASSÉ\n")


# ============================================================
# TEST 2 : Méthode afficher_info()
# ============================================================
print("=" * 50)
print("TEST 2 : afficher_info()")
print("=" * 50)

print("-- Livre simple --")
l1.afficher_info()

print("\n-- Livre Académique --")
l3.afficher_info()

print("✅ TEST 2 PASSÉ\n")


# ============================================================
# TEST 3 : changer_disponibilite()
# ============================================================
print("=" * 50)
print("TEST 3 : Changement de disponibilité")
print("=" * 50)

l1.changer_disponibilite(False)
assert l1.disponible == False
print(f"Après emprunt    : {l1}")

l1.changer_disponibilite(True)
assert l1.disponible == True
print(f"Après retour     : {l1}")

print("✅ TEST 3 PASSÉ\n")


# ============================================================
# TEST 4 : Création des Utilisateurs
# ============================================================
print("=" * 50)
print("TEST 4 : Création d'Utilisateurs")
print("=" * 50)

etudiant  = Etudiant("Diallo", "Fatou")
professeur = Professeur("Dubois", "Claire")

print(etudiant)
print(professeur)

# Vérification des limites
assert etudiant._limite_pret == 3
assert professeur._limite_pret == 7

print(f"Limite étudiant  : {etudiant._limite_pret} livres")
print(f"Limite professeur: {professeur._limite_pret} livres")

print("✅ TEST 4 PASSÉ\n")


# ============================================================
# TEST 5 : Création de la Bibliothèque
# ============================================================
print("=" * 50)
print("TEST 5 : Création de la Bibliothèque")
print("=" * 50)

bib = Bibliotheque()
print("Bibliothèque créée avec succès")
print("✅ TEST 5 PASSÉ\n")


# ============================================================
# TEST 6 : Ajout de livres (méthode + opérateur)
# ============================================================
print("=" * 50)
print("TEST 6 : Ajout de livres")
print("=" * 50)

# Via méthode classique
bib.ajouter_livre(l1)
bib.ajouter_livre(l2)
bib.ajouter_livre(l3)

# Via opérateur surchargé +
l4 = LivreAcademique("Mécanique Quantique",
                      "Cohen-Tannoudji", "Physique")
bib + l4
print("Opérateur + utilisé avec succès")

print("✅ TEST 6 PASSÉ\n")


# ============================================================
# TEST 7 : Affichage du catalogue
# ============================================================
print("=" * 50)
print("TEST 7 : Affichage du catalogue")
print("=" * 50)

bib.afficher_catalogue()
print("✅ TEST 7 PASSÉ\n")


# ============================================================
# TEST 8 : Ajout d'utilisateurs + Emprunt
# ============================================================
print("=" * 50)
print("TEST 8 : Emprunt de livres")
print("=" * 50)

bib.ajouter_utilisateur(etudiant)
bib.ajouter_utilisateur(professeur)

# Emprunt normal
bib.emprunter_livre("Les Misérables", etudiant)
assert not l1.disponible
assert "Les Misérables" in etudiant.livres_empruntes
print(f"Après emprunt : {l1}")

# Emprunt par professeur
bib.emprunter_livre("1984", professeur)
print(f"Après emprunt : {l2}")

print("✅ TEST 8 PASSÉ\n")


# ============================================================
# TEST 9 : Cas d'erreur - Emprunt d'un livre déjà emprunté
# ============================================================
print("=" * 50)
print("TEST 9 : Erreurs d'emprunt")
print("=" * 50)

# Livre déjà emprunté
try:
    bib.emprunter_livre("Les Misérables", professeur)
    print("❌ Erreur : exception non levée !")
except RuntimeError as e:
    print(f"✅ Exception correcte : {e}")

# Livre inexistant
try:
    bib.emprunter_livre("Livre Fantôme", etudiant)
    print("❌ Erreur : exception non levée !")
except ValueError as e:
    print(f"✅ Exception correcte : {e}")

print("✅ TEST 9 PASSÉ\n")


# ============================================================
# TEST 10 : Limite de prêt (Étudiant = 3 livres max)
# ============================================================
print("=" * 50)
print("TEST 10 : Limite de prêt")
print("=" * 50)

l5 = Livre("Dune", "Frank Herbert")
l6 = Livre("Fondation", "Isaac Asimov")
l7 = Livre("Neuromancien", "William Gibson")

bib.ajouter_livre(l5)
bib.ajouter_livre(l6)
bib.ajouter_livre(l7)

# L'étudiant emprunte jusqu'à la limite
bib.emprunter_livre("Dune", etudiant)
bib.emprunter_livre("Fondation", etudiant)

# 3ème emprunt → doit échouer (déjà 1 + 2 = 3)
try:
    bib.emprunter_livre("Neuromancien", etudiant)
    print("❌ Erreur : la limite n'est pas respectée !")
except RuntimeError as e:
    print(f"✅ Limite atteinte correctement : {e}")

etudiant.afficher_emprunts()
print("✅ TEST 10 PASSÉ\n")


# ============================================================
# TEST 11 : Retour de livre
# ============================================================
print("=" * 50)
print("TEST 11 : Retour de livres")
print("=" * 50)

bib.retourner_livre("Les Misérables", etudiant)
assert l1.disponible == True
assert "Les Misérables" not in etudiant.livres_empruntes
print(f"Après retour : {l1}")

# Retourner un livre non emprunté → erreur
try:
    bib.retourner_livre("Les Misérables", etudiant)
    print("❌ Erreur : exception non levée !")
except RuntimeError as e:
    print(f"✅ Exception correcte : {e}")

print("✅ TEST 11 PASSÉ\n")


# ============================================================
# TEST 12 : Suppression de livre (méthode + opérateur -)
# ============================================================
print("=" * 50)
print("TEST 12 : Suppression de livres")
print("=" * 50)

# Via méthode
bib.supprimer_livre("Les Misérables")

# Via opérateur -
bib - "Neuromancien"
print("Opérateur - utilisé avec succès")

# Supprimer un livre emprunté → erreur
try:
    bib.supprimer_livre("1984")   # emprunté par professeur
    print("❌ Erreur : exception non levée !")
except RuntimeError as e:
    print(f"✅ Exception correcte : {e}")

print("✅ TEST 12 PASSÉ\n")


# ============================================================
# TEST 13 : Statistiques (Pandas + NumPy)
# ============================================================
print("=" * 50)
print("TEST 13 : Statistiques")
print("=" * 50)

bib.statistiques()
print("✅ TEST 13 PASSÉ\n")


# ============================================================
# TEST 14 : Persistance des données (JSON)
# ============================================================
print("=" * 50)
print("TEST 14 : Persistance JSON")
print("=" * 50)

assert os.path.exists("catalogue.json"), "Fichier JSON non créé !"

with open("catalogue.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Livres sauvegardés dans JSON : {len(data)}")
for item in data:
    print(f"  - {item['titre']} | Disponible: {item['disponible']}")

print("✅ TEST 14 PASSÉ\n")


# ============================================================
# BILAN FINAL
# ============================================================
print("\n" + "🎉" * 25)
print("   TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS !")
print("🎉" * 25)