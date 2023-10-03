#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista = []
impares = []
pares = []
c=1
while True:
    x = (int(input(f'Digite o {c} número:')))
    lista.append(x)
    if x%2==0:
        pares.append(x)
    else:
        impares.append(x)
    escolha = (str(input('Quer continuar [S/N]: ').strip().upper()))
    if escolha == 'N':
        break
print(f'A lista de números digitados é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
