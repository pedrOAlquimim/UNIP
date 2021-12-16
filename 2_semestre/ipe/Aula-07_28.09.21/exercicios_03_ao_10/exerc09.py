lista = ["BRUNO", "PEDRO", "JOÃO", "GABRIEL", "BRENO", "PAMELA", "AFONSO", "CARLOS", "RIAN", "ANTHONY"]

print(lista)
resp = str(input("Qual nome você deseja remover? ")).upper()

lista.remove(resp)

print(lista)