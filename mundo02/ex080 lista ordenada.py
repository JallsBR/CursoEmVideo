#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
c=1
d=0
for c in range(0, 5):
    n =  (int(input(f'Digite o {c+1} número:')))
    if len(lista) == 0 or n > max(lista):
        lista.append(n)
    elif n < min(lista):
        lista.insert(0, n)
    elif n in lista:
        lista.insert(lista.index(n), n)
    else:
        while True:
            if lista[d]<n<lista[d+1]:
                lista.insert(d+1, n)
                break
            d+=1


print(lista)
for c in range(0, 5):
    print(f'Número {lista[c]} na posição {c}')

