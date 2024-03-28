from time import sleep
from os import system


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar esse número')
            return 0
        else:
            return n


def desenha_linha(n=40):
    print('-' * n)


def limpa_tela():
    system('cls')


def cabecalho(txt):
    limpa_tela()
    desenha_linha()
    print(f'{txt:^40}')
    desenha_linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    desenha_linha()
    opc = leiaInt('Sua Opção: ')
    return opc