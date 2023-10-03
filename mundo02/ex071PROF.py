#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('{:-^40}'.format(' Caixa eletrônico '))
valor = int(input('Qual será o valor a ser sacado: R$ '))
ced = 50
totalced = 0
while True:
    if valor > ced:
        valor -= ced
        totalced += 1
    elif valor<ced and ced == 50:
        print(f'{totalced} cédulas de R${ced}')
        totalced = 0
        ced = 20
    elif valor < ced and ced == 20:
        print(f'{totalced} cédulas de R${ced}')
        totalced = 0
        ced = 10
    elif valor < ced and ced == 10:
        print(f'{totalced} cédulas de R${ced}')
        totalced = 0
        ced = 1
    elif valor == ced and ced == 1:
        totalced+= 1
        print(f'{totalced} cédulas de R${ced}')
        valor = 0
    elif valor == 0:
        break

print('{:-^40}'.format(' Programa encerrado '))

