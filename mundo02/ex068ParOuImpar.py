#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-='*30)
print('-'*20, ' PAR OU ÍMPAR ','-'*20)
print('-='*30)

jogador = maquina = contador = vitorias = 0
jogada = ''
while True:
    jogador = int(input('Escolha um número: '))
    jogada = str(input('Par ou impar [P/I]: ')).strip().upper()[0]
    while jogada not in 'PpIi':
        jogada = str(input('Par ou impar [P/I]: ')).strip().upper()[0]
    maquina = randint(0, 5)
    print(f'A maquina escolheu {maquina}')
    contador += 1
    if (jogador + maquina)%2 == 0 and jogada[0] == 'P':
        print('Jogador vence!')
        vitorias += 1
    elif (jogador + maquina)%2 == 1 and jogada[0] == 'I':
        print('Jogador vence!')
        vitorias += 1
    else:
        print('Máquina vence!')
        break
    print('-=' * 30)
print(f'Você venceu {vitorias} vezes em {contador} jogo(s). Fim do programa')

