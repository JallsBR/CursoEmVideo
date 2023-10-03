# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('-=-=- Números Primos -=-=-')
n = int(input('Digite um número pra saber se ele é primo: '))
listadiv = []
listaocorrencia = []
divi = 0

for c in range (1,n+1):
    if n % c == 0:
        print(' \033[33m{}\033[m'.format(c), end='')
        listadiv.append((c))
        listaocorrencia.append('1')
    else:
        print(' \033[31m{}\033[m'.format(c), end='')
vezes = listaocorrencia.count('1')
print('\nO número {} é divisivel por {}'.format(n, str(listadiv)[1:-1].replace("'", '')))
print('Ele foi dividido {} vezes'.format(vezes), end='')
if vezes>3:
    print(' e não é PRIMO')
else:
    print(' e é PRIMO!!!')
