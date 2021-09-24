a1 = float(input("Entre com o valor do lado A: "))
b1 = float(input("Entre com o valor do lado B: "))
c1 = float(input("Entre com o valor do lado C: "))

if (a1 == b1 == c1):
    print("Esse é um triângulo Equilátero")
elif (a1 != b1) and (a1 != c1) and (b1 != c1):
    print("Este é um triângulo Escaleno")
else:
    print("Este é um triângulo Isóceles")