import csv

nome_arquivo = "pin_pong.csv"
cabecalho = {"TURMA", "PONTOS LADO A", "PONTOS LADO B"}
dados = [
    {"turma": "Dev", "pontos_a": 20.0, "pontos_b": 10.0},
    {"turma": "Eletrica", "pontos_a": 10.0, "pontos_b": 52.0},
    {"turma": "Calderaria", "pontos_a": 30.0, "pontos_b": 12.0},
    {"turma": "Solda", "pontos_a": 13.0, "pontos_b": 9.0}
]

with open(nome_arquivo, "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for dado in dados:
        turma = dado.get("turma")
        pontos_lado_a = dado.get("pontos_a")
        pontos_lado_b = dado.get("pontos_b")
        escritor.writerow([turma, pontos_lado_a, pontos_lado_b])
    if pontos_lado_a > pontos_lado_b:
        print(f"A turma {turma} é campeão: {pontos_lado_a}")

    elif pontos_lado_b < pontos_lado_a:
        print(f"A turma {turma} é campeão : {pontos_lado_b}")
