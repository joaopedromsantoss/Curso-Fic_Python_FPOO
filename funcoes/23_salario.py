def calculo_salario():
    salario = float(input('Insira seu salário: '))
    percentual_aumento = float(input('Insira o percentual de aumento: '))

    salario_com_aumento = salario + (salario * percentual_aumento / 100)

    return salario_com_aumento

print(f"O salário com aumento é: R$ {calculo_salario():.2f}")
