import random

contador= 0
quantidade= 9
lista1 = []
lista2 = []

x= int(input('digite um numero '))

while contador < quantidade:
    numero= random.randint(1, 6)
    contador = contador +1
    lista1.append(numero)

lista1.append(x)
print (lista1)

contador=0

while contador < quantidade:
    numero = random.randint(1, 6)
    contador = contador +1
    lista2.append(numero)

lista2.append(x)
print (lista2)

conc = (lista1 + lista2)
print(conc)

lista1.sort()
print(lista1)

lista2.reverse()
print(lista2)