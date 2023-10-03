# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

distancia = float(input('Qual a distância percorrida? '))
diarias = int(input('Por quantos dias foi alugado? '))
valor = (diarias*60)+(distancia*0.15)

print('\n','-'*30, '\n','O valor da locação é R$ {}'.format(valor),'\n','-'*30)
