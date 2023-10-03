#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

p = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
		 'programador', 'futuro')
for c in p:
    print(f'Na palavra {c} temos', end='')
    if 'a' in c:
        print(' a', end='')
    if 'e' in c:
        print(' e', end='')
    if 'i' in c:
        print(' i', end='')
    if 'o' in c:
        print(' o', end='')
    if 'u' in c:
        print(' u', end='')
    print('')

print('-'*45)

for c in p:
    print(f'Na palavra {c.upper()} temos as vogais ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end='  ')
    print('')
