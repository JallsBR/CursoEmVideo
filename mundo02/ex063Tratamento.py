# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print(' Para parar digite o número 000')
soma = 0
count = 0
n = int(input('Digite um número:'))
while n != 000:
    count +=1
    soma = soma + n
    n = int(input('Digite o {}° número:'.format(count+1)))
print('A soma dos {} números é {}'.format(count, soma))
