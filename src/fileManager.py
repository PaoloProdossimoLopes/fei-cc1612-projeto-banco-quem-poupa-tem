import json

def load():
    dict_json = {}
    with abrir_arquivo_leitura() as arquivo:
        dict_json = json.load(arquivo)
    return dict_json

def save(new):
    with abrir_arquivo_escrita() as arquivo:
        json.dump(new, arquivo)

def nome_arquivo_clientes():
    return 'clientes.json'

def abrir_arquivo_leitura():
    return open(nome_arquivo_clientes(), "r")

def abrir_arquivo_escrita():
    return open(nome_arquivo_clientes(), "w")
