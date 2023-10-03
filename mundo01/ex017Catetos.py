#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, hypot
cateto1 = float(input('Digite o valor do prieiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto:' ))
quadhipo = (cateto1**2) + (cateto2**2)
hipotenusa = sqrt(quadhipo)
# Com raiz quadrada
print('- '*10)
print("A hipotenusa é {:.2f}".format(hipotenusa))
print('- '*10)

# Com hipotenusa automatica
print('- '*10)
print("A hipotenusa é {:.2f}".format(hypot(cateto1, cateto2)))
print('- '*10)