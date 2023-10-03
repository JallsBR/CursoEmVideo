# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idade = maiores = totalhomens = mulheresmenores = contador = 0
sexo = ''

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F/Outro]: ')).strip().upper()[0]
    contador += 1
    if idade >=18:
        maiores += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade<20:
        mulheresmenores += 1
    interromper = str(input('Quer finalizar o programa: [S/N]: ')).strip().upper()[0]
    while interromper not in 'SsNn':
        interromper = str(input('INVÁLIDO. Quer finalizar o programa: [S/N]: ')).strip().upper()[0]
    if interromper == 'S':
        break
print(f'Foram {contador} cadastrado(s). {totalhomens} homens. Tivemos {mulheresmenores} Mulheres abaixo de 20 anos. {maiores} são maiores de idade.')
print('\nFim do programa')