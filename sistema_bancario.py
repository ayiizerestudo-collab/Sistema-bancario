def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite por saque.")
    elif saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, saques

def exibir_extrato(saldo, extrato):
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================")

def main():
    saldo = 0.0
    limite = 500.0
    extrato = []
    saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, saques = sacar(saldo, valor, extrato, limite, saques, LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "0":
            print("Encerrando o sistema bancário.")
            break

        else:
            print("Opção inválida.")

main()\n