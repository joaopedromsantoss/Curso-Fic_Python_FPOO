from empresa import get_cargo, get_descontos, calcula_inss

funcionarios = [
    {
        "nome": "Alfredo",
        "cargo": "Assistente RH",
        "dependentes": 3,
        "vale_transporte": True
    },
    {
        "nome": "Eliza",
        "cargo": "Gerente",
        "dependentes": 2,
        "vale_transporte": False

    },
    {
        "nome": "Silas",
        "cargo": "Programador",
        "dependentes": 4,
        "vale_trnasporte": False
    },
    {
        "nome": "Francisco",
        "cargo": "Diretor",
        "dependentes": 5,
        "vale_transporte": True
    },
    {
        "nome": "Maria",
        "cargo": "Vendedor",
        "dependentes": 1,
        "vale_transporte": False
    },
    {
        "nome": "Danilo",
        "cargo": "Programador",
        "dependentes": 2,
        "vale_transporte": False
    },
    {
        "nome": "Mariana",
        "cargo": "Assistente RH",
        "dependentes": 3,
        "vale_transporte": True
    }
]

for funcionario in funcionarios:
    nome = funcionario.get("nome")
    cargo = funcionario.get("cargo")
    dependentes_funcionario = funcionario.get("dependentes")

    salario_funcionario = get_cargo(cargo)
    descontos = get_descontos()

    valor_plano_saude = descontos.get("plano_saude")
    valor_plano_odontologico = descontos.get("plano_odontologico")

    desconto_plano_saude = dependentes_funcionario * valor_plano_saude
    desconto_plano_odontologico = dependentes_funcionario * valor_plano_odontologico
    desconto_inss = calcula_inss(salario_funcionario)

    print(f"Funcionario: {nome} \n salario: {salario_funcionario} \n desconto plano saúde: {desconto_plano_saude:.2f} \n desconto plano odontológico: \n {desconto_plano_odontologico:.2f} \n desconto INSS: {desconto_inss:.2f}")
