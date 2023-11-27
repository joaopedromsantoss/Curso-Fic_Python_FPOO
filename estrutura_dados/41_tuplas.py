numeros = [20, 56, 19, 40, 31]
print(f"A lista tem {len(numeros)} itens")

print(f"o index 2 da lista é o numero {numeros[2]}")

"""
Ateração de itens da lista
"""
# Atualizar itens da lista
numeros[4] = 230
print(f"A lista tem os numeros {numeros}")

# Adicionar item na lista
numeros.append(670)
print(f"A lista tem os numeros {numeros}")

# Remover item da lista
del numeros[3]
print(f"A lista tem os numeros {numeros}")

# Remover ultimo item da lista
numeros.pop()
print(f"A lista tem os numeros {numeros}")