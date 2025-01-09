import sqlite3
from constantes_escola import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
# conn.row_factory = sqlite3.Row
cursor.execute(
    """
    CREATE TABLE alunos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    ra INTEGER NOT NULL,
    email TEXT NOT NULL, 
    disciplina TEXT NOT NULL,
    nota1 REAL DEFAULT 0,
    nota2 REAL DEFAULT 0,
    media REAL DEFAULT 0, 
    aprovado BOOLEAN DEFAULT FALSE
    )
    """
)
print("Tabela criada com sucesso :)")
conn.close()