import sqlite3
from constantes import DATABASE_NAME

conexao = sqlite3.connect(DATABASE_NAME)
cursor = conexao.cursor()
cursor.execute(
    """
    CREATE TABLE clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT NOT NULL,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL  
    )
    """
)
print("Tabela criada com sucesso :)")

conexao.close()