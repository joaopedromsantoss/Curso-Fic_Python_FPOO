import calcular_media

resultado_media = calcular_media.media(10,5)
print(f"A média é: {resultado_media}")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

resultado_media1 = calcular_media.media(nota1,nota2)
print(f"A média das notas é: {resultado_media1:.2f}")