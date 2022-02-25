import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"A única raiz é {raiz1}")
else:
    if delta < 0:
        print("Esta equação não possui raízes reais.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A primeira raiz é {raiz1} e a segunda é {raiz2}")