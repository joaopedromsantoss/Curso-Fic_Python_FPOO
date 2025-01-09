import matplotlib.pyplot as plt
import pandas as pd

try:
    dataframe = pd.read_csv("chuvas_jan_2023.csv", sep=";")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

# Define o tamanho da figura
plt.figure(figsize=[20, 10])

# Passa as informações do eixo X e Y
plt.plot(dataframe["DIA"], dataframe["VALOR"], marker='o', linestyle='-', color='b', label="Chuvas")

# Ajusta os rótulos do gráfico
plt.title("Informações de Chuvas - Janeiro 2023", fontsize=16)
plt.xlabel("Dias", fontsize=14)
plt.ylabel("Valores (mm)", fontsize=14)

# Exibe os valores do eixo X com rotação
plt.xticks(dataframe["DIA"], rotation=45, fontsize=12)

# Ajusta a escala do eixo Y para evitar sobreposição
plt.yticks(fontsize=12)

# Adiciona linhas no gráfico
plt.grid(True, linestyle='--', alpha=0.7)

# Ajusta automaticamente o espaçamento
plt.tight_layout()

# Salva o gráfico como uma imagem
plt.savefig("chuvas_jan_2023.png")
plt.close("all")
