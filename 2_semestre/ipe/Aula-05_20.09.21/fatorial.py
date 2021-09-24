num = int(input("Digite o númnero desejado: "))
cont = num

while cont > 2:
    cont -= 1
    num = num * (cont)
print(f"O fatorial é igual a {num}")