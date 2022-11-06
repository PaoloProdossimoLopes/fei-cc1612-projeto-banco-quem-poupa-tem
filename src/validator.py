import Logger as log
import Constant


def validando_valor(mensagem):
    try:
        valor = float(input(mensagem + ' '))
        return valor
    except:
        log.error(Constant.ONLY_NUMBER_ERRORMESSAGE)
        return validando_valor(mensagem)


def validando_tipo_conta():
    tipo_conta = input(Constant.TYPE_ACCOUNT_PLACEHOLDER)
    tipo_conta = tipo_conta.lower()

    if tipo_conta == Constant.COMMON_TYPE_LITERAL or tipo_conta == Constant.PLUS_TYPE_LITERAL:
        return tipo_conta
    
    else:
        log.error(Constant.ACCOUNT_TYPE_ERROR_MESSAGE)
        validando_tipo_conta()

def validate_cpf(cpf):
    if ((Constant.DOT_SYMBOL in cpf) or (Constant.DASH_SYMBOL in cpf)):
        log.error(Constant.ONLY_NUMBER_ERROR_MESSAGE)
        return False
    elif len(cpf) < Constant.CPF_SIZE:
        return False   
    else:
        return True

def eh_novo_cliente(opcao):
    return opcao == Constant.OPTION_REGISTER_CODE


def eh_deletat_cliente(opcao):
    return opcao == Constant.OPTION_DELETE_CODE


def eh_debito(opcao):
    return opcao == Constant.OPTION_DEBIT_CODE


def eh_deposito(opcao):
    return opcao == Constant.OPTION_DEPOSIT_CODE


def eh_extrato(opcao):
    return opcao == Constant.OPTION_BANK_STATEMENT_CODE


def eh_transferencia(opcao):
    return opcao == Constant.OPTION_TRANSFER_CODE


def eh_opcao_livre(opcao):
    return opcao == Constant.OPTION_LIVRE_CODE