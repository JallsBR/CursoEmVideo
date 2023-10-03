#Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
c=1
while True:
    x = (int(input(f'Digite o {c} número:')))
    if x in lista:
        print('O número ja está na lista.')
    else:
        lista.append(x)
        c+=1
    escolha = (str(input('Quer continuar [S/N]: ').strip().upper()))
    if escolha == 'N':
        break

print(f' Os valores digitados foram {sorted(lista)}')
