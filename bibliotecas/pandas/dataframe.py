from pandas import DataFrame, Series

notas_alunos = {
    "alunos": Series(data=["aluno01", "aluno02", "aluno03"]),
    "nota1": Series(data=[2.9, 3.5, 7.8]),
    "nota2": Series(data=[3.9, 6.5, 8.8])
}

dataframe = DataFrame(notas_alunos)
print(f"Dados dos alunos \n {dataframe}")

filtro1 = DataFrame(notas_alunos, index=[1, 2])
print(f"Filtro 1: \n{filtro1}")

filtro2 = DataFrame(notas_alunos, columns=["alunos", "nota2"])
print(f"Filtro 2: \n{filtro2}")