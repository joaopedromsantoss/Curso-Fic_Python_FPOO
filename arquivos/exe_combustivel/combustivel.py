import csv

cabecalho = []
dados_qtde_litros_gasolina = []
dados_qtde_litros_etanol = []
dados_valor_total_gasolina = []
dados_valor_total_etanol = []
valor_gasolina = 5.19
valor_etanol = 3.19

with open("combustiveis.csv", "r", encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        print(linha)
        if indice == 0:
            cabecalho = linha
        else:
            veiculo = linha[0]
            valor_por_km = linha[1]
            valor_km = float(valor_por_km.replace("R$ ", ""))
            valor_por_dia = linha[2]
            valor_dia = float(valor_por_dia.replace("R$ ", ""))
            seguro = (linha[3])
            seg = float(seguro.replace("R$ ", ""))
            media_gasolina = linha[4]
            media_g = float(media_gasolina.replace("R$ ", ""))
            media_etanol = linha[5]
            media_e = float(media_etanol.replace("R$ ", ""))
            qtde_litros_gasolina = 569 / media_g
            qtde_litros_etanol = 569 / media_e
            valor_litro_gasolina = (qtde_litros_gasolina * valor_gasolina)
            valor_etanol = (qtde_litros_etanol * valor_etanol)
            valor_gasolina_total = valor_gasolina + (valor_km * 569) + (5 * valor_dia) + seg
            valor_etanol_total = valor_etanol + (valor_km * 569) + (5 * valor_dia) + seg
            linha_salvar = [veiculo, valor_por_km, valor_por_dia, seguro, media_gasolina, media_etanol, valor_gasolina, valor_etanol, qtde_litros_gasolina, qtde_litros_etanol, valor_gasolina_total, valor_etanol_total]
            dados_qtde_litros_gasolina.append(linha_salvar)
            dados_qtde_litros_etanol.append(linha_salvar)
            dados_valor_total_gasolina.append(linha_salvar)
            dados_valor_total_etanol.append(linha_salvar)

with open("combustiveis.csv", "w", encoding= "UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("QTDE_LITROS_GASOLINA")
    escritor.writerow(cabecalho)
    for linha in dados_qtde_litros_gasolina:
        escritor.writerow([linha])

with open("combustiveis_valor_etanol.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("QTDE_LITROS_ETANOL")
    escritor.writerow(cabecalho)
    for linha in dados_qtde_litros_etanol:
        escritor.writerow([linha])
