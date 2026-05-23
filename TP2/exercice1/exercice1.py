
import pandas as pd
import numpy as np
import os
import string
import random
import json




#Déclaration des constantes
FICHIER_CSV = "resultats.csv"
COLONNES_NOTES = ["Math", "Physique", "Français", "Informatique"]

#création du fichier csv avec les données initiales
def creer_fichier_csv():
    """Crée le fichier resultats.csv avec les données initiales."""
    contenu = """Nom,Prenom,Math,Physique,Français,Informatique
Diallo,Fatou,85,78,92,88
Nguyen,Minh,62,71,65,70
Smith,John,45,50,48,42
Dubois,Claire,91,89,94,90
Lopez,Ana,72,68,74,70
Bencheikh,Yanis,55,60,58,59
Tremblay,Julie,88,84,86,87
Kouassi,Adama,40,35,38,42
Khan,Amir,95,92,90,94
Zhao,Wei,77,80,75,79"""
    with open(FICHIER_CSV, "w", encoding="utf-8") as f:
        f.write(contenu)
    print(f"Fichier '{FICHIER_CSV}' créé avec succès.")

# Charger les données du fichier CSV et gérer les erreurs
def charger_donnees():
    """Charge le fichier CSV et retourne un DataFrame. Gère les erreurs."""
    try:
        df = pd.read_csv(FICHIER_CSV)
        # Vérifier que les colonnes attendues sont présentes
        colonnes_attendues = ["Nom", "Prenom"] + COLONNES_NOTES
        for col in colonnes_attendues:
            if col not in df.columns:
                print(f"Erreur : La colonne '{col}' est manquante dans le fichier.")
                return None
        print(f"Fichier '{FICHIER_CSV}' chargé avec succès ({len(df)} élèves).")
        return df
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{FICHIER_CSV}' est introuvable.")
        print("   Création automatique du fichier...")
        creer_fichier_csv()
        return pd.read_csv(FICHIER_CSV)
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None
    
# Afficher les statistiques descriptives pour chaque matière
def afficher_statistiques(df):
    """Calcule et affiche les statistiques descriptives pour chaque matière."""
    print("\n" + "=" * 60)
    print("STATISTIQUES DESCRIPTIVES PAR MATIÈRE")
    print("=" * 60)
    for matiere in COLONNES_NOTES:
        notes = df[matiere]
        print(f"\n{matiere} :")
        print(f"   Moyenne    : {notes.mean():.2f}")
        print(f"   Médiane    : {notes.median():.2f}")
        print(f"   Écart-type : {notes.std():.2f}")
        print(f"   Min        : {notes.min()}")
        print(f"   Max        : {notes.max()}")
        input("Appuyer sur Entrée pour continuer...")
       

# Afficher les élèves dont la moyenne est supérieure à la moyenne générale
def afficher_bons_eleves(df):
    """Identifie et affiche les élèves au-dessus de la moyenne générale."""
    print("\n" + "=" * 60)
    print("ÉLÈVES AU-DESSUS DE LA MOYENNE GÉNÉRALE")
    print("=" * 60)
    df["Moyenne"] = df[COLONNES_NOTES].mean(axis=1)
    moyenne_generale = df["Moyenne"].mean()
    print(f"\n   Moyenne générale de la classe : {moyenne_generale:.2f}\n")

    bons_eleves = df[df["Moyenne"] > moyenne_generale]
    if bons_eleves.empty:
        print("   Aucun élève au-dessus de la moyenne générale.")
    else:
        for _, eleve in bons_eleves.iterrows():
            print(f"{eleve['Prenom']} {eleve['Nom']} — Moyenne : {eleve['Moyenne']:.2f}")
        print("Appuyer sur Entrée pour continuer...")
        input()
    # Nettoyer la colonne temporaire
    df.drop(columns=["Moyenne"], inplace=True, errors="ignore")
    return bons_eleves
   

# Ajouter un nouvel étudiant au DataFrame et sauvegarder les modifications dans le fichier CSV
def ajouter_etudiant(df):
    """Ajoute un nouvel étudiant au DataFrame et sauvegarde."""
    nom = input("   Nom : ").strip()
    prenom = input("   Prénom : ").strip()
    try:
        math = float(input("   Note Math : "))
        physique = float(input("   Note Physique : "))
        francais = float(input("   Note Français : "))
        informatique = float(input("   Note Informatique : "))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return df
    nouvelle_ligne = pd.DataFrame({
        "Nom": [nom], "Prenom": [prenom],
        "Math": [math], "Physique": [physique],
        "Français": [francais], "Informatique": [informatique]
    })
    df = pd.concat([df, nouvelle_ligne], ignore_index=True)
    df.to_csv(FICHIER_CSV, index=False)
    print(f"{prenom} {nom} ajouté avec succès.")
    return df

# Supprimer un étudiant du DataFrame et sauvegarder les modifications dans le fichier CSV
def supprimer_etudiant(df):
    """Supprime un étudiant par son nom et prénom."""
    print("\n--- Suppression d'un étudiant ---")
    nom = input("   Nom de l'étudiant à supprimer : ").strip()
    prenom = input("   Prénom : ").strip()
    masque = (df["Nom"] == nom) & (df["Prenom"] == prenom)
    if masque.any():
        df = df[~masque].reset_index(drop=True)
        df.to_csv(FICHIER_CSV, index=False)
        print(f"{prenom} {nom} supprimé avec succès.")
    else:
        print(f"Étudiant '{prenom} {nom}' introuvable.")
    return df

# Modifier les notes d'un étudiant existant et sauvegarder les modifications dans le fichier CSV
def modifier_notes(df):
    """Modifie les notes d'un étudiant existant."""
    print("\n--- Modification des notes ---")
    nom = input("   Nom de l'étudiant : ").strip()
    prenom = input("   Prénom : ").strip()
    masque = (df["Nom"] == nom) & (df["Prenom"] == prenom)
    if not masque.any():
        print(f"Étudiant '{prenom} {nom}' introuvable.")
        return df
    try:
        print("   (Laissez vide pour ne pas modifier)")
        for matiere in COLONNES_NOTES:
            note_actuelle = df.loc[masque, matiere].values[0]
            nouvelle = input(f"   {matiere} (actuel: {note_actuelle}) : ").strip()
            if nouvelle:
                df.loc[masque, matiere] = float(nouvelle)
        df.to_csv(FICHIER_CSV, index=False)
        print("Notes modifiées avec succès.")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    return df



def menu_exercice1():
    """Menu interactif pour l'exercice 1."""
    if not os.path.exists(FICHIER_CSV):
        creer_fichier_csv()

    df = charger_donnees()

    while True:
        print("\n" + "=" * 60)
        print("MENU — ANALYSE DES RÉSULTATS SCOLAIRES")
        print("=" * 60)
        print("  1. Afficher les statistiques descriptives")
        print("  2. Afficher les bons élèves (> moyenne générale)")
        print("  3. Ajouter un étudiant")
        print("  4. Supprimer un étudiant")
        print("  5. Modifier les notes d'un étudiant")
        print("  6. Afficher toutes les données")
        print("  0. Quitter")
        choix = input("\n  Votre choix : ").strip()

        if choix == "1":
            afficher_statistiques(df)
        elif choix == "2":
            afficher_bons_eleves(df)
        elif choix == "3":
            df = ajouter_etudiant(df)
        elif choix == "4":
            df = supprimer_etudiant(df)
        elif choix == "5":
            df = modifier_notes(df)
        elif choix == "6":
            print("\n", df.to_string(index=False))
            input("Appuyer sur Entrée pour continuer...")
        elif choix == "0":
            print("Retour au menu principal.")
            break
        else:
            print("Choix invalide.")


#charger_donnees()
#df = charger_donnees()
#afficher_statistiques(df)


menu_exercice1()

#creer_fichier_csv()
    