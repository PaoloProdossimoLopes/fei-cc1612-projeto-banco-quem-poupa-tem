def alerta_de_opcao_invalida():
    print('Opção invalida! selecione uma opcao valida para continuar.')    

def imprime_menu():
    print('''
        OPÇOES DO BANCO:
        1 - Novo cliente
        2 - Apagar cliente
        3 - Débito
        4 - Depósito
        5 - Extrato
        6 - Transferencia entre contas
        7 - 'Operação livre'
        8 - Sair
    ''')

def run():
    while True:
        imprime_menu()

        try:
            opcao = int(input('Oque deseja realizar no banco? '))
            if opcao in range(1, 8):
                pass
            else:
                alerta_de_opcao_invalida()

        except:
            alerta_de_opcao_invalida()
