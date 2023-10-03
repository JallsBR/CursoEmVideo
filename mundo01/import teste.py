# Exercício Python 016: Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc, ceil
número = float(input('Digite um número real: '))

print('O número é {}, e a porção inteira é {}'.format(número, ceil(número)))
print('O número é {}, e a porção inteira é {:.0f}'.format(número, número))
print('O número é {}, e a porção inteira é {}'.format(número, trunc(número)))
print('O número é {}, e a porção inteira é {}'.format(número, int(número)))