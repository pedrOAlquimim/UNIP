from math import sqrt
a = 1
b = 2
c = -3

delta = (b ** 2) - 4 * a * c
deltaf = sqrt(delta)

if deltaf < 0:
    print("Sem valores reais")

else:
    x1 = ((-b + deltaf)/ (2 * a))
    x2 = ((-b - deltaf)/ (2 * a))
    print(f"x1: {x1}, x2: {x2}")