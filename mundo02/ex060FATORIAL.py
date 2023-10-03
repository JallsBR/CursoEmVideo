# Faça um programa que leia um número qualquer e mostre o seu fatorial. n! = n . (n – 1)
n = int(input('Digite um número: '))
count = n
total = 0
print('Calculando {}! = {}'.format(n, n), end='')

while n!= 1:
    count = count *(n-1)
    n -= 1
    print(' x {}'.format(n), end='')
print(' = {}'.format(count))

