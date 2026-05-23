import os

# Fichier de stockage des utilisateurs
USER_FILE = "users.txt"
# Liste d'utilisateurs pré-enregistrés avec leurs mots de passe
DEFAULT_USERS = [
    ("alice", "password123"),
    ("bob", "securepass"),
    ("charlie", "admin123"),
    ("david", "mypassword"),
]

def create_user_file():
    """Créer le fichier users.txt s'il n'existe pas."""
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            for username, password in DEFAULT_USERS:
                f.write(f"{username}:{password}\n")    
        print("Fichier users.txt créé avec succès.")
    else:
        print("Le fichier users.txt existe déjà.")

def save_user(username, password):
    """Ajoute un utilisateur dans le fichier (méthode vulnérable)."""
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{password}\n")


def authenticate(username, password):
    """Vérifie si les identifiants existent (méthode vulnérable)."""
    with open(USER_FILE, "r") as f:
        for line in f:
            user, pwd = line.strip().split(":")
            if user == username and pwd == password:
                return True
    return False

def search_user(query):
    """Recherche un utilisateur contenant la chaîne entrée (vulnérable à l'injection)."""
    with open(USER_FILE, "r") as f:
        return [line.strip() for line in f if query in line]

def main():
    while True:
        print("\n1. Inscrire un utilisateur")
        print("2. Se connecter")
        print("3. Rechercher un utilisateur")
        print("4. Quitter")
        choice = input("Votre choix : ")

        if choice == "1":
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            save_user(username, password)
            print("Utilisateur ajouté avec succès.")

        elif choice == "2":
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            if authenticate(username, password):
                print("Connexion réussie.")
            else:
                print("Identifiants incorrects.")

        elif choice == "3":
            query = input("Rechercher : ")
            results = search_user(query)
            print("Résultats :", results)

        elif choice == "4":
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
