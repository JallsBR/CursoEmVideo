#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1, n2, n3, n4)
pares = 0

print(f'Você digitou os valore {tupla}')
print(f'O número 9 apareceu: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3)}')
print(f'Os valore(s) par(es) e´/são: ', end='')
for c in tupla:
    if c%2==0:
        print(c, ' ', end='' )
print('')
