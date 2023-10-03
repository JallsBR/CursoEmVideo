#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# cada elemento subsequente é a soma dos dois anteriores



fibo = int(input('Quantos números na escala Fibonacci vc quer:'))
n1 = 0
n2 = 0
n3 = 0
n4 = 1
count = 0
while count<fibo:
    count += 1
    print(n3, end=' ')
    n1 = n2
    n2 = n3
    n3 = n4
    n4 = n2+n3
print('\nFIM')

