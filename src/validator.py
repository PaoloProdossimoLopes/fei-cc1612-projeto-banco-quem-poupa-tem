import Logger as log


def validando_valor(mensagem):
    try:
        valor = float(input(mensagem + ' '))
        return valor
    except:
        print('❌ Valor invalido! Informe apenas numeros.')
        return validando_valor(mensagem)


def validando_tipo_conta():
    tipo_conta = input('Tipo de conta: ')
    tipo_conta = tipo_conta.lower()

    if tipo_conta == 'comum' or tipo_conta == 'plus':
        return tipo_conta
    
    else:
        log.error('Tipo de conta invalida! Escolha um tipo de conta valida (comum ou plus)')
        validando_tipo_conta()

def validate_cpf(cpf):
    if (('-' in cpf) or ('.' in cpf)):
        log.error('Coloque apenas numeros')
        return False
    elif len(cpf) < 11:
        return False   
    else:
        return True

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