aluno = {
    "nome": "Elias",
    "idade": 18,
    "curso": "Administração",
    "disciplinas": ["RH", "Excel", "Lidreança"]
}

for chave, valor in aluno.items():
    if chave == "disciplinas":
        for disciplina in aluno.get("disciplinas"):
            print(f"Disiciplina: {disciplina}")
    else:
        print(f"Chave: {chave}, valor: {valor}")