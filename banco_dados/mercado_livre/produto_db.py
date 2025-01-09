from produto import Produto
from typing import List
class ProdutoDb:
    def __init__(self, cursor):
        self.tabela_nome = "produtos"
        self.nome_col = 'nome'
        self.valor_col = 'valor'
        self.qtde_estoque_col = 'qtde_estoque'
        self.cursor = cursor
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.tabela_nome}(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            {self.nome_col} TEXT NOT NULL,
            {self.valor_col} REAL NOT NULL,
            {self.qtde_estoque_col} INTEGER NOT NULL DEFAULT 0
            )
            """
        )

    def inserir_registros(self, produtos: List[Produto]):
        for produto in produtos:
            self.cursor.execute(
                f"""
                INSERT INTO {self.tabela_nome}
                ({self.nome_col}, {self.valor_col}, {self.qtde_estoque_col})
                VALUES ('{produto.nome}', {produto.valor}, {produto.qtde_estoque})
                """
            )

