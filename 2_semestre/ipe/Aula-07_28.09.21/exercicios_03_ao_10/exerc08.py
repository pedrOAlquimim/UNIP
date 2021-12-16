from random import randint

''' No inicio do programa deve permitir os usuários entrar com os respectivos nomes.'''
player1 = str(input("Qual o nome do 1 jogador: "))
player2 = str(input("Qual o nome do 2 jogador: "))

lista = []

for x in range(0, 19):
    lista.append(randint(0, 9))

'''Deverá ser possível dois jogadores escolher os números.'''
player1_c = int(input(f"Qual valor o {player1} deseja contar?: "))
qtd1 = lista.count(player1_c)

player2_c = int(input(f"Qual valor o {player2} deseja contar?: "))
qtd2 = lista.count(player2_c)

'''Deve ser retornado o nome do jogador que acertou mais.'''
if qtd1 > qtd2:
    print(f"O jogador {player1} ganhou com um total de {qtd1} acertos.")
elif qtd2 > qtd1:
    print(f"O jogador {player2} ganhou com um total de {qtd2} acertos.")
else:
    print(f"Os jogadores {player1} e {player2} empataram.")

'''No final do programa retorna o total acertado por cada um dos jogadores.'''
print(f"{player1}: {qtd1} acertos.")
print(f"{player2}: {qtd2} acertos.")
