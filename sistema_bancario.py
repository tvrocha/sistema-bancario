def menu_opçoes():
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


def menu_cadastro():
    opcao_cadastro = input("""
================================
Sistema Bancário - Cadastro
================================

[1] - Cadastrar
[2] - Já tenho cadastro
[0] - Sair

Entre com a opção: """)
    return opcao_cadastro


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


def saque(*, saldo, extrato, qtde_saque, LIMITE_SAQUE, LIMITE_VALOR_SAQUE):
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


def imprimir_extrato(saldo, clientes, cpf, /, *, extrato):
    if extrato:
        print(f"""
================================
    Extrato
================================

Agência: {clientes[cpf]['Ag']}
Conta: {clientes[cpf]['Conta']}
Titular: {clientes[cpf]['Nome']}
""")
        print(extrato)
        print(f'\nSaldo: R${saldo:,.2f}')
    else:
        print(f"""
================================
    Extrato
================================

Agência: {clientes[cpf]['Ag']}
Conta: {clientes[cpf]['Conta']}
Titular: {clientes[cpf]['Nome']}
""")
        print('\nNão houve movimentações.')


def criar_conta(lista_clientes):
    conta_corrente = len(lista_clientes) + 1
    return conta_corrente


def cadastrar(lista_clientes):
    cpf = input("""
================================
    Cadastro
================================

Entre com CPF (apenas números): """)
    if cpf in lista_clientes:
        print('Usuário já cadastrado.')
        return lista_clientes
    else:        
        nome = input('Entre com o nome completo: ')
        logradouro = input('Entre com a rua: ')
        numero = input('Entre com o número: ')
        bairro = input('Entre com o bairro: ')
        cidade = input('Entre com a cidade: ')
        estado = input('Entre com o estado: ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}'
        conta = criar_conta(lista_clientes)
        lista_clientes[cpf] = {"Nome": nome, "Endereço": endereco, "Saldo": 0, "Extrato": '', "Qtde_saque": 0, 'Ag': '0001', 'Conta': conta}
        return lista_clientes  


def login(lista_clientes):
    cpf = input("""
================================
    Login
================================

Entre com CPF (apenas números): """)
    if cpf in lista_clientes:
        print(f'Bem vindo, {lista_clientes[cpf]["Nome"]}!')
        return cpf
    else:
        print('Usuário não encontrado.')
        return None


saldo = 0
extrato = ''
qtde_saque = 0
clientes = {}

# Constante de quantidades de saque e valor máximo de saque
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500


while True:

    sair = False
    usuario_atual = None

    while not usuario_atual:

        cadastro = menu_cadastro()

        if cadastro == '1':
            # função cadastrar (CPF, Nome, Endereço e Criar Conta [Agencia: 0001])
            clientes = cadastrar(clientes)
            break
        
        elif cadastro == '2':
            # função verificar cadastro
            usuario_atual = login(clientes)
        
        elif cadastro == '0':
            print("""
================================
    FIM DO PROGRAMA
================================""")
            sair = True
            break
        
        else:
            print("""
================================
    Opção Inválida
================================""")
    if sair:
        break

    while usuario_atual:

        opcao = menu_opçoes()
        saldo = clientes[usuario_atual]['Saldo']
        extrato = clientes[usuario_atual]['Extrato']
        qtde_saque = clientes[usuario_atual]['Qtde_saque']

        if opcao == '1':
            saldo, extrato = deposito(saldo, extrato)
            clientes[usuario_atual]['Saldo'] = saldo
            clientes[usuario_atual]['Extrato'] = extrato

        elif opcao == '2':
            saldo, extrato, qtde_saque = saque(saldo=saldo, extrato=extrato, qtde_saque=qtde_saque, LIMITE_SAQUE=LIMITE_SAQUE, LIMITE_VALOR_SAQUE=LIMITE_VALOR_SAQUE)
            clientes[usuario_atual]['Saldo'] = saldo
            clientes[usuario_atual]['Extrato'] = extrato
            clientes[usuario_atual]['Qtde_saque'] = qtde_saque
        
        elif opcao == '3':
            imprimir_extrato(saldo, clientes, usuario_atual, extrato=extrato)
        
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
    