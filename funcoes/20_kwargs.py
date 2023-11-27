def calcula_salario(**kwargs):
    desconto_inss = kwargs.get('inss') / 100
    desconto_plano_de_saude = kwargs.get('plano')
    total_descontos = desconto_inss + desconto_plano_de_saude
    salario_liquido = kwargs.get('salario_base') - total_descontos
    return salario_liquido

salario_a_receber = calcula_salario(salario_base=5000,
                                    inss=8,
                                    plano=129.90)

print(f'O salario é {salario_a_receber}')