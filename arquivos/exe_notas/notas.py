import csv

cabecalho = []
alunos_com_media = []
disciplina_poo = []

with open("notas.csv", "r", encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        if indice == 0:
            cabecalho = linha
        else:
         aluno = linha[0]
         disciplina = linha[1]
         nota1 = int(linha[2])
         nota2 = int(linha[3])
         media = (nota1 + nota2) / 2
         linha_salvar = [aluno, disciplina, nota1, nota2, media]
         alunos_com_media.append(linha_salvar)

with open("notas_medias_csv", "w", encoding= "UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("MEDIA")
    escritor.writerow(cabecalho)
    for linha in alunos_com_media:
        escritor.writerow([linha])

with open("notas_aprovados", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("APROVADO")
    escritor.writerow(cabecalho)

    for linha in alunos_com_media:
        media = linha[4]
        if media > 5.5:
            linha.append("Aprovado")
            escritor.writerow([linha])

with open("notas_reprovados", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)

    # 1 opção com pop
    # cabecalho.pop()
    # cabecalho.append("REPROVADO")

    cabecalho[5] = "Reprovado"
    escritor.writerow(cabecalho)

    for linha in alunos_com_media:
        media = linha[4]
        if media < 5.5:
            linha.append("Reprovado")
            escritor.writerow([linha])

with open("notas_poo", "w", encoding="UTF8", newline="") as file:
    cabecalho.pop()
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for linha in alunos_com_media:
        disciplinas = linha[1]
        if disciplinas == "POO":
            escritor.writerow([linha])






