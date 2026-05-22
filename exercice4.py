n=int(input("Entrez un nombre :"))
if n < 2:
    print("Non premier")
else:
    premier = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            premier = False
            break

        if premier:
            print("Nombre premier")
        else:
            print("Non premier")