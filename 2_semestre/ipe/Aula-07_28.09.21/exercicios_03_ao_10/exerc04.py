quantidade = int(input("quantos numeros você deseja digitar? "))
contador = 0
lista1 = []

while contador < quantidade:
    numero= int(input("numero: ")) 
    contador= contador + 1
    lista1.append(numero)

print(lista1)
maior = max(lista1)
print(maior)