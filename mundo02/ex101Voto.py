#Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições
import datetime

date = datetime.date.today()
anoatual = date.strftime("%Y")

def Voto(ano):

    idade= anoatual = int(date.strftime("%Y")) - ano
    situação = ''
    if idade< 16:
        situação = 'Voto Indisponível'
    if (idade > 16 and idade < 18) or (idade > 65):
        situação = 'Voto Opcional'
    if idade > 18 and idade <65:
        situação = 'Voto Obrigatório'
    return situação



pessoa = (int(input('Em que ano a pessoa nasceu: ')))
print(f'A pessoa tem {int(date.strftime("%Y")) - pessoa} e a situação é de {Voto(pessoa)}')