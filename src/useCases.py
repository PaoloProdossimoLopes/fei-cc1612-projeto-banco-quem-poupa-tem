import validator
import fileManager
import Constant
import useCaseHelpers as useCaseHelper


def executar_opcao_novo_cliente():
    nome = input(Constant.NAME_PLACEHOLDER)
    cpf = input(Constant.CPF_PLACEHOLDER)
    senha = input(Constant.PASSWORD_PLACEHOLDER)
    tipo_conta = validator.validando_tipo_conta()
    valor_inicial = validator.validando_valor(Constant.INITIAL_ACCOUNT_VALUE)
    json = useCaseHelper.criaClienteDict(cpf, nome, tipo_conta, valor_inicial, senha)
    useCaseHelper.cadastrarCliente(cpf, json)

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

        useCaseHelper.registarar_evento(origem_cpf, -valor)
        useCaseHelper.registarar_evento(destino_cpf, valor)
    except:
        print(Constant.OCCOUR_AN_ERROR_MESSAGE)
        executar_opcao_transferencia()


def executar_opcao_livre():
    pass


def executar_opcao_sair():
    print(Constant.THANKS_MESSAGE)
    raise 

def debitar(cpf, senha, valor):
    dict_json = fileManager.load()

    if dict_json[cpf][Constant.PASSWORD_KEY] == senha:
        dict_json[cpf][Constant.VALUE_KEY] -= valor
        fileManager.save(dict_json)
        
    else:
        print(Constant.DATA_INVALID_TRY_AGAIN_ERROR_MESSAGE)
        executar_opcao_debito()
        return
    
def depositar(cpf, valor):
    dict_json = fileManager.load()
    dict_json[cpf][Constant.VALUE_KEY] += valor
    fileManager.save(dict_json)