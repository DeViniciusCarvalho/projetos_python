saque = 111000
saldo = 12200

status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque!")