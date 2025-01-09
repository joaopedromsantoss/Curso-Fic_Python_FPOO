class Disciplina:

    def __init__(self, nome: str):
        self.nome = nome
        self.curso = ""
        self.aprovada = False

    def aprovar(self):
        self.aprovada = True

    def atribuir_curso(self, nome_curso):
        self.curso = nome_curso

    def __str__(self):
        return f"Informações \n Disciplina: {self.nome} \n Aprovada: {self.aprovada} \n Curso: {self.curso}"
