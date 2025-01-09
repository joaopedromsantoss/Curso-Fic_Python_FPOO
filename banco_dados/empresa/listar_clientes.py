import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

clientes = cursor.execute("""SELECT * FROM clientes""")
for cliente in clientes.fetchall():
    print(f"Cliente: {cliente[1]}, Email: {cliente[4]}")
print("--------------------------------------------------------")


clientes_10 = cursor.execute("""SELECT * FROM clientes LIMIT 3""")
for cliente in clientes_10.fetchall():
    print(f"Cliente: {cliente[1]}, Email: {cliente[4]}")
print("--------------------------------------------------------")


clientes_rio = cursor.execute("""SELECT * FROM clientes WHERE cidade = 'Rio de Janeiro'""")
for cliente in clientes_rio.fetchall():
    print(f"Cliente: {cliente[1]}, Cidade: {cliente[6]}")
print("--------------------------------------------------------")


clientes_americanas_55 = cursor.execute("""SELECT * FROM clientes WHERE cidade = 'Americana' AND idade = 55""")
for cliente in clientes_americanas_55.fetchall():
    print(f"Cliente: {cliente[1]}, Cidade: {cliente[6]}, Idade: {cliente[2]}")
print("--------------------------------------------------------")

clientes_email = cursor.execute("""SELECT nome, email FROM clientes WHERE cidade = 'Rio de Janeiro'""")
for cliente in clientes_email.fetchall():
    print(f"Cliente: {cliente[0]}, Email: {cliente[1]}")
print("--------------------------------------------------------")
conn.close()