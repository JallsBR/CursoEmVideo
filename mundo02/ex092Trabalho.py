#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ano_atual=datetime.now().year

trabalhador = {}

trabalhador['Nome']= str(input('Nome: ')).strip().title()
trabalhador['Ano de Nascimento'] = int(input('Ano de Nasciemento: '))
trabalhador['Idade'] = ano_atual - trabalhador['Ano de Nascimento']
del trabalhador['Ano de Nascimento']
trabalhador['CTPS'] = int(input('Digite o numero da carteira de trabalho: [0 em caso de não possuir]'))

if trabalhador['CTPS'] == 0:
    del trabalhador['CTPS']
else:
    trabalhador['Contrato inicial'] = int(input('Ano em que começou a trabalhar: '))
    trabalhador['Salário'] = 'R$ ' + (input('Salário: '))
    trabalhador['Aposentadoria'] = trabalhador['Contrato inicial'] + 35
print('◉'*30)
for k,v in trabalhador.items():
    print(f'{k} é igual a {v}')
print('◉'*30)
