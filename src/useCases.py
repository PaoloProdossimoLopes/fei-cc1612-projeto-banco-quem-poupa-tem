import datetime

import validator
import fileManager

import main

def executar_opcao_novo_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    senha = input('Senha: ')
    tipo_conta = validator.validando_tipo_conta()
    valor_inicial = validator.validando_valor('Valor inicial da conta:')
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

    cliente['nome'] = nome
    cliente['tipo'] = tipo
    cliente['valor'] = valor
    cliente['senha'] = senha
    cliente['eventos'] = []

    cliente_informacao = dict()
    cliente_informacao[cpf] = cliente

    return cliente_informacao

def executar_opcao_deletando_cliente():
    cpf = input('CPF: ')

    dict = fileManager.load()
    
    dict.pop(cpf, None)

    fileManager.save(dict)

def executar_opcao_debito():
    cpf = input('CPF: ')
    senha = input('Senha: ')
    valor = validator.validando_valor('Valor:')

    debitar(cpf, senha, valor)
    registarar_evento(cpf, valor)

def registarar_evento(cpf, valor):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        print('ainda nao registrado!')
        main.run()

    literal_tarifa = dic[cpf]['tipo']
    tarifa = chose_tax(literal_tarifa, valor)

    saldo = dic[cpf]['valor']
    today = datetime.datetime.now()
    eventos = dic[cpf]['eventos']

    indicator = chose_indicator(valor)
    valor = abs(valor)

    lancamento = f'Data: {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second} {indicator} {valor} Tarifa: {tarifa} Saldo: {saldo}'
    eventos.append(lancamento)
    dic[cpf]['eventos'] = eventos

    fileManager.save(dic)


def chose_tax(literal, value):
    if literal == 'comum' and value < 0:
        return value * 0.05
    elif literal == 'plus' and value < 0:
        return value * 0.03

def chose_indicator(value):
    if value > 0:
        return '+'
    else:
        return '-'

def debitar(cpf, senha, valor):
    dict_json = fileManager.load()

    if dict_json[cpf]['senha'] == senha:
        dict_json[cpf]['valor'] -= valor
    else:
        print('❌ Dados da conta invalido, tente novamente!')
        executar_opcao_debito()
        return

    fileManager.save(dict_json)

def executar_opcao_deposito():
    cpf = input('CPF: ')
    valor = validator.validando_valor('Valor:')

    depositar(cpf, valor)
    registarar_evento(cpf, valor)


def executar_opcao_extrato():
    cpf = input('CPF: ')
    senha = input('Senha: ')

    contas = fileManager.load()

    print('Conta:', contas[cpf]['tipo'])
    eventos = contas[cpf]['eventos']
    for evento in eventos:
        print(evento)

def abrir_arquivo_transferencias_leitura():
    return open('transferencias', "r")

def executar_opcao_transferencia():
    origem_cpf = input('CPF (Origem): ')
    origem_senha = input('Senha (Origem): ')
    destino_cpf = input('CPF (Destino): ')
    valor = validator.validando_valor('Valor:')

    try:
        debitar(origem_cpf, origem_senha, valor)
        depositar(destino_cpf, valor)

        registarar_evento(origem_cpf, -valor)
        registarar_evento(destino_cpf, valor)
    except:
        print("❌ Ocorreu um erro no processo, tente novamente")
        executar_opcao_transferencia()

    
def depositar(cpf, valor):
    dict_json = fileManager.load()
    dict_json[cpf]['valor'] += valor
    fileManager.save(dict_json)

def executar_opcao_livre():
    pass


def executar_opcao_sair():
    print('👋🏼 Obrigado por usar nosos serviços! 👋🏼')
    raise 