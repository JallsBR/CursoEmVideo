# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

n = 0
l = []
for c in range (1, 7):
    número = int(input('Digite um número: '))
    l.append(número)
    if número % 2 == 0:
        n += número
print('Os números foram {}'.format(str(l)[1:-1]))
print('A soma dos pares é de {}'.format(n))
