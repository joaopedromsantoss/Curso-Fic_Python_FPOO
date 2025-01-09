import sqlite3


class Aluno:
    def __init__(self, nome, email, ra, nota1, nota2):
        self.nome = nome
        self.email = email
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0
        self.aprovado = False

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        if self.media >= 5.5:
            self.aprovado = True

    @staticmethod
    def conectar_banco():
        conn = sqlite3.connect("escola.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def desconectar_banco(conn):
        conn.commit()
        conn.close()

    def salvar(self):
        conn, cursor = self.conectar_banco()
        cursor.execute(
            """
            INSERT INTO alunos (nome, email, ra, nota1, nota2, media, aprovado)
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """, (self.nome, self.email, self.ra, self.nota1, self.nota2, self.media, self.aprovado)
        )
        self.desconectar_banco(conn)

    @staticmethod
    def buscar_todos_alunos():
        conn = sqlite3.connect("escola.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        resultados = cursor.execute(
            """SELECT * FROM alunos"""
        )
        alunos = []
        for resultado in resultados.fetchall():
            situacao = "reprovado"

            if resultado["aprovado"]:
                situacao = "aprovado"
            aluno = [
                    resultado["nome"], resultado["email"], resultado["ra"], resultado["nota1"], resultado["nota2"], resultado["media"], situacao
                ]
            alunos.append(aluno)

        conn.commit()
        conn.close()
        return alunos

    @staticmethod
    def buscar_todos_aprovados():
        conn = sqlite3.connect("escola.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        resultados = cursor.execute(
            """SELECT * FROM alunos WHERE aprovado = true"""
        )
        alunos = []
        for resultado in resultados.fetchall():
            situacao = "reprovado"

            if resultado["aprovado"]:
                situacao = "aprovado"
            aluno = [
                resultado["nome"], resultado["email"], resultado["ra"], resultado["nota1"], resultado["nota2"],
                resultado["media"], situacao
            ]
            alunos.append(aluno)

        conn.commit()
        conn.close()
        return alunos

    @staticmethod
    def buscar_todos_reprovados():
        conn = sqlite3.connect("escola.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        resultados = cursor.execute(
            """SELECT * FROM alunos WHERE aprovado = false"""
        )
        alunos = []
        for resultado in resultados.fetchall():
            situacao = "reprovado"

            if resultado["aprovado"]:
                situacao = "aprovado"
            aluno = [
                resultado["nome"], resultado["email"], resultado["ra"], resultado["nota1"], resultado["nota2"],
                resultado["media"], situacao
            ]
            alunos.append(aluno)

        conn.commit()
        conn.close()
        return alunos
