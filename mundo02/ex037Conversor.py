# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.

print('\033[1:36m-=\033[m'*20)
print('Programa de Conversão' )
print('\033[1:36m-=\033[m'*20)
n = int(input('Digite um número inteiro: '))
conversor = int(input('Escolha a conversão: \033[1:36m1\033[m para binário, \033[1:36m2\033[m para octal e \033[1:36m3\033[m para hexadecimal. '))
binário = n%2




if conversor == 1:
    print('O número \033[1:36m{}\033[m convertido para Binário é \033[1:36m{}\033[m'.format(n, bin(n)[2:]))
elif conversor == 2:
    print('O número \033[1:36m{}\033[m convertido para Octal é \033[1:36m{}\033[m'.format(n, oct(n)[2:]))
elif conversor == 3:
    print('O número \033[1:36m{}\033[m convertido para Hexadecimal é \033[1:36m{}\033[m'.format(n, hex(n)[2:]))
else:
    print('Parametros inconsistentes. Operação não realizada')
