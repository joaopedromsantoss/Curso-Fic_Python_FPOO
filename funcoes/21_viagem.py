cidade_saída = input('Insira a cidade de partida: ')
cidade_destino = input('Insira a cidade destino: ')
distancia = float(input('Insira a distância entre as cidades: '))
media_km_por_litro = float(input('Insira a média de km por litro do veículo: '))
combustivel_utilizado = input('Insira o combustível utilizado: ')

def mensagem():
    print(f'O custo da viagem entre as cidades {cidade_saída} e {cidade_destino} '
          f'com o combustível {combustivel_utilizado} é {custo_viagem}')

def calculo_quantidade_litros():
    quantidade_litros = distancia / media_km_por_litro

def imprimir_custo_viagem():
    if combustivel_utilizado == 'gasolina':
        calculo_quantidade_litros()
        custo_viagem = calculo_quantidade_litros() * 5.39
        mensagem()
    elif combustivel_utilizado == 'etanol':
        calculo_quantidade_litros()
        custo_viagem = calculo_quantidade_litros() * 3.49
        mensagem()
    else:
        print('Combustível não identificado.')

print(imprimir_custo_viagem())