import arquivo

class Arquivo:
    def __init__(self, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo
        self.cabecalho = ["NOME", "EMAIL", "RA", "NOTA1", "NOTA2", "MEDIA", "SITUAÇÃO"]

    def criar_csv(self, alunos):
        with open(self.nome_arquivo,"w", encoding="UTF8", newline="") as file:
            escritor = arquivo.writer(file)
            escritor.writerow(self.cabecalho)

            escritor.writerows(alunos)

            # TODO: falta os dados
