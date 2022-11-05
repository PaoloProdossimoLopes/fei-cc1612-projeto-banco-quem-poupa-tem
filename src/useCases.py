import datetime

import validator
import fileManager
import Constant
import main


def executar_opcao_novo_cliente():
    nome = input(Constant.NAME_PLACEHOLDER)
    cpf = input(Constant.CPF_PLACEHOLDER)
    senha = input(Constant.PASSWORD_PLACEHOLDER)
    tipo_conta = validator.validando_tipo_conta()
    valor_inicial = validator.validando_valor(Constant.INITIAL_ACCOUNT_VALUE)
    json = criaClienteDict(cpf, nome, tipo_conta, valor_inicial, senha)
    cadastrarCliente(cpf, json)

def cadastrarCliente(cpf, json_dict):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        fileManager.save(json_dict)
        main.run()

    dic[cpf] = json_dict[cpf]

    fileManager.save(dic)

def cliente_ainda_nao_esta_registardo(cpf, clientes_registrados):
    cpfs = clientes_registrados.keys()
    return (cpf in cpfs) == False

def criaClienteDict(cpf, nome, tipo, valor, senha):
    cliente = dict()

    cliente[Constant.NAME_KEY] = nome
    cliente[Constant.TYPE_KEY] = tipo
    cliente[Constant.VALUE_KEY] = valor
    cliente[Constant.PASSWORD_KEY] = senha
    cliente[Constant.EVENTS_KEYS] = []

    cliente_informacao = dict()
    cliente_informacao[cpf] = cliente

    return cliente_informacao

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
    registarar_evento(cpf, valor)

def registarar_evento(cpf, valor):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        print(Constant.ERROR_ON_REGISTER_EVENT_MESSAGE)
        main.run()
        return

    literal_tarifa = dic[cpf][Constant.TYPE_KEY]
    tarifa = chose_tax(literal_tarifa, valor)

    saldo = dic[cpf][Constant.VALUE_KEY]
    eventos = dic[cpf][Constant.EVENTS_KEYS]
    today = datetime.datetime.now()

    indicator = chose_indicator(valor)
    valor = abs(valor)

    lancamento = f'Data: {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second} {indicator} {valor} Tarifa: {tarifa} Saldo: {saldo}'
    eventos.append(lancamento)
    dic[cpf][Constant.EVENTS_KEYS] = eventos

    fileManager.save(dic)


def chose_tax(literal, value):

    is_debit_operation = value < 0
    if literal == Constant.COMMON_TYPE_LITERAL and is_debit_operation:
        return value * Constant.COMMON_TAX
    elif literal == Constant.PLUS_TYPE_LITERAL and is_debit_operation:
        return value * Constant.PLUS_TAX
    else:
        return 0.0

def chose_indicator(value):
    if value > 0:
        return Constant.POSITIVE_SYMBOL
    else:
        return Constant.NEGATIVE_SYMBOL

def debitar(cpf, senha, valor):
    dict_json = fileManager.load()

    if dict_json[cpf][Constant.PASSWORD_KEY] == senha:
        dict_json[cpf][Constant.VALUE_KEY] -= valor
        fileManager.save(dict_json)
        
    else:
        print(Constant.DATA_INVALID_TRY_AGAIN_ERROR_MESSAGE)
        executar_opcao_debito()
        return
    

def executar_opcao_deposito():
    cpf = input(Constant.CPF_PLACEHOLDER)
    valor = validator.validando_valor(Constant.VALUE_PLACEHOLDER)

    depositar(cpf, valor)
    registarar_evento(cpf, valor)


def executar_opcao_extrato():
    cpf = input(Constant.CPF_PLACEHOLDER)
    senha = input(Constant.PASSWORD_PLACEHOLDER)

    contas = fileManager.load()
    if contas[cpf][Constant.PASSWORD_KEY] == senha:        
        print('Conta:', contas[cpf][Constant.TYPE_KEY])
        eventos = contas[cpf][Constant.EVENTS_KEYS]
        for evento in eventos:
            print(evento)
    else:
        print(Constant.DATA_IS_INVALID)
        executar_opcao_extrato()

def executar_opcao_transferencia():
    origem_cpf = input(Constant.CPF_ORIGEM_PLACEHOLDER)
    origem_senha = input(Constant.PASSWORD_ORIGEM_PLACEHOLDER)
    destino_cpf = input(Constant.CPF_DESTINO_PLACEHOLDER)
    valor = validator.validando_valor(Constant.VALUE_PLACEHOLDER)

    try:
        debitar(origem_cpf, origem_senha, valor)
        depositar(destino_cpf, valor)

        registarar_evento(origem_cpf, -valor)
        registarar_evento(destino_cpf, valor)
    except:
        print(Constant.OCCOUR_AN_ERROR_MESSAGE)
        executar_opcao_transferencia()

    
def depositar(cpf, valor):
    dict_json = fileManager.load()
    dict_json[cpf][Constant.VALUE_KEY] += valor
    fileManager.save(dict_json)

def executar_opcao_livre():
    pass


def executar_opcao_sair():
    print(Constant.THANKS_MESSAGE)
    raise 