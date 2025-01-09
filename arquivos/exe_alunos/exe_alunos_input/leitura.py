with open("alunos_input.txt", "r") as file:
    for aluno in file.readlines():
        print(f"Nome do aluno: {aluno}")