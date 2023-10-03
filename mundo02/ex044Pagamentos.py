#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('-'*40)
print(f'{" SISTEMA DE PAGAMENTOS ":=^40}')
print('-'*40)
preço = float(input('Qual o valor do produto? R$ '))
print('Qual a condição de pagamento:\n 1 -  à vista dinheiro/cheque\n 2 - à vista no cartão\n 3 - em até 2x no cartão\n 4 - 3x ou mais no cartão ')
metododepagamento = int(input('OPÇÃO: '))
print('-'*40)
if metododepagamento == 1:
    preço = preço - (preço*0.1)
    print('10% de desconto')
elif  metododepagamento == 2:
    preço = preço - (preço*0.05)
    print('5% de desconto')
elif metododepagamento == 3:
    print('Preço sem desconto')
    print('2x parcelas de R${:.2F} SEM JUROS'.format(preço / 2))
elif metododepagamento == 4:
    preço = preço + (preço*0.2)
    parcelas = int(input('Quantas parcelas? '))
    print('20% de acrécimo')
    print('{}x parcelas de R${:.2F} COM JUROS'.format(parcelas, preço / parcelas))
print('O valor a pagar é R${:.2f}'.format(preço))
