menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito; R$ {valor:.2f}\n"
        else:
            print("Operação invalida")
    elif opcao == 's':
        valor = float(input("informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Saldo Insuficiente!")
        elif valor > limite:
            print("Operação falhou! Valor ultrapassa limite permitido")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Saques diarios ultrapassados")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Cheque novamente o valor")

    elif opcao == 'e':
        print(extrato)
    elif opcao == 'q':
        break
    else:
        print("Operação inválida")