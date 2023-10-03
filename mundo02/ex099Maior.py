#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def Maior(*nun):
    if len(nun) == 0:
        nun = [0]
    print('-'*25)
    print(f'Foram informados {len(nun)}')
    print(f'os valores são {nun}')
    print(f'O maior valor é {max(nun)}')
    sleep(0.5)


Maior(2, 9, 4, 5, 7, 1)
Maior(4, 7, 0)
Maior(1, 2)
Maior(6)
Maior()
