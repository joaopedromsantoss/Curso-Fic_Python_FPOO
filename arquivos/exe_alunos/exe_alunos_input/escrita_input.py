alunos = []

for numero in range(1,6):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

with open("alunos_input.txt", "a", encoding="UTF8") as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno}\n")