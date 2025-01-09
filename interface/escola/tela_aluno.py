from tkinter import *
from aluno import Aluno
from random import randrange
from arquivo import  Arquivo

def gerar_csv(nome_arquivo, categoria):
    arquivo = Arquivo(nome_arquivo=nome_arquivo)
    alunos = []
    if categoria == "todos":
       alunos = Aluno.buscar_todos_alunos()
    elif categoria == "aprovados":
        alunos = Aluno.buscar_todos_aprovados()
    elif categoria == "reprovados":
        alunos = Aluno.buscar_todos_reprovados()

    arquivo.criar_csv(alunos)

def gerar_ra():
    ra = randrange(1, 10000)
    input_ra.delete(0, END)
    input_ra.insert(0, ra)

def calcular_media(i_nome, i_email, i_ra, i_nota1, i_nota2):
    print(f"Nome: {i_nome.get()}")
    print(f"Nota 1: {i_nota1.get()}")
    print(f"Nota 2: {i_nota2.get()}")
    email = i_email.get()
    ra = i_ra.get()
    nota1 = float(i_nota1.get())
    nota2 = float(i_nota2.get())
    aluno = Aluno(i_nome.get(), email, ra, nota1, nota2)
    aluno.calcular_media()
    aluno.salvar()

    aprovado_str = "reprovado"
    if aluno.aprovado:
       aprovado_str = "aprovado"

    mensagem = f"Aluno: {aluno.nome} \n Sua média é: {aluno.media:.2f} \n Você foi: {aprovado_str}"
    label_media.config(text=mensagem)

    #Limpa os campos
    input_nome.delete(0, END)
    input_email.delete(0, END)
    input_ra.delete(0, END)
    input_nota1.delete(0, END)
    input_nota2.delete(0, END)



janela = Tk()
janela.state("zoomed")
janela.title("Cálculo de Notas dos Alunos")
janela.config(padx=10, pady=10, bg="gray")
janela.geometry("700x500")

# label
label_nome = Label(text="Nome: ", font=("Arial", 25))
label_nome.grid(row=1, column=1, padx=10, pady=10)

label_email = Label(text="Email: ", font=("Arial", 25))
label_email.grid(row=2, column=1, padx=10, pady=10)

label_ra = Label(text="RA: ", font=("Arial", 25))
label_ra.grid(row=3, column=1, padx=10, pady=10)

label_nota1 = Label(text="Nota 1: ", font=("Arial", 25))
label_nota1.grid(row=4, column=1, padx=10, pady=10)

label_nota2 = Label(text="Nota 2: ", font=("Arial", 25))
label_nota2.grid(row=5, column=1, padx=10, pady=10)

label_media = Label(text="Sua média é: ", font=("Arial", 25), width=30)
label_media.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

# input
input_nome = Entry(font=("Arial", 25))
input_nome.grid(row=1, column=2, padx=5, pady=10)

input_email = Entry(font=("Arial", 25))
input_email.grid(row=2, column=2, padx=5, pady=10)

input_ra = Entry(font=("Arial", 25))
input_ra.grid(row=3, column=2, padx=5, pady=10)

input_nota1 = Entry(font=("Arial", 25))
input_nota1.grid(row=4, column=2, padx=5, pady=10)

input_nota2 = Entry(font=("Arial", 25))
input_nota2.grid(row=5, column=2, padx=5, pady=10)

# button
botao_ra = Button(
    text="Gerar RA", width=20, font=("Arial", 25),
    command=lambda: gerar_ra()
)
botao_ra.grid(row=3, column=3, columnspan=2)

botao_calcular = Button(text='Calcular a média', width=30, command=lambda: calcular_media(input_nome, input_email, input_ra, input_nota1, input_nota2))
botao_calcular.grid(row=9, column=1, columnspan=2)

# Exportar dados
label_exportar = Label(font=("Arial", 25), width=40, bg="yellow", text="Opções para exportação de dados")
label_exportar.grid(row=10, column=1, columnspan=2, padx=10, pady=30)

botao_todos = Button(text="Todos os dados", width=20, font=("Verdana", 20), bg="blue", command=lambda: gerar_csv("todos_alunos.csv", "todos"))
botao_todos.grid(row=12, column=1, padx=10, pady=10)

botao_aprovados = Button(text="Alunos Aprovados", width=20, font=("Verdana", 20), bg="green", command=lambda: gerar_csv("alunos_aprovados.csv", "aprovados"))
botao_aprovados.grid(row=12, column=2, padx=10, pady=10)

botao_reprovados = Button(text="Alunos Reprovados", width=20, font=("Verdana", 20), bg="red", command=lambda: gerar_csv("alunos_reprovados.csv", "reprovados"))
botao_reprovados.grid(row=12, column=3, padx=10, pady=10)

janela.mainloop()
