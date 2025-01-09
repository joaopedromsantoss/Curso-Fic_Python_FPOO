cidade_saida = input("Digite a cidade de saída: ")
cidade_destino = input("Digite a cidade de destino: ")
nome_veiculo = input("Digite o nome do veículo: ")
ano_fabricacao = float(input("Digite o ano de fabricação do veículo: "))
valor_gasolina = float(input("Digite o preço da gasolina: "))
valor_etanol = float(input("Digite o preço do etanol: "))
km_percorridos = float(input("Digite os Kms percorridos: "))
km_por_litro_gasolina = float(input("Digite quantos Km por litro de gasolina faz seu veículo: "))
km_por_litro_etanol = float(input("Digite quantos Km por litro de etanol faz seu veículo: "))

total_gasolina = (km_percorridos / km_por_litro_gasolina) * valor_gasolina
total_etanol = (km_percorridos / km_por_litro_etanol) * valor_etanol

if total_gasolina > total_etanol:
    print(f"O etanol vai custar {total_etanol:.2f} e a gasolina vai custar {total_gasolina:.2f}. Ou seja, o etanol compensa mais")
elif total_gasolina < total_etanol:
    print(f"A gasolina vai custar {total_gasolina:.2f} e o etanol vai custar {total_etanol:.2f}. Ou seja, a gasolina compensa mais")
elif total_gasolina == total_etanol:
    print(f"O etanol vai custar{total_etanol:.2f} e a gasolina vai custar {total_gasolina:.2f}. Ou seja, ambos compensam")
