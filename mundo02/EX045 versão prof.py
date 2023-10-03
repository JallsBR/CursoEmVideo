from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
vezes  = (int(input('Quantas vezes você quer jogar Pedra papel e tesoura? ')))

for g in range (1, vezes+1):
    # print(itens[computador])
    print(('\n 0 - Pedra\n 1 - Papel\n 2 - Tesoura\n'))
    jogador = int(input('Escolha: '))
    computador = randint(0, 2)
    print('-'*25)
    print('Pedra ', end='')
    sleep(0.5)
    print('Papel', end='')
    sleep(0.5)
    print(' e ', end='')
    sleep(0.2)
    print('Tesou', end='')
    sleep(0.3)
    print('ra')
    sleep(0.5)
    print('-'*25)

    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador Jogou {}'.format(itens[jogador]))
    print('-'*25)

    if jogador == computador:
        print('Ninguém ganha')

    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print('{} ganha de {}\n\033[1:33mJogador\033[m Vence!!! Parabéns'.format(itens[jogador], itens[computador]))
    elif (jogador == 2 and computador == 0) or (jogador == 0 and computador == 1) or (jogador == 1 and computador == 2):
        print('{} ganha de {} \n\033[1:33mComputador\033[m Vence!!! Mais sorte da próxima vez!'.format(itens[computador], itens[jogador]))

        print('\033[1:36m-=\033[m' * 25)
