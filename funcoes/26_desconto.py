def calculor_desconto():
    nome = input('Insira o nome do produto: ')
    preco = float(input('Insira o preço do mesmo: '))
    percentual_desconto = float(input('Insira o percentual de desconto do mesmo: '))
    desconto_produto = preco * (percentual_desconto / 100)
    valor_final_produto = preco - desconto_produto
    return valor_final_produto, desconto_produto, nome

valor_final_produto, desconto_produto, nome = calculor_desconto()

print(f'O valor com desconto de R${desconto_produto} do produto {nome} é R${valor_final_produto}')