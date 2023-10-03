#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
posi1 = int(nome.find(' '))
posi2 = int(nome.rfind(' '))
nome1 = nome[:posi1]
nome2 = nome[posi2:]
#meu modo
print('Olá {}, o seu último nome é {}.'.format(nome1, nome2))

n = nome.split()
#modo Prof
print('Olá {}, o seu último nome é {}.'.format( (n[0]), (n[len(n)-1])))
