def conta(n1,n2,n3,n4):
   n1 = nota1 * 0.15
   n2 = nota2 * 0.25
   n3 = nota3 * 0.40
   n4 = nota4 * 0.20
   media = n1 + n2 + n3 + n4
   return media

nota1 = float(input("A nota 1 é: "))
nota2 = float(input("A nota 2 é: "))
nota3 = float(input("A nota 3 é: "))
nota4 = float(input("A nota 4 é: "))

resultado = conta(nota1,nota2,nota3,nota4)

print(f"A media final é de: {resultado}")