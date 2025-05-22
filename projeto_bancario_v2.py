from datetime import datetime
import pytz
import textwrap




def menu():
    menu =""" \n ------------- MENU ----------------
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova conta
        [5] Consultar contas
        [6] Novo usuário
        [0] Sair
"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, data_atual):
    if valor <= 0:
        print("O valor inserido é invalido!")
    else:
        extrato += f"[{data_atual.strftime('%d/%m/%Y %H:%M')}] Depósito: +R${valor:.2f}\n"
        saldo += valor
        print("Depósito realizado com sucesso!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, data_atual):
    if saldo < valor:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Limite de saque excedido!")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários excedido!")
    elif valor <= 0:
        print("Valor inválido!")
    else:
        saldo -= valor
        extrato += f"[{data_atual.strftime('%d/%m/%Y %H:%M')}] Saque: -R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato, data_hoje, numero_saques, limite_saques):
    print("\n============ EXTRATO =============")
    print("Nenhuma movimentação a ser exibida" if not extrato else extrato)
    print(f"Saldo atual: R${saldo:.2f}")
    print(f"Saques realizados em {data_hoje}: {numero_saques}/{limite_saques}")
    print("=================================\n")
    return saldo, extrato


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse usuário já está cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Conta criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado. Fluxo de criação encerrado.")


def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}"
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        data_atual = datetime.now(pytz.timezone("America/Sao_Paulo"))
        data_hoje = data_atual.date()

        if opcao == "1":
            try:
                valor = float(input("Informe o valor a depositar: "))
            except ValueError:
                print("Valor inválido!")
                continue
            saldo, extrato = depositar(saldo, valor, extrato, data_atual)

        elif opcao == "2":
            try:
                valor = float(input("Informe o valor a sacar: "))
            except ValueError:
                print("Valor inválido!")
                continue
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                data_atual=data_atual
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato, data_hoje, numero_saques, LIMITE_SAQUES)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida!")


main()