# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print('O Maior Número é {}'.format(n1))
if n1 < n2 and n2 > n3:
    print('O Maior Número é {}'.format(n2))
if n1 < n3 and n2 < n3:
    print('O Maior Número é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O Menor Número é {}'.format(n1))
if n1 > n2 and n2 < n3:
    print('O Menor Número é {}'.format(n2))
if n1 > n3 and n2 > n3:
    print('O Menor Número é {}'.format(n3))

# primeiro = int(input('Digite o primeiro número:'))
# segundo = int(input('Digite o segundo número:'))
# terceiro = int(input('Digite o terceiro número:'))
# numeros = [primeiro, segundo, terceiro]
#
# print('O maior valor digitado foi {}'.format(max(numeros)))
# print('O menor numero digitado foi {}'.format(min(numeros)))