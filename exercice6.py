mot_cache ="python"
tentatives = 5
for _ in range(tentatives):
    mot = input("Devinez le mot cache : ").lower()
    if mot == mot_cache:
        print("Bravo")
        break
    else:
        print("Essayez encore !")

