lista = []

valor = int(input("Quantos valores você deseja inputar?"))
soma = 0

for x in range(valor):
	resposta = int(input("Digite o número: "))
	lista.append(resposta)
	if resposta > 0:
		soma += resposta
print(soma)
