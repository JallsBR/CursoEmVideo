# Crie um programa que faça o computador jogar Jokenpô com você
import random
a = '\033[1:33mPedra\033[m'
b = '\033[1:33mPapel\033[m'
c = '\033[1:33mTesoura\033[m'
lista = [a, b, c]

print(f'{" JOGO Pedra, Papel e Tesoura ":-^40}')
vezes  = (int(input('Quantas vezes você quer jogar Pedra papel e tesoura? ')))

for g in range (1, vezes+1):
    print('\n\n')
    proximo = input('Vamos Lá! Esta é a {} vez, faltam {}.Pressione \033[33mENTER\033[m para começar:'.format(g, vezes-g))
    maquina = random.choice(lista)
    print('\033[1:36m-=\033[m'*15)
    print('\033[1:33mPEDRA, PAPEL OU TESOURA!!! \033[m')
    print('\033[1:36m-=\033[m'*15)
    jogador = int(input('\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n'))

    # Ajuste de Jogador

    if jogador == 1:
        jogador = a
    elif jogador == 2:
        jogador = b
    elif jogador == 3:
        jogador = c
    print('Você escolheu {} e a maquina escolheu {}'.format(jogador, maquina))
    if jogador == maquina:
        print('Ninguém ganha')
    elif (jogador == a and maquina == c) or (jogador == b and maquina == a) or (jogador == c and maquina == b):
        print('{} maior que {},\033[1:36mJogador\033[m Vence!!! Parabéns'.format(jogador, maquina))
    elif (jogador == c and maquina == a) or (jogador == a and maquina == b) or (jogador == b and maquina == c):
        print('{} maior que {}, \033[1:36mMáquina\033[m Vence!!! Mais sorte da próxima vez!'.format(maquina, jogador))
    else:
        print('Erro... que vergonha... você encontrou um bug!')
    print('\033[1:36m-=\033[m'*25)

