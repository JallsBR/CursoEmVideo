# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# Não pode ser divisível por 100. ...
# Pode ser que seja divisível por 400.
from datetime import date
ano = int(input('Digite o ano para saber se ele é Bissexto. Se quiser o ano atual, digite 0: '))
verbo = ano
anoatual = date.today().year
if verbo < anoatual:
        verbo = str('foi')
elif verbo == anoatual:
    verbo = str('é')
elif verbo > anoatual:
    verbo = str('será')

print('-'*25)
if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} {} Bissexto.'.format(ano, verbo))
else:
    print('O ano {} não {} Bissexto.'.format(ano, verbo))
print('-'*25)
