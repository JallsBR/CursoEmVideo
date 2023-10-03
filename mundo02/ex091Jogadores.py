#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
maior = 0
print('-'*35)
sleep(1)
jogo['Jogador1']= int(randint(1, 20))
print(f'Jogagor 01 jogou o d20 e tirou {jogo["Jogador1"]}')
jogo['Jogador2']= int(randint(1, 20))

sleep(1)
print(f'Jogagor 02 jogou o d20 e tirou {jogo["Jogador2"]}')


sleep(1)
jogo['Jogador3']= int(randint(1, 20))
print(f'Jogagor 03 jogou o d20 e tirou {jogo["Jogador3"]}')

sleep(1)
jogo['Jogador4']= int(randint(1, 20))
print(f'Jogagor 04 jogou o d20 e tirou {jogo["Jogador4"]}')
sleep(1)
print('-'*35)
print('      Ranking')
print('-'*35)
sorted(jogo.values())
raking = {}
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
lugar = 1
for i,v in enumerate(raking):
    print(f'O {lugar}° é {v[0]} com {v[1]} no dado!')
    lugar +=1

