A = [1, 2, 3]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
R = [0, 0, 0]

for linha in range(0, 3):
    for coluna in range(0, 3):
        R[linha] = R[linha] * B[coluna][coluna] + A[coluna]
    print(R[linha])