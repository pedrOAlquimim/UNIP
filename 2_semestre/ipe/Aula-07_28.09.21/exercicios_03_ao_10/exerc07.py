from random import randint

lista = []

for x in range(0, 19):
    lista.append(randint(0, 9))
print(lista)

valor = int(input("Qual valor você deseja contar?: "))
qtd = lista.count(valor)
print(qtd)
