from cliente import Cliente
from conta import Conta


cliente01 = Cliente("Alfredo", 12312312312, 12313121, "alfredo@gmail.com", True)
cliente02 = Cliente("Silas", 87282884298, 12331132, "maria@gmail.com", True)
cliente03 = Cliente("Helena", 87282883398, 12353332, "helena@gmail.com", True)
cliente04 = Cliente("Rafael", 87282882398, 12344332, "rafael@gmail.com", True)
cliente05 = Cliente("João", 87282884398, 12353332, "joao@gmail.com", True)


conta01 = Conta("Conta Corrente", "Esta é a conta corrente do Alfredo", 5000, cliente01)
conta02 = Conta("Conta Corrente", "Esta é a conta corrente do Silas", 500, cliente02)
conta03 = Conta("Conta Corrente", "Esta é a conta corrente do Helena", 2500, cliente03)
conta04 = Conta("Conta Corrente", "Esta é a conta corrente do Rafael", 5000, cliente04)
conta05 = Conta("Conta Corrente", "Esta é a conta corrente do João", 1000, cliente05)

conta01.depositar(3000)
conta02.depositar(1000)
conta03.depositar(1000)
conta04.depositar(100)
conta05.depositar(1000)

conta01.sacar(50)
conta02.sacar(2000)
conta03.sacar(1000)
conta04.sacar(10000)
conta05.sacar(2500)

conta01.get_extrato()
conta02.get_extrato()
conta03.get_extrato()
conta04.get_extrato()
conta05.get_extrato()

print(f"O saldo do Sr {cliente01.nome} é {conta01.get_saldo()}")
print(f"O saldo do Sr {cliente02.nome} é {conta02.get_saldo()}")
print(f"O saldo do Sr {cliente03.nome} é {conta03.get_saldo()}")
print(f"O saldo do Sr {cliente04.nome} é {conta04.get_saldo()}")
print(f"O saldo do Sr {cliente05.nome} é {conta05.get_saldo()}")
