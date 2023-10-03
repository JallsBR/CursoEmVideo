#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
soma = 0
menor = 0
maior = 0

teste = str(input('Você quer digitar um número [S/N]')).strip().upper()
while teste =='S':
    n = int(input('Digite um número:'))
    soma += n
    contador +=1
    if menor==0 and maior == 0:
        maior = n
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor=n
    teste = str(input('Você quer digitar um número [S/N]')).strip().upper()
    while teste != 'S' and teste != 'N':
        teste = str(input('Entrada Inválida. Você quer digitar um número [S/N]')).strip().upper()
if contador>1:
    print('A média dos {} númeoros foi de {}'.format(contador, soma/contador))
    print('O Menor foi {} e o Maior foi {}'.format(menor, maior))

