def imprime_menu():
    header = '''
    ********************************
    Serviços:
    1 - Novo cliente
    2 - Apagar cliente
    3 - Débito
    4 - Depósito
    5 - Extrato
    6 - Transferencia entre contas
    7 - 'Operação livre'
    0 - Sair
    ********************************
    '''
    print(header)


def validando_valor(mensagem):
    try:
        valor = float(input(mensagem + ' '))
        return valor
    except:
        print('❌ Valor invalido! Informe apenas numeros.')
        validando_valor(mensagem)


def validando_tipo_conta():
    tipo_conta = input('Tipo de conta: ')
    tipo_conta = tipo_conta.lower()

    if tipo_conta == 'comum' or tipo_conta == 'plus':
        return tipo_conta
    
    else:
        print('❌ Tipo de conta invalida! Escolha um tipo de conta valida (comum ou plus)')
        validando_tipo_conta()


def executar_opcao_novo_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    tipo_conta = validando_tipo_conta()
    valor_inicial = validando_valor('Valor inicial da conta:')


def executar_opcao_deletando_cliente():
    pass


def executar_opcao_debito():
    cpf = input('CPF: ')
    senha = input('Senha: ')
    valor = validando_valor('Valor:')


def executar_opcao_deposito():
    cpf = input('CPF: ')
    valor = valor = validando_valor('Valor:')


def executar_opcao_extrato():
    cpf = input('CPF: ')
    senha = input('Senha: ')


def executar_opcao_transferencia():
    origem_cpf = input('CPF (Origem): ')
    origem_senha = input('Senha (Origem): ')
    destino_cpf = input('CPF (Destino): ')
    valor = validando_valor('Valor:')


def executar_opcao_livre():
    pass


def executar_opcao_sair():
    print('👋🏼 Obrigado por usar nosos serviços! 👋🏼')


def eh_novo_cliente(opcao):
    return opcao == 1


def eh_deletat_cliente(opcao):
    return opcao == 2


def eh_debito(opcao):
    return opcao == 3


def eh_deposito(opcao):
    return opcao == 4


def eh_extrato(opcao):
    return opcao == 5


def eh_transferencia(opcao):
    return opcao == 6


def eh_opcao_livre(opcao):
    return opcao == 7


def lidando_opcao(opcao):
    if eh_novo_cliente(opcao):
        executar_opcao_novo_cliente()

    elif eh_deletat_cliente(opcao):
        executar_opcao_deletando_cliente()

    elif eh_debito(opcao):
        executar_opcao_debito()

    elif eh_deposito(opcao):
        executar_opcao_deposito()

    elif eh_extrato(opcao):
        executar_opcao_extrato()

    elif eh_transferencia(opcao):
        executar_opcao_transferencia()

    elif eh_opcao_livre(opcao):
        executar_opcao_livre()

    else:
        executar_opcao_sair()
        raise 

def escolhendo_opcao(opcao):

    (OPCAO_MIN, OPCAO_MAX) = (0, 8)
    if opcao in range(OPCAO_MIN, OPCAO_MAX):
        try: lidando_opcao(opcao)
        except: return -1

    else:
        print('❌ Opção invalida! Escolha um numero entre 0 - 7.')   


def run():
    while True:
        imprime_menu()

        try:
            opcao = int(input('Oque deseja realizar no banco? '))
            if escolhendo_opcao(opcao) == -1: break

        except:
            print('❌ Opção invalida! Escolha apenas numeros.')   


if __name__ == '__main__':
    run()
