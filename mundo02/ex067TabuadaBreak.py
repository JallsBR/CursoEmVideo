# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-+/*'*10)
print(f'Tabuada')
print('-+/*'*10)

número = int(input('Digite um número:'))
cont = 1
while True:
    while cont <=10:
        print(f'{número} x {cont} = {número*cont}')
        cont += 1
    número = int(input(f'Digite um número:'))
    cont = 1
    if número < 0:
        break
print('-+/*'*10)
print('Fim do programa!!')