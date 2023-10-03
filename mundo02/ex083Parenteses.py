#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

expressão = str(input('Digite uma expressão numérica: '))
lista = expressão.split()
abetos = expressão.count('(')
fechados = expressão.count(')')

if abetos == fechados:
    print('A expressão está correta')
else:
    print('A expressão é inválida')
