def run():
    while True:
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

        try:
            opcao = int(input('Oque deseja realizar no banco? '))

        except:
            print('Opção invalida! selecione uma opcao valida para continuar.')
