#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

print('Programa de análide se triângulo')
print('\033[36m-\033[m'*55)
lado1 = float(input('A medida do lado 1 é:'))
lado2 = float(input('A medida do lado 2 é:'))
lado3 = float(input('A medida do lado 3 é:'))

if lado1+lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2:
    print('\033[1:32mÉ possível montar um triângulo com esses valores.\033[m')
else:
    print('\033[1:31mNão é possível montar um triângulo com esses valores.')

print('\033[36m-\033[m'*55)
print('Tipo do Triangulo:')

if lado1+lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2:
    # Teste equilátero
    if lado1 ==lado2 == lado3:
        print('\033[1:32mEste triângulo é Equilátero!')
    # Teste Escaleno
    elif lado1 != lado2 != lado3 != lado1:
        print('\033[1:32mEste triângulo é Escaleno')
    # Teste Isóceles (por eliminação)
    else:
        print('\033[1:32mEsse triangulo é Isóceles')
else:
    print('\033[1:31mIsso não é um Triângulo!')
print('\033[36m-\033[m'*55)
