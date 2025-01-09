cidade = input("Digite sua cidade: ")
temperatura = float(input("Digite a temperatura em sua cidade: "))

if temperatura > 26:
    print("Muito calor")
elif temperatura > 20:
    print("Calor")
elif temperatura > 15:
    print("Agradável")
elif temperatura > 11:
    print("Frio")
elif temperatura <= 10:
    print("Muito frio")