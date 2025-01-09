from produto import Produto

class Venda:
    def __init__(self, produto: Produto, qtde, desconto):
        self.produto = produto
        self.qtde = qtde
        self.total = 0.0
        self.desconto = desconto

    def calcular_total(self):
        self.total = (self.produto.valor * self.qtde) - self.desconto