# Exemplo de soma com uso de funções

def soma(n1=float(input('Insira um valor:')), n2=float(input('Insira outro valor:'))):
    total = n1 + n2
    return total

print(f'O resultado é:{soma()}')