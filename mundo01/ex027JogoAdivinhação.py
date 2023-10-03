import random
import time
n = random.randint(1,5)
print('Estou pensnado em um número entre 1 e 5...você consegue acertar?')
n2 = int(input('Em que número estou pensando? '))
print('Processando...')
time.sleep(4)
if n == n2:
    print('Acertou miserávi!!!')
else:
    print('Perdeu,prayboy! Era no {}'.format(n))

