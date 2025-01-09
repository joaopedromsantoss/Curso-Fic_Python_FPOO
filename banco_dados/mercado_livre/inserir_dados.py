from database import Database
from produto_db import ProdutoDb
from produto import Produto
from venda import Venda
from venda_db import VendaDb

banco_de_dados = Database("mercado_livre.db")
produto_db = ProdutoDb(banco_de_dados.cursor)

produtos = [
    Produto("Caderno 10 matérias", 30.99, 10),
    Produto("Caixa de caneta Bic", 59.99, 20),
    Produto("Lápis de cor", 12.99, 35),
    Produto("Tesoura", 8.99, 55),
    Produto("Borracha", 3.99, 78)
]

produto_db.inserir_registros(produtos)

venda_db = VendaDb(banco_de_dados.cursor)

vendas = [
    Venda(produtos[0], 5, 10),
    Venda(produtos[1], 10, 5),
    Venda(produtos[2], 30, 0),
    Venda(produtos[3], 40, 10),
    Venda(produtos[4], 70, 50),
]
venda_db.criar_venda(vendas)

banco_de_dados.close()