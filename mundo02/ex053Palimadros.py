#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('DETECTORDE PALINDROMO')

frase = str(input('Digite a frase: ').strip())
frase = frase.replace(' ', '').lower()
carateres = int(len(frase))
contrario = "a"

print('Temos {} caracteres'.format(carateres))

for c in range(1, carateres+1):
    v = (frase[-c])
    contrario = contrario + v
contrario = contrario[1:]

if frase == contrario:
    print('É um Palíndromo')
else:
    print('Não é Um Palímadro')
