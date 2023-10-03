#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna3 = maior2 = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite um numero para [{c}],[{l}]: '))

for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]: ^6}]', end='')
    print()
print('\n')
for c in range(0,3):
    for l in range(0,3):
        if matriz[c][l] % 2 == 0:
            soma = soma + matriz[c][l]
print(f'Soma dos valores pares: {soma}')


for c in range(0, 3):
    coluna3 = coluna3 + matriz[c][2]
print(f'A soma dos itens da coluna 3 é {coluna3}')


for c in range(0, 3):
    if maior2 < matriz[1][c]:
        maior2 = matriz[1][c]
print(f'O maior valor da linha 2 é {maior2}')
print('\n')