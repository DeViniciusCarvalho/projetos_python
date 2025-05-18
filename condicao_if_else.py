saldo = 3000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print ("Realizando o saque, aguarde!")

if saldo < saque: 
    print("Saldo insuficiente!") #SOMENTE IF


saldo = 7000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")
