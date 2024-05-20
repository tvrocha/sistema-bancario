def menu():
    opcao = input("""
================================
   Menu - Sistema Bancário
================================

[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair

Entre com a opção: """
    )
    return opcao


def deposito(saldo, extrato):
    deposito = float(input("""
================================
    Depósito
================================

[1] - Depósito

Valor a depositar: R$"""))
    if deposito > 0:
        saldo += deposito
        info_extrato = f"""
------
[DEPÓSITO] - R${deposito:,.2f}
------"""
        extrato += info_extrato
    else:
        print('Valor inválido! Tente novamente')
    print(f'Saldo: R${saldo:,.2f}')
    print(f'Extrato: \n{info_extrato}')
    return saldo, extrato


def saque(saldo, extrato, qtde_saque, LIMITE_SAQUE, LIMITE_VALOR_SAQUE):
    saque = float(input("""
================================
    SAQUE
================================

[2] - Saque

Valor a sacar: R$"""))
    if qtde_saque >= LIMITE_SAQUE:
        print('\nLimite de saques diários atingido.')
    elif saque > LIMITE_VALOR_SAQUE:
        print('\nValor do saque excede o saque máximo.')
    elif saque > saldo:
        print('\nSaldo insuficiente.')
    elif saque < 0:
        print('\nValor inválido! Tente novamente')
    else:
        saldo -= saque
        info_extrato = f"""
------
[SAQUE] - R${saque:,.2f}
------"""
        extrato += info_extrato
        qtde_saque += 1
        print(f'Saldo: R${saldo:,.2f}')
        print(f'Extrato: \n{info_extrato}')    
    return saldo, extrato, qtde_saque


def imprimir_extrato(saldo, extrato):
    if extrato:
        print(extrato)
        print(f'Saldo: R${saldo:,.2f}')
    else:
        print('\nNão houve movimentações.')


saldo = 0
extrato = ''
qtde_saque = 0

# Constante de quantidades de saque e valor máximo de saque
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500


while True:

    opcao = menu()

    if opcao == '1':
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == '2':
        saldo, extrato, qtde_saque = saque(saldo, extrato, qtde_saque, LIMITE_SAQUE, LIMITE_VALOR_SAQUE)
    
    elif opcao == '3':
        imprimir_extrato(saldo, extrato)
    
    elif opcao == '0':
        print("""
================================
    FIM DO PROGRAMA
================================""")
        break

    else:
        print("""
================================
    Opção Inválida
================================""")
    