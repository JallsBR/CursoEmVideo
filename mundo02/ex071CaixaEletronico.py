#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('{:-^40}'.format(' Caixa eletrônico '))
valor = int(input('Qual será o valor a ser sacado: R$ '))
nota50 = valor//50
resto50 = valor%50
not20 = resto50//20
resto20 = resto50%20
nota10 = resto20//10
nota1 = resto20%10
print('{:-^40}'.format(' Saque '))
if nota50 > 1:
    print(f'Você receberá {nota50} notas de R$50')
if not20 > 1:
    print(f'Você receberá {not20} notas de R$20')
if nota10>1:
    print(f'Você receberá {nota10} notas de R$10')
if nota1>1:
    print(f'Você receberá {nota1} notas de R$1')

print('{:-^40}'.format(' FIM '))