import locale
from random import randint
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')
    
print("----------Menu---------")
print("(1) - Exercício 1")
print("(2) - Exercício 2")
print("(3) - Exercício 3")
print("(4) - Exercício 4")
print("(0) - Sair")
print("------------------------")

opcao = int(input("Digite a opção desejada: "))
print("------------------------------------")
lista = []

if opcao == 1:

    for x in range(0, 20):
        lista.append(randint(0, 10))

    print(f"A lista é {lista}")

    print(f"A ordem Crescente é {sorted(lista)}")
    print(f"A ordem Decrescente é {sorted(lista, reverse=True)}")
    print(f"O Maior valor é o {max(lista)}")
    print(f"O Menor valor é o {min(lista)}")
    print(f"A Soma da lista é {sum(lista)}")

    for x in range(0, 20):
        if 5 in lista:
            lista.remove(5)
    print(f"A lista sem o valor 5 = {lista}")

elif opcao == 2:
    
    for x in range(0, 10):
        lista.append(randint(0, 50))
    
    print(f"A lista é {lista}")

    for x in range(len(lista)):
        if lista[x] < 25:
            lista[x] = lista[x] + 10
        else:
            lista[x] = lista[x] - 5

    print(f"A lista depois das condições: {lista}")

elif opcao == 3:
    
    day = int(input("Digite o Dia (dd): "))
    month = int(input("Digite o Mês (mm): "))
    year = int(input("Digite o Ano (yyyy): "))

    m = datetime(year, month, day)

    print(m.strftime((f"Você nasceu em {day} de %B de {year}")))

elif opcao == 4:

    palavra = "This is just a simple string"

    print(f"A quantidade de caracteres é {len(palavra)}")

    palavra = palavra.replace('simple', 'short')
    print(f"De simple para short é = {palavra}")

    palavra = "This is just a simple string"
    print(f"A posição é {palavra.find('simple')}")
    
    print(f"A letra de cada palavra da frase em maiúsculo: [{palavra.title()}]")

elif opcao == 0:
    print("Você saiu do Menu")

else:
    print("Opção Inválida")
    print("Digite um valor correto (De 0 á 4)")
