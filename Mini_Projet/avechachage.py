import bcrypt

USER_FILE = "users.txt"

def save_user(username, password):
    """Ajoute un utilisateur avec un mot de passe sécurisé."""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed_password.decode()}\n")

        
###2. Vérification des mots de passe hachés
def authenticate1(username, password):
    """Vérifie les identifiants avec un mot de passe haché."""
    with open(USER_FILE, "r") as f:
        for line in f:
            user, hashed_pwd = line.strip().split(":")
            if user == username and bcrypt.checkpw(password.encode(), hashed_pwd.encode()):
                return True
    return False
###3. Empêcher les attaques par force brute
###Implémentez un compteur de tentatives de connexion :

login_attempts = {}

def authenticate2(username, password):
    """Vérifie les identifiants avec une limitation des tentatives."""
    global login_attempts
    if username in login_attempts and login_attempts[username] >= 3:
        print("Compte temporairement bloqué.")
        return False

    with open(USER_FILE, "r") as f:
        for line in f:
            user, hashed_pwd = line.strip().split(":")
            if user == username and bcrypt.checkpw(password.encode(), hashed_pwd.encode()):
                login_attempts[username] = 0
                return True

    login_attempts[username] = login_attempts.get(username, 0) + 1
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
            if authenticate2(username, password):
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