from disciplina import Disciplina
from curso import Curso
from aluno import Aluno

curso_dev = Curso("Programação em Python")
gustavo = Aluno("Gustavo", 1234)
gabriel = Aluno("Gabriel", 5643)

gustavo.atribuir_disciplina(Disciplina("Fundamentos", 3.4, 9.8))
gabriel.atribuir_disciplina(Disciplina("Fundamentos", 5.6, 4.8))

gustavo.atribuir_disciplina(Disciplina("POO com Python", 7.6, 5.5))
gabriel.atribuir_disciplina(Disciplina("POO com Python", 2.6, 8.5))

curso_dev.adicionar_aluno(gustavo)
curso_dev.adicionar_aluno(gabriel)

curso_eletrica = Curso("Elétrica")
aroldo = Aluno("Aroldo", 1434)
aroldo.atribuir_disciplina(Disciplina("CLP", 4.5, 7.7))
aroldo.atribuir_disciplina(Disciplina("Comandos", 7.5, 3.5))

artur = Aluno("Artur", 4534)
artur.atribuir_disciplina(Disciplina("CLP", 4.3, 6.5))
artur.atribuir_disciplina(Disciplina("Comandos", 6.5, 9.5))

curso_eletrica.adicionar_aluno(aroldo)
curso_eletrica.adicionar_aluno(artur)

for aluno in curso_dev.alunos:
    print(f"Aluno: {aluno.aluno}")
    for disciplina in aluno.disciplinas:
        print(f"Disciplina: {disciplina.nome}")
        print(f"Nota 1: {disciplina.nota1}")
        print(f"Nota 2: {disciplina.nota2}")
        print(f"Média: {disciplina.media:.2f}")
    if disciplina.verifcar_aprovado():
        print(f"O aluno {aluno.aluno} está aprovado")
    else:
        print(f"O aluno {aluno.aluno} está reprovado")

for aluno in curso_eletrica.alunos:
    print(f"Aluno {aluno.aluno}")
    for disciplina in aluno.disciplinas:
        print(f"Disciplina: {disciplina.nome}")
        print(f"Nota 1: {disciplina.nota1}")
        print(f"Nota 2: {disciplina.nota2}")
        print(f"Média: {disciplina.media}")
    if disciplina.verifcar_aprovado():
        print(f"O aluno {aluno.aluno} está aprovado")
    else:
        print(f"O aluno {aluno.aluno} está reprovado")


