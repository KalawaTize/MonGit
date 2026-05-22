salaire_brut=float(input("Entrez votre salaire brut : "))
if salaire_brut >= 3000:
    taxe = 0.20
else:
    taxe = 0.15
salaire_net = salaire_brut * (1-taxe)
print(f"Salaire net apres impot : {salaire_net:.2f} $")