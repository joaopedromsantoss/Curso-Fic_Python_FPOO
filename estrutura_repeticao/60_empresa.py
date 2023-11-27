def get_cargo(folha_pag):
    lista_folhapagamento = [
        {"cargo": "Gerente", "salario": 6890.00},
        {"cargo": "Programador", "salario": 4290.00},
        {"cargo": "Assistente RH", "salario": 2990.00},
        {"cargo": "Diretor", "salario": 12490.00},
        {"cargo": "Vendedor", "salario": 3670.00}

    ]

    for cargo in lista_folhapagamento:
        if folha_pag == cargo.get("cargo"):
            return cargo.get("salario")


def get_descontos():
    descontos = {
        "vale_transporte": 1.09,
        "vale_refeicao": 1.89,
        "plano_odontologico": 29.90,
        "plano_saude": 109.90
    }
    return descontos


def calcula_inss(salario):
    desconto_inss = 0
    if salario <= 1320:
        desconto_inss = salario * (7.5 / 100)
    if 1320 < salario <= 2571.29:
        desconto_inss = salario * (9.0 / 100)
    if 2571.29 < salario <= 3856.94:
        desconto_inss = salario * (12.0 / 100)
    if salario > 3856.94:
        desconto_inss = salario * (14.0 / 100)
    return desconto_inss
