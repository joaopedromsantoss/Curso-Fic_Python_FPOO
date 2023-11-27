def calculo():
    dia = input('Insira o número de dias: ')
    hora = input('Insira o número de horas: ')
    minuto = input('Insira o número de minutos: ')
    segundo = input('Digite o número de segundos: ')
    transformar_dia = int(dia) * 24 * 3600
    transformar_hora = int(hora) * 3600
    transformar_minuto = int(minuto) * 60
    soma_total = int(segundo) + transformar_minuto + transformar_hora + transformar_dia
    return soma_total


print(calculo())