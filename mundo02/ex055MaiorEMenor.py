# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []
maior = 0
menor = 0
print('\n\n')
for c in range(1,6):
    pesopessoa = float(input('Digite o peso da pessoa 0{}:'.format(c)))
    peso.append(pesopessoa)
    if c==1:
        maior = pesopessoa
        menor = pesopessoa
    if pesopessoa>maior:
        maior = pesopessoa
    if pesopessoa<menor:
        menor = pesopessoa

print('\nO MAIOR peso foi {:.1f}kg e o MENOR foi {:.1f}kg'.format(maior, menor))