import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
filename ="INMET_CO_DF_A001_BRASILIA_01-01-2022_A_31-12-2022.csv"
dados = pd.read_csv(filename, skiprows=8, sep=";", encoding="latin-1", on_bad_lines="skip")

# print(f"Dataframe \n{dados.head()}")
# print(f"Colunas\n{dados.columns}")
# print(f"Datas \n{dados['Data']}")
# print(f"Chuva \n{dados['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']}")

meses = [
    {"mes_numero": 1, "mes_nome": "Jan", "total_chuva": 0.0},
    {"mes_numero": 2, "mes_nome": "Fev", "total_chuva": 0.0},
    {"mes_numero": 3, "mes_nome": "Mar", "total_chuva": 0.0},
    {"mes_numero": 4, "mes_nome": "Abr", "total_chuva": 0.0},
    {"mes_numero": 5, "mes_nome": "Mai", "total_chuva": 0.0},
    {"mes_numero": 6, "mes_nome": "Jun", "total_chuva": 0.0},
    {"mes_numero": 7, "mes_nome": "Jul", "total_chuva": 0.0},
    {"mes_numero": 8, "mes_nome": "Ago", "total_chuva": 0.0},
    {"mes_numero": 9, "mes_nome": "Set", "total_chuva": 0.0},
    {"mes_numero": 10, "mes_nome": "Out", "total_chuva": 0.0},
    {"mes_numero": 11, "mes_nome": "Nov", "total_chuva": 0.0},
    {"mes_numero": 12, "mes_nome": "Dez", "total_chuva": 0.0},

]
for index, row in dados.iterrows():
    data_planinha = row.get('Data')
    data_python = datetime.strptime(data_planinha, "%Y/%m/%d").date()
    mes_planilha = data_python.month
    valor_chuva_planilha = str(row.get('PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'))
    valor_chuva_planilha = valor_chuva_planilha.replace(",", ".")
    valor_chuva_planilha = float(valor_chuva_planilha)

    for mes in meses:
        if mes.get("mes_numero") == mes_planilha:
            mes["total_chuva"] += valor_chuva_planilha

print(f"Chuvas \n {meses}")

dados_grafico = [
    [], []
]

for mes in meses:
    dados_grafico[0].append(mes.get("mes_numero"))
    dados_grafico[1].append(mes.get("total_chuva"))

plt.figure(figsize=[20,10])
plt.bar(dados_grafico[0], dados_grafico[1])
plt.title("Informações de Chuvas de 2022")
plt.xlabel("Meses")
plt.ylabel("Valores")
plt.xticks(dados_grafico[0])
plt.savefig("chuvas_anuais_barras.png")
plt.close("all")
    # print(type(valor_chuva_planilha), valor_chuva_planilha)
    # print()
    # # print(row['Data'])
