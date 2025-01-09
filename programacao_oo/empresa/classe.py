from funcionario import Funcionario

funcionario01 = Funcionario(nome="Funcionario01", salario_base=3450.00)
print(f"1: Valor{funcionario01.desconto_plano_saude_v}")
funcionario01.desconto_plano_saude= 250.90
print(f"2: Valor{funcionario01.desconto_plano_saude_v}")