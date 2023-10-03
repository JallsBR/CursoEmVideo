#Exercício Python 026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.

frase1 = str(input('Digite uma frase: ')).strip()
frase = frase1.upper()
aproc = frase.count("A")
listafrase = frase.split()

print('Quantasvezes aparece a letra A: {}'.format(aproc))
print('A primeira vez que o A aparece é na posição: {}'.format(frase.find("A")+1))
print('A ultima vez que o A aparece é na posição: {}'.format(frase.rfind("A")+1))

