import csv

nome_arquivo = "temperaturas.csv"
cabecalho = ["Dia da Semana", "Temperatura"]
dados = [
    {"dia": "segunda-feira", "temperatura": 12.9},
    {"dia": "terca-feira", "temperatura": 20.8},
    {"dia": "quarta-feira", "temperatura": 32.2},
    {"dia": "quinta-feira", "temperatura": 5.9},
    {"dia": "sexta-feira", "temperatura": 40.5},
    {"dia": "sabado", "temperatura": 1.1},
    {"dia": "domingo", "temperatura": 12.5}
]

with open(nome_arquivo, "w", encoding= "UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)
    for temperatura in dados:
        dia = temperatura.get("dia")
        valor = temperatura.get("temperatura")
        escritor.writerow([dia, valor])