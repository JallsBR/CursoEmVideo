#Exercício Python 034: Escreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual o valor do salário atual do funcionário:'))
if salário <= 1250:
    salário = salário + salário*0.15
else:
    salário = salário + salário*0.10

print('Com o aumento, o salário agora é R${:.2f}'.format(salário))
