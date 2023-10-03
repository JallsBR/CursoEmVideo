# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1:33m-\033[m'*35)
print('\033[1mPrograma Minha Casa, Minha Dívida\033[m')
print('\033[1:33m-\033[m'*35)
casa = float(input('Qual o \033[33mvalor\033[m da casa a ser financiada? R$'))
salário = float(input('Qual a \033[33mrenda mensal\033[m da família? R$'))
ano = int(input('Quantos \033[33manos\033[m de fianciamento?'))
prestação = casa / (12 * ano)
if (salário*0.3)>= prestação:
    print('A prestação de \033[1:33mR${:.2f}\033[m em \033[1:33m{}anos\033[m é possível! Parabéns! Você contraiu uma dívida de \033[1:33mR${:.2f}\033[m'.format(prestação, ano, casa))
else:
    print('A prestação de \033[1:33mR${:.2f}\033[m em \033[1:33m{}anos\033[m \033[1:31mNÂO\033[m é possível!' .format(prestação, ano ))

