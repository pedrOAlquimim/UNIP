import random

quantidade = int(input("quantos numeros você deseja sortear? "))
contador = 0
lista1 = []

while contador < quantidade:
    numero= random.randint(-100, 100)
    contador = contador + 1
    lista1.append(numero)

print(lista1)
maior= max(lista1)
print(maior)
menor = min(lista1)
print(menor)
soma = sum(lista1)
media = (soma/quantidade)
print(media)
print(soma)
