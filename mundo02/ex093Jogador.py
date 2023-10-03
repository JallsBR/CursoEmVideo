#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
lista_gols = []
jogador  = {}
jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
jogador['Partidas']= int(input('Quantas partidas foram jogadas: '))
jogador['Gols'] = lista_gols = []
gols_totais=0


for c in range(0,jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Quantos gols o {jogador["Nome"]} fez na partida {c+1}: ')))
    gols_totais += jogador['Gols'][c]
jogador['Total de gols'] = gols_totais
count = 0
print('- '*15)
print(jogador)
print('- '*15)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('- '*15)

print(f'O {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i,v in enumerate(jogador['Gols']):
    print(f'Na Partida {i+1}, {jogador["Nome"]} fez {v} gol(s)')
print(f'Um total de {jogador["Total de gols"]}')
print('- '*15)
