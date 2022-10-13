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

def executar_opcao_novo_cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    tipo_conta = input('Tipo de conta: ')
    valor_inicial = input('Valor inicial da conta: ')

def executar_opcao_deletando_cliente():
    pass

def executar_opcao_debito():
    cpf = input('CPF: ')
    senha = input('Senha: ')
    valor = float(input('Valor: '))

def executar_opcao_deposito():
    cpf = input('CPF: ')
    valor = float(input('Valor: '))

def executar_opcao_extrato():
    cpf = input('CPF: ')
    senha = input('Senha: ')

def executar_opcao_transferencia():
    origem_cpf = input('CPF (Origem): ')
    origem_senha = input('Senha (Origem): ')
    destino_cpf = input('CPF (Destino): ')
    destino_senha = input('Senha (Destino): ')

def executar_opcao_livre():
    pass

def executar_opcao_sair():
    print('Obrigado por usar nosos serviços!')

def run():
    while True:
        imprime_menu()

        try:
            opcao = int(input('Oque deseja realizar no banco? '))
            if opcao in range(0, 8):
                if (opcao == 1):
                    executar_opcao_novo_cliente()

                elif (opcao == 2):
                    executar_opcao_deletando_cliente()

                elif (opcao == 3):
                    executar_opcao_debito()

                elif (opcao == 4):
                    executar_opcao_deposito()

                elif (opcao == 5):
                    executar_opcao_extrato()

                elif (opcao == 6):
                    executar_opcao_transferencia()

                elif (opcao == 7):
                    executar_opcao_livre()

                else:
                    executar_opcao_sair()
                    break
            else:
                alerta_de_opcao_invalida()

        except:
            alerta_de_opcao_invalida()


if __name__ == '__main__':
    run()
