#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('{:-^40}'.format(' Cadasto de produtos '))
total = mais1000 = preçomaisbarato = 0
maisbarato = ''
while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    valor = float(input('Digite o valor do produto: '))
    total += valor
    if valor >1000:
        mais1000 += 1
    if maisbarato == '':
        maisbarato = produto
        preçomaisbarato = valor
    if preçomaisbarato > valor:
        maisbarato = produto
        preçomaisbarato = valor
    escolha = str(input('Quer continuar cadastrando produtos [S/N: ')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar cadastrando produtos [S/N: ')).strip().upper()[0]
    if escolha == "N":
        break
    print('='*25)
print('{:-^40}'.format(' Fim do Programa'))
print(f'\nO total de compras é R${total:.2f} \nTemos {mais1000} produto(s) com valores maiores que R$ 1000.00. \nO produto mais batrato foi {maisbarato}, com no valor de R${preçomaisbarato:.2f} ')