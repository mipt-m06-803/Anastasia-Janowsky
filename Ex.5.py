a = float(input("Vvedite a "))
b = float(input("Vvedite b "))
c = float(input("Vvedite c "))
D = b**2 - 4*a*c
if a == 0:
    print("Korney ne zavezli :(")
x1 = ((-1)*b - D**(1/2)) / (2*a)
x2 = ((-1)*b + D**(1/2)) / (2*a)
if x1 != x2:
    l = [x1, x2]
    X1 = max(l)
    X2 = min(l)
    print(X1, X2)
else:
    print(x1)
