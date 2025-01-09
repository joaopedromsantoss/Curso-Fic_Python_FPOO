"""
Exemplo de criação de arquivo com Python
MODO  OPERAÇÃO
r     leitura
w     escrita
a     escrita, mas preserva o conteudo
"""

nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo, "w")

for numero in range(1,101):
    arquivo.write(f"numero {numero}\n")

arquivo.close()