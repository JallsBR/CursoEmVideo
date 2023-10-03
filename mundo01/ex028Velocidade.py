#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
print('\n')
print('-'*30)
vel = int(input('Velocidade do veículo: '))
print('\n')
print('-'*30)
multa = float((vel-80)*7.00)
if vel >= 80:
    print('Acima do limite de velocidade. \nA sua velocidade é {}Km/h em uma pista de 80Km/h. \nMulta de R${:.2f}'.format(vel, multa))
else:
    print('{}km/h Velocidade permitida.'.format(vel))
print('\n')
print('-'*30)
