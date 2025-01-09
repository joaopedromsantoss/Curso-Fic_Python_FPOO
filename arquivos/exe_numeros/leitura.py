arquivo = open("numeros.txt", "r")

for linha in arquivo.readlines():
    print(f"{linha}")

arquivo.close()