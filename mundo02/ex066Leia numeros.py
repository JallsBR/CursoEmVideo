#Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).


print(' Para parar digite o número 999')
soma = 0
count = 0
n = int(input('Digite um número:'))
while True:
    count += 1
    soma = soma + n
    n = int(input(f'Digite o {count+1}° número:'))
    if n == 999:
        break
print(f'A soma dos {count} números é {soma} e a média é {soma/count:.0f}')
