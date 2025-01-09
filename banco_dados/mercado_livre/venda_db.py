from venda import Venda
from typing import List


class VendaDb:
    def __init__(self, cursor):
        self.tabela_nome = "vendas"
        self.nome_p_col = "nome_produto"
        self.valor_p_col = "valor_produto"
        self.qtde_p_col = "qtde_produto"
        self.total_p_col = "total_produto"
        self.desconto_col = "desconto_venda"
        self.cursor = cursor
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.tabela_nome}(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            {self.nome_p_col} TEXT NOT NULL,
            {self.valor_p_col} REAL NOT NULL,
            {self.qtde_p_col} INTEGER NOT NULL,
            {self.total_p_col} REAL NOT NULL,
            {self.desconto_col} REAL NOT NULL
            )
            """
        )
    def criar_venda(self, vendas: List[Venda]):
        for venda in vendas:
            venda.calcular_total()
            self.cursor.execute(
                f"""
                INSERT INTO {self.tabela_nome} (
                {self.nome_p_col}, {self.valor_p_col}, {self.qtde_p_col}, {self.total_p_col}, {self.desconto_col}
                ) VALUES (
                '{venda.produto.nome}', {venda.produto.valor}, {venda.qtde}, {venda.total}, {venda.desconto}
                )"""
            )
