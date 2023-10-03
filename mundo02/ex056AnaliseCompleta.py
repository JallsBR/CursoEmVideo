# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

homemvelho = 0
idadevelho = 0
mulher20 = 0
somaidade = 0
for c in range(1,5):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = int(input(' Sexo:\n[1] - MASCULINO\n[2] - FEMININO\n[3] - OUTROS\nEscolha: '))
    somaidade += idade
    if sexo == 1:
        sexo = "M"
    if sexo == 2:
        sexo = "F"
    if sexo == "M" and idade>idadevelho:
        homemvelho = nome
        idadevelho = idade
    if sexo == "F" and idade<20:
       mulher20 = mulher20+1

print('A media de idade do grupo foi {}'.format(somaidade/4))
if homemvelho != 0:
    print('O Homem mais velho é {} com {} anos'.format(homemvelho,idadevelho))

print('Temos {} Mulheres abaixo de 20 anos'.format(mulher20))
