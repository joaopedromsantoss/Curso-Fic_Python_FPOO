nome = input("Digite seu nome: ")
disciplina = input("Digite seu curso: ")
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
faltas = float(input("Digite suas faltas: "))

media = (nota1 + nota2) / 2

if media >= 6.5 and faltas <= 3:
    print("Você está aprovado")
elif media <= 6.5 and faltas <= 4:
    print("Você está de recuperação")
elif media <= 6.5 and faltas > 4:
    print("Você está reprovado")