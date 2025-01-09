import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(150) NOT NULL,
        email VARCHAR(150) NOT NULL,
        ra INTEGER NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL,
        media REAL NOT NULL,
        aprovado BOOLEAN DEFAULT FALSE
    )
    """
)

conn.close()