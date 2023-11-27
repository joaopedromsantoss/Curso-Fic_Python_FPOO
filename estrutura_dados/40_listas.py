nomes = ("Aluno 01", "Aluno 02", "Aluno 03")
print(f"A tupla tem {len(nomes)} itens")
print(f"o index 2 da tupla é {nomes[2]}")

# Adicionar item na tupla
nomes += ("Aluno 04",)
print(f"Tupla alterada {nomes}")

# Remover o item da tupla
del nomes[1]
print(f"Tupla removida {nomes}")