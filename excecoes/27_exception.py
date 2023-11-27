def somar(n1,n2):
    resultado = n1 + n2
    return resultado

try:
    numero1 = 10
    numero2 = "b"
    somar(numero1,numero2)

except Exception as ex:
    print(f"Ocorreu um erro, tente mais tarde {ex}")