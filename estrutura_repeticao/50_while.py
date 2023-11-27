# Imprimir os números ímpares de 1 até 100
# Quando a qtde chegar em 10 deve para o while
numero = 1
contador_unidades = 0

while numero <= 100:
    if(numero % 2) != 0:
        print(f"O numero {numero} é impar")
        contador_unidades += 1

    if contador_unidades == 10:
        break

    numero+= 1