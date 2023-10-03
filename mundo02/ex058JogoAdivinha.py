# o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
maquina = randint(1, 10)
cont = 1

jogador = int(input('\n\nPensei em um número entre 1 e 10. Você Consegue acertar? Qual número eu pensei: '))

while jogador != maquina:
    cont += 1
    if jogador > maquina:
        dica = '\033[1:33mMENOR\033[m'
    if jogador < maquina:
        dica = '\033[1:33mMAIOR\033[m'
    jogador = int(input('\nVocê errou. O número que eu pensei é {}\nQual numero eu pensei : '.format(dica)))
print('\nVocê acertou. Precisou de {} tentativas'.format(cont))

