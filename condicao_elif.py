opcao = int(input("Informe uma opção: [1] Sacar \n [2] Consultar extrato"))

if opcao == 1:
    valor = float(input("Informe o valor para saque: "))

elif opcao == 2:
    print("Exibindo extrato...")
else: sys.exit("Opcão invalida")