class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome =nome
        self.salario_base = salario_base
        self.desconto_plano_saude_v = 0.0
        self.desconto_farmacia = 0.0

    @property
    def desconto_plano_saude(self):
        return self.desconto_plano_saude_v
    @desconto_plano_saude.setter
    def desconto_plano_saude(self, value):
        self.desconto_plano_saude_v =value
        pass