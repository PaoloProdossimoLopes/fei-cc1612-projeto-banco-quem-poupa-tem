import Logger as log
import Constant

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
    log.log()
    log.log(header)

def imprime_extrato(tipo_conta, eventos):
    print('\n** Extrato **')
    print('*' * 14)
    print('🏷 Conta:', tipo_conta)
    
    for evento in eventos:
        if Constant.POSITIVE_SYMBOL in evento:
            log.incame(evento)
        else:
            log.spend(evento)

    log.log(f'* FIM DO EXTRATO *****\n')
