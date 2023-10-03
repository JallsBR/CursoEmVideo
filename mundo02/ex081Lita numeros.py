#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
c=1
while True:
    x = (int(input(f'Digite o {c} número:')))
    lista.append(x)
    escolha = (str(input('Quer continuar [S/N]: ').strip().upper()))
    if escolha == 'N':
        break
listainvert = sorted(lista, reverse=True)

print(f'foram digitados {len(lista)} números' )

print(f'A lista ordenada é {listainvert}')
if 5 in lista  :
    print('O valor 5 está presenta na lista')
else:
    print('O valor 5 não estápresente na lista')
