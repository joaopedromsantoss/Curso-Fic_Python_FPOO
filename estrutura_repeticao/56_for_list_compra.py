# Imprimir os números de 0 até 100 em uma linha com for
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[print(f"Numero: {n}") for n in numeros]

n_pares = [n for n in numeros if n % 2 == 0]
print(f"Pares: {n_pares}")

n_impares = [n for n in range(0,101) if n % 2 != 0]
print(f"Impares: {n_impares}")

#Exemplo 1
cores = ["azul", "amarelo", "roxo", "azul"]
c_azul = [c for c in cores if c == "azul"]
print(c_azul)

#Exemplo 2
c_azul2 = []
for c in cores:
    if c == "azul":
        c_azul2.append(c)

print(c_azul2)