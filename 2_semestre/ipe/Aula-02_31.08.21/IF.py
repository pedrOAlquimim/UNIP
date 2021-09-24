n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3)/3

if media >= 6:
    print(f"Você foi aprovado com media {media}")

else:
    print(f"Você foi reprovado com média {media}")