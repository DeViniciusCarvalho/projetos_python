saldo = 1000
saque = 250
limite = 200
conta_especial = True


print(True and True) #AND os dois precisam ser true
print(True and False)
print(True or False) #Or apenas uma das variáveis precisam ser true
print(True or True)


exp_1=(saldo >= saque and saque <= limite) or (conta_especial and saldo>= saldo)
print(exp_1)