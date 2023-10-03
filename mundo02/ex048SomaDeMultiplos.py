# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.


print(f'{" Soma de mútiplos de 3 impares no intervalo ":=^70}')

range1 = int(input('range 1 '))
range2 = int(input('range 2 '))

soma = 0
n = 0
for c in range (range1, range2+1):
    if c%3 == 0 and c%2 !=0:
        print(c, end=' ')
        soma = soma + c
        n = n+1
   #if c%3 == 0:
print('\n \nA soma dos {} números é {}'.format(n, soma))
