#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
print('\n\n')
from datetime import date
anoatual= date.today().year
anos18 = anoatual - 18
menores = 0
maiores = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento do numero {} '.format(c)))
    if ano < anos18:
        menores = menores+1
    else:
        maiores = maiores+1
print('\n Temos {} MENORES e {} MAIORES'.format(menores, maiores))
