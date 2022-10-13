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

def novo_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    tipo_conta = input('Tipo de conta: ')
    valor_inicial = input('Valor inicial da conta: ')

def run():
    while True:
        imprime_menu()

        try:
            opcao = int(input('Oque deseja realizar no banco? '))
            if opcao in range(1, 9):
                if (opcao == 1):
                    novo_cliente()

                elif (opcao == 2):
                    print('Apagar cliente')
                elif (opcao == 3):
                    print('Débito')
                elif (opcao == 4):
                    print('Déposito')  
                elif (opcao == 5):
                    print('Extrato')  
                elif (opcao == 6):
                    print('Transferencia entre contas')
                elif (opcao == 7):
                    print('Operação livre')
                else:
                    print('Obrigado por usar nosos serviços!')
                    break
            else:
                alerta_de_opcao_invalida()

        except:
            alerta_de_opcao_invalida()


if __name__ == '__main__':
    run()
