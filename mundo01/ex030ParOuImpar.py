#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
print('{} É Par'if n%2==0 else "{} É impar".format(n, n))
