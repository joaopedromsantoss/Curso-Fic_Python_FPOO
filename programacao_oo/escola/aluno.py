from disciplina import Disciplina
class Aluno:
    def __init__(self,nome, matricula):
        self.aluno = nome
        self.matricula = matricula
        self.disciplinas =[]

    def atribuir_disciplina(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)