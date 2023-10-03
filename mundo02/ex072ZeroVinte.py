zerovinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete',
             'oito', 'nove', 'dez', 'onze','doze', 'treze', 'catorze', 'quinze',
             'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero entre 0 e 20:'))
while True:
    if 0<= n<= 20:
        break
    n = int(input('Digite um numero entre 0 e 20:'))
print(zerovinte[n])
