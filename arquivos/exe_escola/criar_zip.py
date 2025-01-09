import os
import shutil
import csv

os.mkdir("escola")
os.mkdir("arquivos_processados_pelo_sistema")
alunos = ["Alfredo", "Silas", "Roberto", "Maria", "Helena", "Beatriz"]
notas = [
    [3.4, 6.8, 7.8],
    [4.4, 7.8, 7.8],
    [2.4, 1.8, 9.8],
    [2.4, 1.8, 9.8],
    [2.4, 1.8, 9.8],
    [2.4, 1.8, 9.8],
]
nome_arquivo_txt = "arquivos_processados_pelo_sistema/alunos.txt"
nome_arquivo_csv = "arquivos_processados_pelo_sistema/notas.csv"

# Criando arquivo txt
with open(nome_arquivo_txt, "w", encoding="UTF8") as file:
    for aluno in alunos:
        file.write(f"{aluno}\n")

# Criando arquivo csv
with open(nome_arquivo_csv, "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(["ALUNO", "NOTA_1", "NOTA_2", "NOTA_3"])

    for aluno in alunos:
        for nota in notas:
            nota.insert(0, aluno)
            escritor.writerow(nota)


nome_arquivo_zip = "dados_para_download"

shutil.make_archive(nome_arquivo_zip, "zip", "arquivos_processados_pelo_sistema")
