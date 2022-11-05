import datetime

import Constant
import fileManager
import main

def cadastrarCliente(cpf, json_dict):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        fileManager.save(json_dict)
        main.run()

    dic[cpf] = json_dict[cpf]

    fileManager.save(dic)

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
