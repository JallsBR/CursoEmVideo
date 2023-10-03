# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
date = datetime.date.today()
anoatual= date.strftime("%Y")
print('\033[1:32m-'*57)
print('\033[1:33mPrograma de Alistamento Militar Brasileiro :', date)
print('\033[1:32m-'*57, '\033[m')
ano = int(input('Digite seu ano de Nascimento:'))
idade = int(anoatual) - ano

if idade < 17:
    print('Você ainda não pode se alistar, tem apenas {} anos. tente denovo em {} anos'.format(idade, 18 - idade))
elif idade == 17:
    print('Você ainda não pode se alistar, tem apenas {} anos. tente denovo em {} ano'.format(idade, 18 - idade))
elif idade == 18:
    print('Você tem {} anos, idade do alistamento obrigatório!'.format(idade))
elif idade ==19:
    print('Você tem {} anos, idade do alistamento obrgatório passou a {} ano!'.format(idade, idade-18))
elif idade >=20:
    print('Você tem {} anos, idade do alistamento obrgatório passou a {} anos!'.format(idade, idade-18))
else:
    print('Algo errado com o ano que vc digitou.')