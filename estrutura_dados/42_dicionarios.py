aluno = dict(nome="Sergio", idade=18, matriculado=True)
print(f"Informações do aluno: {aluno}")

aluno_eletrica = {
    "nome": "Elias Silva Santos",
    "idade": 17,
    "cidade": "Piracicaba",
    "disciplinas": ["CLP", "Comandos Eletricos"],
    "matriculado": True,
    "dias_do_curso": {
        "segunda": True,
        "terca": False
    }
}
print(f"As informações do aluno da elétrica {aluno_eletrica}")

# Acessando as propriedades
print(f"O aluno chama-se {aluno_eletrica.get('nome')}")
print(f"O aluno tem a idade {aluno_eletrica.get('idade')}")
print(f"O aluno está no curso {aluno_eletrica.get('curso', 'Não tem propriedade')}")

# Adicionando itens
aluno_eletrica["curso"] = "Dsenvolvimento de sistemas"
print(f"'Novas informações {aluno_eletrica}")

# Removendo itens
del aluno_eletrica["idade"]
print(f"Novas informações {aluno_eletrica}")