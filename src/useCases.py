import datetime

import validator
import fileManager

import main

NAME_PLACEHOLDER = 'Nome: '
CPF_PLACEHOLDER = 'CPF: '
PASSWORD_PLACEHOLDER = 'Senha: '
VALUE_PLACEHOLDER = 'Valor:'
CPF_ORIGEM_PLACEHOLDER = 'CPF (Origem): '
CPF_DESTINO_PLACEHOLDER = 'CPF (Destino): '
PASSWORD_ORIGEM_PLACEHOLDER = 'Senha (Origem): '
INITIAL_ACCOUNT_VALUE = 'Valor inicial da conta:'

NAME_KEY = 'nome'
TYPE_KEY = 'tipo'
VALUE_KEY = 'valor'
PASSWORD_KEY = 'senha'
EVENTS_KEYS = 'eventos'

ERROR_ON_REGISTER_EVENT_MESSAGE = '❌ Erro ao registrar o evento ...'
DATA_INVALID_TRY_AGAIN_ERROR_MESSAGE = '❌ Dados da conta invalido, tente novamente!'
DATA_IS_INVALID = '❌ Dados incorretos'
OCCOUR_AN_ERROR_MESSAGE =  '❌ Ocorreu um erro no processo, tente novamente'
THANKS_MESSAGE = '👋🏼 Obrigado por usar nosos serviços! 👋🏼'

COMMON_TYPE_LITERAL = 'comum'
PLUS_TYPE_LITERAL = 'plus'

COMMON_TAX = 0.05
PLUS_TAX = 0.03

POSITIVE_SYMBOL = '+'
NEGATIVE_SYMBOL = '-'


def executar_opcao_novo_cliente():
    nome = input(NAME_PLACEHOLDER)
    cpf = input(CPF_PLACEHOLDER)
    senha = input(PASSWORD_PLACEHOLDER)
    tipo_conta = validator.validando_tipo_conta()
    valor_inicial = validator.validando_valor(INITIAL_ACCOUNT_VALUE)
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

    cliente[NAME_KEY] = nome
    cliente[TYPE_KEY] = tipo
    cliente[VALUE_KEY] = valor
    cliente[PASSWORD_KEY] = senha
    cliente[EVENTS_KEYS] = []

    cliente_informacao = dict()
    cliente_informacao[cpf] = cliente

    return cliente_informacao

def executar_opcao_deletando_cliente():
    cpf = input(CPF_PLACEHOLDER)

    dict = fileManager.load()
    
    dict.pop(cpf, None)

    fileManager.save(dict)

def executar_opcao_debito():
    cpf = input(CPF_PLACEHOLDER)
    senha = input(PASSWORD_PLACEHOLDER)
    valor = validator.validando_valor(VALUE_PLACEHOLDER)

    debitar(cpf, senha, valor)
    registarar_evento(cpf, valor)

def registarar_evento(cpf, valor):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        print(ERROR_ON_REGISTER_EVENT_MESSAGE)
        main.run()
        return

    literal_tarifa = dic[cpf][TYPE_KEY]
    tarifa = chose_tax(literal_tarifa, valor)

    saldo = dic[cpf][VALUE_KEY]
    eventos = dic[cpf][EVENTS_KEYS]
    today = datetime.datetime.now()

    indicator = chose_indicator(valor)
    valor = abs(valor)

    lancamento = f'Data: {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second} {indicator} {valor} Tarifa: {tarifa} Saldo: {saldo}'
    eventos.append(lancamento)
    dic[cpf][EVENTS_KEYS] = eventos

    fileManager.save(dic)


def chose_tax(literal, value):

    is_debit_operation = value < 0
    if literal == COMMON_TYPE_LITERAL and is_debit_operation:
        return value * COMMON_TAX
    elif literal == PLUS_TYPE_LITERAL and is_debit_operation:
        return value * PLUS_TAX
    else:
        return 0.0

def chose_indicator(value):
    if value > 0:
        return POSITIVE_SYMBOL
    else:
        return NEGATIVE_SYMBOL

def debitar(cpf, senha, valor):
    dict_json = fileManager.load()

    if dict_json[cpf][PASSWORD_KEY] == senha:
        dict_json[cpf][VALUE_KEY] -= valor
        fileManager.save(dict_json)
        
    else:
        print(DATA_INVALID_TRY_AGAIN_ERROR_MESSAGE)
        executar_opcao_debito()
        return
    

def executar_opcao_deposito():
    cpf = input(CPF_PLACEHOLDER)
    valor = validator.validando_valor(VALUE_PLACEHOLDER)

    depositar(cpf, valor)
    registarar_evento(cpf, valor)


def executar_opcao_extrato():
    cpf = input(CPF_PLACEHOLDER)
    senha = input(PASSWORD_PLACEHOLDER)

    contas = fileManager.load()
    if contas[cpf][PASSWORD_KEY] == senha:        
        print('Conta:', contas[cpf][TYPE_KEY])
        eventos = contas[cpf][EVENTS_KEYS]
        for evento in eventos:
            print(evento)
    else:
        print(DATA_IS_INVALID)
        executar_opcao_extrato()

def executar_opcao_transferencia():
    origem_cpf = input(CPF_ORIGEM_PLACEHOLDER)
    origem_senha = input(PASSWORD_ORIGEM_PLACEHOLDER)
    destino_cpf = input(CPF_DESTINO_PLACEHOLDER)
    valor = validator.validando_valor(VALUE_PLACEHOLDER)

    try:
        debitar(origem_cpf, origem_senha, valor)
        depositar(destino_cpf, valor)

        registarar_evento(origem_cpf, -valor)
        registarar_evento(destino_cpf, valor)
    except:
        print(OCCOUR_AN_ERROR_MESSAGE)
        executar_opcao_transferencia()

    
def depositar(cpf, valor):
    dict_json = fileManager.load()
    dict_json[cpf][VALUE_KEY] += valor
    fileManager.save(dict_json)

def executar_opcao_livre():
    pass


def executar_opcao_sair():
    print(THANKS_MESSAGE)
    raise 