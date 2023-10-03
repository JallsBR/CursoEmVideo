#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip()
santo = (cidade[0:5]).capitalize()
print('Começa com Santo: {}'.format("Santo"in santo))



