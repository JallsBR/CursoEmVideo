print('Programa de análide se triângulo')
print('\033[36m-\033[m'*25)
lado1 = float(input('A medida do lado 1 é:'))
lado2 = float(input('A medida do lado 2 é:'))
lado3 = float(input('A medida do lado 3 é:'))

if lado1+lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2:
    print('\033[1:32mÉ possível montar um triângulo com esses valores.\033[m')
else:
    print('\033[1:31mNão é possível montar um triângulo com esses valores.')
