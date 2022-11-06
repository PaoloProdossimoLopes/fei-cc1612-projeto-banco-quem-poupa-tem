import validator
import helpers as helper
import useCases as useCase
import Logger as log
import Constant


def lidando_opcao(opcao):
    if validator.eh_novo_cliente(opcao):
        useCase.executar_opcao_novo_cliente()

    elif validator.eh_deletat_cliente(opcao):
        useCase.executar_opcao_deletando_cliente()

    elif validator.eh_debito(opcao):
        useCase.executar_opcao_debito()

    elif validator.eh_deposito(opcao):
        useCase.executar_opcao_deposito()

    elif validator.eh_extrato(opcao):
        useCase.executar_opcao_extrato()

    elif validator.eh_transferencia(opcao):
        useCase.executar_opcao_transferencia()

    elif validator.eh_opcao_livre(opcao):
        useCase.executar_opcao_livre()

    else:
        useCase.executar_opcao_sair()

def escolhendo_opcao(opcao):

    (OPCAO_MIN, OPCAO_MAX) = (0, 8)
    CODIGO_PARA_LOOP = -1

    if opcao in range(OPCAO_MIN, OPCAO_MAX):
        try: lidando_opcao(opcao)
        except: return CODIGO_PARA_LOOP

    else:
        log.error(Constant.RANGE_NUMBERS_OPTIONS_ERROR_MESSAGE)   
        recebendo_opcao()


def recebendo_opcao():
    try:
        opcao = int(input(Constant.CHOSE_OPTION_PLACEGOLDER))
        return escolhendo_opcao(opcao)

    except:
        log.error(Constant.ONLY_NUMBER_ERRORMESSAGE)
        recebendo_opcao()  


def run():
    while True:
        helper.imprime_menu()
        if recebendo_opcao() != None: break

if __name__ == '__main__':
    run()
