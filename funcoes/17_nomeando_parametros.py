def calcula_aumento_salario(salario, percentual_aumento):
    salario_com_aumento= salario + (salario * percentual_aumento / 100)
    return salario_com_aumento

salario_atual = 2500
percentual = 10
salario_novo = calcula_aumento_salario(salario=salario_atual,
                                       percentual_aumento=percentual)
print(f'Seu sálario com aumento é: {salario_novo}')
