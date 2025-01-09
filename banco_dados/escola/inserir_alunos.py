import sqlite3
from constantes_escola import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO alunos
    (nome, ra, email, disciplina, nota1, nota2)
    VALUES
    ('Alfredo Santos', 123123,'alfredo@gmail.com', 'Matematica', 6.6, 1.4)
    """
)

cursor.execute(
    """
    INSERT INTO alunos
    (nome, ra, email, disciplina, nota1, nota2)
    VALUES
    ('Silas Silva', 123123,'silas@gmail.com', 'Lingua Porutguesa', 5.5, 8.6)
    """
)
cursor.execute(
    """
    INSERT INTO alunos
    (nome, ra, email, disciplina, nota1, nota2)
    VALUES
    ('Aroldo', 123123,'silas@gmail.com', 'Lingua Porutguesa', 5.5, 8.6)
    """
)
cursor.execute(
    """
    INSERT INTO alunos
    (nome, ra, email, disciplina, nota1, nota2)
    VALUES
    ('Arnaldo', 123123,'silas@gmail.com', 'Lingua Porutguesa', 5.5, 8.6)
    """
)
conn.commit()
conn.close()
