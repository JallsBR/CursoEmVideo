#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
c=1

while c<=5:
    lista.append(int(input(f'Digite o {c} número:')))
    c += 1

print(f'A Lista de números digitados foi {lista}, e na ordem correta fica {sorted(lista)}')
print(f'O Maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O Menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
