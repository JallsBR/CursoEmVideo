#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

print('\033[1:36m-'*45)
print('\033[1:33mCalculadora de Índice de Massa Corpórea')
print('\033[1:36m-\033[m'*45)
peso = float(input('Qual o seu Peso? '))
altura = float(input('Qual a sua Altura? '))
imc = peso / (altura*altura)
print('\033[1:36m-\033[m'*45)
print('\033[Seu imc atual é {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1:33mSituação: Abaixo do Peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1:30mSituação: Peso Ideal\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1:33mSituação: Sobrepeso\033[m')
elif imc >= 30 and imc < 400:
    print('\033[1:31mSituação: Obesidade\033[m')
elif imc >= 40 :
    print('\033[1:30:41mSituação: Obesidade Mórbida\033[m')


