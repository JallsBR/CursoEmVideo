# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o
# menor e o maior valor que estão na tupla.
from random import randint
tupla = ( randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f'Os números sorteados são: {tupla}')
print(f'O menor número sorteado é: {sorted(tupla)[0]}')
print(f'O maior número sorteado é: {sorted(tupla)[-1]}')
print('\n')
print(f'O menor número sorteado é: {max(tupla)}')
print(f'O maior número sorteado é: {min(tupla)}')


