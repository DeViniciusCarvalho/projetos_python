conta_normal = True
conta_universitaria = False
saldo = 1900
saque = 100
cheque_especial = 1400

if conta_normal:
    if saldo >= saque:
        print ("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print ("Saque realizado com sucesso com cheque especial")
    else:
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo>= saque : 
        print("Saque realizado com sucesso!")
    else:
      print ("Limite insuficiente!")