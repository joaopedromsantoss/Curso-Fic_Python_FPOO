class Disciplina:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (self.nota1 + self.nota2) / 2

    def verifcar_aprovado(self):
        if self.media < 5.5:
            return False
        else:
            return True


