#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import choice, shuffle, random
a1 = str(input('Digite o nome do Primeiro Aluno: '))
a2 = str(input('Digite o nome do Segundo Aluno: '))
a3 = str(input('Digite o nome do Terceiro Aluno: '))
a4 = str(input('Digite o nome do Quarto aluno: '))
lista1 = [a1, a2, a3, a4]
shuffle(lista1)
print("{}".format(lista1))
