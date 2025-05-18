menu = '''

[1] Sacar
[2] Depositar
[3] Consultar extrato 
[4] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        
        try:
            valor = float(input("Informe o valor que deseja sacar: "))
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")
            continue  

        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("O valor de saque excede o limite diário!")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"{LIMITE_SAQUES} saques já atingidos no limite diário.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            saldo -= valor
            extrato += f"Saque: -R${valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "2":
       
        try:
            valor = float(input("Informe o valor que deseja depositar: "))
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")
            continue  

        if valor <= 0:
            print("Valor inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: +R${valor:.2f}\n"
            print("Depósito realizado com sucesso!")

    elif opcao == "3":
        print("\n====== EXTRATO ======")
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print("=====================\n")

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida. Tente novamente.")