def tempo(**kwargs):
    segundos_total = (kwargs.get("dias") * 86400) + (kwargs.get("horas") * 3600) + (kwargs.get("minutos") * 60) + kwargs.get("segundos")
    return segundos_total

dias_segundos = int(input("Digite os dias: "))
horas_segundos = int(input("Digite as horas: "))
minutos_segundos = int(input("Digite os minutos: "))
segundos_segundos = int(input("Digite os segundos: "))

resultado = tempo(dias=dias_segundos, horas=horas_segundos, minutos=minutos_segundos, segundos=segundos_segundos )

print(resultado)
