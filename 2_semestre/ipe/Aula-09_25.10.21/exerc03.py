M = [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1], [1, 2, 3, 4]]

somaL = [0, 0, 0, 0]
somaC = [0, 0, 0, 0]

for linha in range(0, 4):
    for coluna in range(0, 4):
        somaL[linha] = somaL[linha] + M[linha][coluna]
        somaC[linha] = somaC[linha] + M[coluna][linha]
    print(somaL[linha])

for linha in range(0, 4):
    print(somaC[linha])