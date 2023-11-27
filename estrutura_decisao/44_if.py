nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    print(f"Está de parabéns, sua média foi {media:.2f}")
elif media >= 6.5:
    print(f"Você está aprovado, sua média foi {media:.2f}")
elif media >= 4.0:
    print(f"Você está de recuperação, sua média foi {media:.2f}")
else:
    print(f"Você está reprovado, sua média foi {media:.2f}")