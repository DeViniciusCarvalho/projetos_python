opcao = -1

while opcao != 0:
    opcao = int(input("Selecione uma opção: \n[1] Sacar \n[2] Extrato \n[0] Sair\n"))

    if opcao == 1:
        print("Sacando seu dinheiro, aguarde!")

    elif opcao == 2:
        print("Gerando extrato, aguarde!")

    elif opcao == 0:
        print("Saindo do sistema, até logo!")

    else:
        print("Opção inválida. Tente novamente.")