import sqlite3
from constantes_escola import DATABASE_NAME


conn = sqlite3.connect(DATABASE_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

alunos_aprovados = cursor.execute(
    """
    SELECT * FROM alunos WHERE aprovado = 1
    """
)

for aluno in alunos_aprovados.fetchall():
    print(f"Aluno: {aluno['nome']}, aprovado: {aluno['aprovado']}")

conn.commit()
conn.close()