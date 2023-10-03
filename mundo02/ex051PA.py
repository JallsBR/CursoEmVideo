# Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-=-=- PROGRESSÃO ARITMÉTICA -=-=-')
termo = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a razão: '))

for c in range (termo, termo+10*razão, razão):
    print(c, end=' ')
