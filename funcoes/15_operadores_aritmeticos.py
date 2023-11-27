def adicao(n1, n2):
    total = n1 + n2
    return total


def subtracao(n1, n2):
    total = n1 - n2
    return total


def multiplicacao(n1, n2):
    total = n1 * n2
    return total


def divisao(n1, n2):
    total = n1 / n2
    return total

operador_aritimetico = str(input('Insira seu operador aritimético: '))

if operador_aritimetico =='adicao' or 'soma':
    n1 = float(input('Insira um valor: '))
    n2 = float(input('Insira outro valor: '))
    resultado = adicao(n1, n2)
    print(f'O resultado da {operador_aritimetico} é {resultado}')
elif operador_aritimetico =='subtracao' or 'menos':
    n1 = float(input('Insira um valor: '))
    n2 = float(input('Insira outro valor: '))
    resultado = subtracao(n1, n2)
    print(f'O resultado da {operador_aritimetico} é {resultado}')
elif operador_aritimetico =='multiplicacao' or 'vezes':
    n1 = float(input('Insira um valor: '))
    n2 = float(input('Insira outro valor: '))
    resultado = multiplicacao(n1, n2)
    print(f'O resultado da {operador_aritimetico} é {resultado}')
elif operador_aritimetico =='divisao' or 'dividir':
    n1 = float(input('Insira um valor: '))
    n2 = float(input('Insira outro valor: '))
    resultado = divisao(n1, n2)
    print(f'O resultado da {operador_aritimetico} é {resultado}')
else:
    print('Operador não identificado.')