import sqlite3
from constantes_escola import DATABASE_NAME


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def verificar_aprovado(media):
    aprovado = False
    if media >= 5.5:
        aprovado = True
    return aprovado


conn = sqlite3.connect(DATABASE_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
alunos = cursor.execute("""SELECT * FROM alunos""")

for aluno in alunos.fetchall():
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = calcular_media(nota1, nota2)
    aprovado = verificar_aprovado(media)

    cursor.execute(
        """
        UPDATE alunos SET media = ?, aprovado = ?
        WHERE id = ?
        """, (media, aprovado, aluno["id"])
    )

conn.commit()
conn.close()