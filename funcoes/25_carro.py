def calculo_gasto_viagem(km_percorrido, qtde_dias, valor_dia = 60.00, km_rodado = 0.15):
    qtde_dias_totais = qtde_dias * valor_dia
    km_percorrido_total = km_percorrido * km_rodado
    resultado = qtde_dias_totais + km_percorrido_total
    return resultado


kms = float(input("Quantos Kms foram percorridos? "))
dias = float(input("Quantos dias foram alugados? "))

preco_pagar = calculo_gasto_viagem (kms, dias)

print(f"O valor a pagar é de: {preco_pagar}")