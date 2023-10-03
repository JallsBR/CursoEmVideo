# Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-=-=- PROGRESSÃO ARITMÉTICA -=-=-')
termo = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a razão: '))
count = 0
total = 0
print('Os 10 primeiros termos da P.A são\n{}'.format(termo), end='')

while count < 9:
    count += 1
    total += 1
    termo += razão
    print(' {}'.format(termo), end='')

final = int(input('\nQuantos termos você quer mostrar a mais? '))

while final!= 0:
    count = 0
    while count < final:
        count += 1
        total += 1
        termo += razão
        print(' {}'.format(termo), end='')
    final = int(input('\nQuantos termos você quer mostrar a mais? '))
print('{} termos mostrados'.format(total+1))
