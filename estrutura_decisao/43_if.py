idade = int(input("Digite sua idade:"))

if idade < 18:
    print("Você é menor de idade")
elif idade > 18:
    print("Você é maior de idade")
elif idade == 18:
    print("Você tem 18 anos, já pode trabalhar")
else:
    print("Idade não identificada")