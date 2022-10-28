from http import client
import json


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


def abrir_arquivo_leitura():
    return open(nome_arquivo_clientes(), "r")


def abrir_arquivo_escrita():
    return open(nome_arquivo_clientes(), "w")


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
        with abrir_arquivo_leitura() as file:
            dic = json.load(file)
    except:
        with abrir_arquivo_escrita() as arquivo:
            json.dump(json_dict, arquivo)
            run()

    dic[cpf] = json_dict[cpf]
    print('DEBUG:', dic)

    with abrir_arquivo_escrita() as arquivo:
        json.dump(dic, arquivo)

def nome_arquivo_clientes():
    return 'clientes.json'

def cliente_ainda_nao_esta_registardo(cpf, clientes_registrados):
    cpfs = clientes_registrados.keys()
    return (cpf in cpfs) == False

def pega_clientes_resgistrados(file):
    arquivo = abrir_arquivo_leitura()
    clientes = json.load(arquivo)
    arquivo.close()
    return clientes

def registrar_cliente(cliente_info, nome_arquivo):
    arquivo = abrir_arquivo_escrita()
    json_dict = json.load(arquivo)
    json_dict.update(cliente_info)
    json.dump(json_dict, arquivo, indent=4)
    arquivo.close()
    

def criaClienteDict(cpf, nome, tipo, valor, senha):
    cliente = dict()

    cliente['nome'] = nome
    cliente['tipo'] = tipo
    cliente['valor'] = valor
    cliente['senha'] = senha

    cliente_informacao = dict()
    cliente_informacao[cpf] = cliente

    return cliente_informacao

def executar_opcao_deletando_cliente():
    cpf = input('CPF: ')

    dict = {}
    with abrir_arquivo_leitura() as arquivo:
        dict = json.load(arquivo)
    
    dict.pop(cpf, None)

    with abrir_arquivo_escrita() as arquivo:
        json.dump(dict, arquivo)



def executar_opcao_debito():
    cpf = input('CPF: ')
    senha = input('Senha: ')
    valor = validando_valor('Valor:')

    debitar(cpf, senha, valor)


def debitar(cpf, senha, valor):
    dict_json = {}
    with abrir_arquivo_leitura() as arquivo:
        dict_json = json.load(arquivo)

    if dict_json[cpf]['senha'] == senha:
        dict_json[cpf]['valor'] -= valor
    else:
        print('❌ Dados da conta invalido, tente novamente!')
        executar_opcao_debito()
        return

    with abrir_arquivo_escrita() as arquivo:
        json.dump(dict_json, arquivo)


def executar_opcao_deposito():
    cpf = input('CPF: ')
    valor = validando_valor('Valor:')
    depositar(cpf, valor)


def executar_opcao_extrato():
    cpf = input('CPF: ')
    senha = input('Senha: ')


def executar_opcao_transferencia():
    origem_cpf = input('CPF (Origem): ')
    origem_senha = input('Senha (Origem): ')
    destino_cpf = input('CPF (Destino): ')
    valor = validando_valor('Valor:')

    try:
        debitar(origem_cpf, origem_senha, valor)
        depositar(destino_cpf, valor)
    except:
        print("❌ Ocorreu um erro no processo, tente novamente")
        executar_opcao_transferencia()

    
def depositar(cpf, valor):
    dict_json = {}
    with abrir_arquivo_leitura() as arquivo:
        dict_json = json.load(arquivo)

    dict_json[cpf]['valor'] += valor

    with abrir_arquivo_escrita() as arquivo:
        json.dump(dict_json, arquivo)

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
        imprime_menu()
        if recebendo_opcao() != None: break
        


if __name__ == '__main__':
    run()
