alunos = ["Alfredo", "Silas", "Maria", "Humberto"]

nome_arquivo = "alunos.txt"

with open(nome_arquivo, "w") as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno} \n")