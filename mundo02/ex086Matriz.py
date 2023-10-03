#Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
temp = 0
a = b = 0
for c in range(0,9):
    temp = int(input(f'Digite um valor para [{a}],[{b}]:'))
    temp = (f'[{temp: ^6}]')
    matriz[a].insert(b, temp)
    b+=1
    if c == 2:
        a = 1
        b = 0
    if c == 5:
        a = 2
        b = 0
print('\n\n')
print(*matriz[0])
print(*matriz[1])
print(*matriz[2])