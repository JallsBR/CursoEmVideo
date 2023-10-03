#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome= str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('\n')
print('-'*10, 'Analizando Nome', '-'*17)
print('\n')
print(' '*5,'{} -  Maiúsculas'.format(nome.upper()))
print(' '*5,'{} - Minúsculas'.format(nome.lower()))
print(' '*5,'{} Letras no total'.format((len(nome)) - (nome.count(' '))))
print(' '*5,'{} é o seu primeiro nome'.format(lista[0]), 'com {} letras'.format(len(lista[0])))
print('\n')
print('-'*45)
