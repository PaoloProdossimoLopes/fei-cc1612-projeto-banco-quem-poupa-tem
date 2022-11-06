import validator
import fileManager
import Constant
import Logger as log
import useCaseHelpers as useCaseHelper
import helpers as helper


def executar_opcao_novo_cliente():
    nome = input(Constant.NAME_PLACEHOLDER)
    cpf = recieve_cpf()
    senha = input(Constant.PASSWORD_PLACEHOLDER)
    tipo_conta = validator.validando_tipo_conta()
    valor_inicial = validator.validando_valor(Constant.INITIAL_ACCOUNT_VALUE)
    json = useCaseHelper.criaClienteDict(cpf, nome, tipo_conta, valor_inicial, senha)
    useCaseHelper.cadastrarCliente(cpf, json)

def recieve_cpf():
    cpf = input(Constant.CPF_PLACEHOLDER)
    if validator.validate_cpf(cpf):
        return cpf
    else:
        log.error(Constant.CPF_INVALID)
        return recieve_cpf()

def cliente_ainda_nao_esta_registardo(cpf, clientes_registrados):
    cpfs = clientes_registrados.keys()
    return (cpf in cpfs) == False

def executar_opcao_deletando_cliente():
    cpf = input(Constant.CPF_PLACEHOLDER)

    dict = fileManager.load()
    
    dict.pop(cpf, None)

    fileManager.save(dict)

def executar_opcao_debito():
    cpf = input(Constant.CPF_PLACEHOLDER)
    senha = input(Constant.PASSWORD_PLACEHOLDER)
    valor = validator.validando_valor(Constant.VALUE_PLACEHOLDER)

    debitar(cpf, senha, valor)
    useCaseHelper.registarar_evento(cpf, -valor)


def executar_opcao_deposito():
    cpf = input(Constant.CPF_PLACEHOLDER)
    valor = validator.validando_valor(Constant.VALUE_PLACEHOLDER)

    depositar(cpf, valor)
    useCaseHelper.registarar_evento(cpf, valor)


def executar_opcao_extrato():
    cpf = input(Constant.CPF_PLACEHOLDER)
    senha = input(Constant.PASSWORD_PLACEHOLDER)

    contas = fileManager.load()
    if contas[cpf][Constant.PASSWORD_KEY] == senha: 
        eventos = contas[cpf][Constant.EVENTS_KEYS]
        tipo_conta = contas[cpf][Constant.TYPE_KEY]
        helper.imprime_extrato(tipo_conta, eventos)
    else:
        log.error(Constant.DATA_IS_INVALID)
        executar_opcao_extrato()

def executar_opcao_transferencia():
    origem_cpf = input(Constant.CPF_ORIGEM_PLACEHOLDER)
    origem_senha = input(Constant.PASSWORD_ORIGEM_PLACEHOLDER)
    destino_cpf = input(Constant.CPF_DESTINO_PLACEHOLDER)
    valor = validator.validando_valor(Constant.VALUE_PLACEHOLDER)

    try:
        debitar(origem_cpf, origem_senha, valor)
        depositar(destino_cpf, valor)
        log.success(Constant.TRANSFER_SUCCEDED)

        useCaseHelper.registarar_evento(origem_cpf, -valor)
        useCaseHelper.registarar_evento(destino_cpf, valor)
    except:
        log.error(Constant.OCCOUR_AN_ERROR_MESSAGE)
        executar_opcao_transferencia()


def executar_opcao_livre():
    pass


def executar_opcao_sair():
    log.log(Constant.THANKS_MESSAGE)
    raise 

def debitar(cpf, senha, valor):
    dict_json = fileManager.load()

    if dict_json[cpf][Constant.PASSWORD_KEY] == senha:
        dict_json[cpf][Constant.VALUE_KEY] -= valor
        fileManager.save(dict_json)
        log.success(Constant.DEBIT_SUCCEDED)
        
    else:
        log.error(Constant.DATA_INVALID_TRY_AGAIN_ERROR_MESSAGE)
        executar_opcao_debito()
        return
    
def depositar(cpf, valor):
    dict_json = fileManager.load()
    dict_json[cpf][Constant.VALUE_KEY] += valor
    fileManager.save(dict_json)
    log.success(Constant.DEPOSIT_SUCCEDED)