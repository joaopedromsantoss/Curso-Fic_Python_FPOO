import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Alfredo Santos', 22, '123123123', 'alfredo@gmail.com', '19-91212-8989', 'Piracicaba', 'SP', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Maria Silva', 25, '567567567', 'maria@gmail.com', '19-56412-4739', 'São Paulo', 'SP', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Alisson Santos', 55, '856856123', 'alisson@gmail.com', '19-98912-5769', 'Americana', 'SP', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Waldemar Costa', 48, '856566123', 'alisson@gmail.com', '19-98912-5769', 'Rio de Janeiro', 'RJ', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Aroldo', 48, '856676123', 'alisson@gmail.com', '19-98966-5769', 'Rio de Janeiro', 'RJ', '2023-07-18')
    """
)

cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Arnaldo Santos', 55, '856856123', 'alisson@gmail.com', '19-98912-5769', 'Americana', 'SP', '2023-07-18')
    """
)

cursor.execute(
    """
    INSERT INTO clientes
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES
    ('Armando Santos', 45, '856856123', 'alisson@gmail.com', '19-98912-5769', 'Americana', 'SP', '2023-07-18')
    """
)
conn.commit()
conn.close()

