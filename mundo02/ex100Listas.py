#Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
def Sorteia():
    lista = [randint(0,100), randint(0,100), randint(0,100), randint(0,100),randint(0,100)]
    return lista


def Soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 ==0:
            soma += n
    return soma

sorteio = Sorteia()
resultado = Soma_par(sorteio)

print(sorteio)
print(resultado)