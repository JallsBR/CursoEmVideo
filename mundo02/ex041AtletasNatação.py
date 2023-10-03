#A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
import datetime
date = datetime.date.today()
anoatual= date.strftime("%Y")
print('\033[1:33m-\033[m'*40)
print('\033[1:34mConfederação Nacional de Natação\033[m')
print('\033[1:33m-\033[m'*40)
nome = str(input('Digite o nome do Atleta: ')).strip()
ano = int(input('Digite o ano de Nascimento:'))
idade = int(anoatual) - ano
if idade<=9:
    print('{} tem {} anos e está na categoria Mirim'.format(nome.title(), idade))
elif idade > 9 and idade <= 14:
    print('{} tem {} anos e está na categoria Infantil'.format(nome.title(), idade))
elif idade >14 and idade <= 19:
    print('{} tem {} anos e está na categoria Júnior'.format(nome.title(), idade))
elif idade >=20 and idade <=25:
    print('{} tem {} anos e está na categoria Sênior'.format(nome.title(), idade))
elif idade >=26:
    print('{} tem {} anos e está na categoria Master'.format(nome.title(), idade))
else:
    print('ERROR')

