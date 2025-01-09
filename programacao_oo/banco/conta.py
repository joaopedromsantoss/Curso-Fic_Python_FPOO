from cliente import Cliente
class Conta:
    def __init__(self, nome, descricao, saldo, cliente: Cliente):
        self.nome = nome
        self.descricao = descricao
        self.saldo = saldo
        self.cliente = cliente
        self.movimentacao = []

    def depositar (self, valor):
        self.saldo += valor
        self.movimentacao.append("Depositou" + str(valor))

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.movimentacao.append("Sacou" + str(valor))
        else:
            print("Saldo insuficiente")

    def get_saldo(self):
        return self.saldo
    def get_extrato(self):
        for movimentacao in self.movimentacao:
            print(movimentacao)



