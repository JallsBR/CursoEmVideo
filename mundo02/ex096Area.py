# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def Área (a, b):
    s = a * b
    print(s)


altura = float(input('Digite a Altura(m):'))
comprimento = float(input('Digite o Comprimento(m):'))

Área(altura, comprimento)

