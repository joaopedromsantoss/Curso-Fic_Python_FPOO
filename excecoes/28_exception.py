def calcular_media(nota1, nota2):
    # media = (nota1 + nota2) / 2
    media = sum([nota1 + nota2]) / 2
    return media

try:
    n1=5.5
    n2=10
    resultado = calcular_media(n1,n2)
    print(f"O resultado é: {resultado}")

except Exception as ex:
    print(f"Ocorreu um erro, tente mais tarde {ex}")

finally:
    print("Finalizou o algorítmo")