# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número número: '))
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n')
menu = int(input('Escolha: '))
while menu != 5:
    if menu == 1:
        print('{} + {} = {}\n'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('{} x {} = {}\n'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O maior é {}\n'.format(n1))
        else:
            print('O maior é {}\n'.format(n2))
    elif menu == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número número: '))
    else:
        print('Opção inválida')
    sleep(1)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    menu = int(input('\nEscolha: '))
