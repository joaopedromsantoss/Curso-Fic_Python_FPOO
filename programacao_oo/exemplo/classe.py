"""
Exemplo de uso de classes com Python
"""

from carro import Carro

carro1 = Carro()
print(f"Carro {carro1.marca}")

from aluno import Aluno

aluno01 = Aluno("Elias dos Santos", 19, "elias@gmail.com")
aluno02 = Aluno("Maria dos Santos", 17, "maria@gmail.com")
aluno03 = Aluno (idade=16, nome="Suzana", email="suzana@gmail.com")

print(f"Aluno 1: {aluno01.nome} \n Aluno 2: {aluno02.nome} \n Aluno 3: {aluno03.nome}")

from atividade import Atividade

atividade_logica = Atividade("Resolver atividade de lógica de programação")
atividade_poo = Atividade("Criar classes POO", 8.0)
atividade_html = Atividade(descricao_atividade="Criar página em HTML", nota_maxima_atividade=7.0)

d_atividade_upper = atividade_html.descricao.upper()

print(atividade_html, d_atividade_upper)

from disciplina import Disciplina

poo = Disciplina(nome="Programação Orientada Objeto")
print(f"1: {poo}")

poo.aprovar()
print(f"2: {poo}")

poo.atribuir_curso("Desenvolvimento Sistemas")
print(f"3: {poo}")