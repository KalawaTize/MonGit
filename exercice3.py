a=float(input("Entrer la premiere longueur : "))
b=float(input("Entrer la deuxieme longueur : "))
c=float(input("Entrer la troisieme longueur : "))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Triangle Equilateral")
    elif a==b or a==c or b==c:
        print("Triangle Isocele")
    else:
        print("Triangle Scalaire")
else:
    print("Les longueurs ne forment pas un triangle")
