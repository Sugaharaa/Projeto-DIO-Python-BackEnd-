saldo = 0
retiradas = []
depositos = []
quantidade_saques = 0
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500


def saque(valor):
    global saldo, quantidade_saques

    if valor <= 0:
        return "Valor de saque inválido."

    if quantidade_saques >= LIMITE_SAQUES:
        return "Limite de saques diários atingido."

    if valor > LIMITE_POR_SAQUE:
        return "Não é possível sacar valores acima de R$ 500,00."

    if valor > saldo:
        return "Saldo insuficiente para realizar o saque."

    saldo -= valor
    retiradas.append(valor)
    quantidade_saques += 1

    return f"Saque realizado com sucesso. Saldo atual: R$ {saldo:.2f}"


def deposito(valor):
    global saldo

    if valor <= 0:
        return "Valor de depósito inválido. O valor deve ser positivo."

    saldo += valor
    depositos.append(valor)

    return f"Depósito realizado com sucesso. Saldo atual: R$ {saldo:.2f}"


def extrato():
    texto_extrato = "\n========== EXTRATO ==========\n"

    if not depositos and not retiradas:
        texto_extrato += "Não foram realizadas movimentações.\n"
    else:
        texto_extrato += "\nDepósitos:\n"

        if depositos:
            for valor in depositos:
                texto_extrato += f"+ R$ {valor:.2f}\n"
        else:
            texto_extrato += "Nenhum depósito realizado.\n"

        texto_extrato += "\nSaques:\n"

        if retiradas:
            for valor in retiradas:
                texto_extrato += f"- R$ {valor:.2f}\n"
        else:
            texto_extrato += "Nenhum saque realizado.\n"

    texto_extrato += f"\nSaldo atual: R$ {saldo:.2f}"
    texto_extrato += "\n============================="

    return texto_extrato


while True:
    print("\nBem-vindo ao Sistema Bancário")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor_saque = float(input("Digite o valor do saque: R$ "))
            print(saque(valor_saque))
        except ValueError:
            print("Digite um valor numérico válido.")

    elif opcao == "2":
        try:
            valor_deposito = float(input("Digite o valor do depósito: R$ "))
            print(deposito(valor_deposito))
        except ValueError:
            print("Digite um valor numérico válido.")

    elif opcao == "3":
        print(extrato())

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")