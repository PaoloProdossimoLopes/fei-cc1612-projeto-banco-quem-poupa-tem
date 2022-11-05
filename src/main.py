import json
import datetime

import validator
import fileManager
import helpers as helper

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
    senha = input('Senha: ')
    tipo_conta = validando_tipo_conta()
    valor_inicial = validando_valor('Valor inicial da conta:')
    json = criaClienteDict(cpf, nome, tipo_conta, valor_inicial, senha)
    cadastrarCliente(cpf, json)

def cadastrarCliente(cpf, json_dict):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        fileManager.save(json_dict)
        run()

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
    valor = validando_valor('Valor:')

    debitar(cpf, senha, valor)
    registarar_evento(cpf, valor)

def registarar_evento(cpf, valor):
    dic = {}
    try:
        dic = fileManager.load()
    except:
        print('ainda nao registrado!')
        run()

    literal_tarifa = dic[cpf]['tipo']

    tarifa = 0.0
    if literal_tarifa == 'comum' and valor < 0:
        tarifa = valor * 0.05
    elif literal_tarifa == 'plus' and valor < 0:
        tarifa = valor * 0.03

    saldo = dic[cpf]['valor']
    today = datetime.datetime.now()
    eventos = dic[cpf]['eventos']

    indicator = ''
    if valor > 0:
        indicator = '+'
    else:
        valor = -valor
        indicator = '-'

    lancamento = f'Data: {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second} {indicator} {valor} Tarifa: {tarifa} Saldo: {saldo}'
    eventos.append(lancamento)
    dic[cpf]['eventos'] = eventos

    fileManager.save(dic)

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
    valor = validando_valor('Valor:')

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
    valor = validando_valor('Valor:')

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


def lidando_opcao(opcao):
    if validator.eh_novo_cliente(opcao):
        executar_opcao_novo_cliente()

    elif validator.eh_deletat_cliente(opcao):
        executar_opcao_deletando_cliente()

    elif validator.eh_debito(opcao):
        executar_opcao_debito()

    elif validator.eh_deposito(opcao):
        executar_opcao_deposito()

    elif validator.eh_extrato(opcao):
        executar_opcao_extrato()

    elif validator.eh_transferencia(opcao):
        executar_opcao_transferencia()

    elif validator.eh_opcao_livre(opcao):
        executar_opcao_livre()

    else:
        executar_opcao_sair()
        raise 

def escolhendo_opcao(opcao):

    (OPCAO_MIN, OPCAO_MAX) = (0, 8)
    CODIGO_PARA_LOOP = -1

    if opcao in range(OPCAO_MIN, OPCAO_MAX):
        try: lidando_opcao(opcao)
        except: return CODIGO_PARA_LOOP

    else:
        print('❌ Opção invalida! Escolha um numero entre 0 - 7.')   
        recebendo_opcao()


def recebendo_opcao():
    try:
        opcao = int(input('Oque deseja realizar no banco? '))
        return escolhendo_opcao(opcao)

    except:
        print('❌ Opção invalida! Escolha apenas numeros.')
        recebendo_opcao()  


def run():
    while True:
        helper.imprime_menu()
        if recebendo_opcao() != None: break
        


if __name__ == '__main__':
    run()
