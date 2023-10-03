# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def Contador(inicio, fim, razão):
    c=0
    if razão <0:
        razão*=-1
    if razão==0:
        razão = 1
    contador = inicio
    if inicio < fim:
        while True:
            print(f'{contador} ', end='')
            contador += razão
            if contador > fim:
                break
            sleep(0.2)
    elif fim < inicio:
        while True:
            print(f'{contador} ', end='')
            contador -= razão
            if contador < fim:
                break
            sleep(0.2)







ini = int(input('Digite o início:'))
final = int(input('Digite o final:'))
salto = int(input('Digite a razão:'))
Contador(ini, final, salto)
