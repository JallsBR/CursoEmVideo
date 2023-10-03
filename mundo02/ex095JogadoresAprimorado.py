jogadores = []
while True:
    lista_gols = []
    jogador  = {}
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    jogador['Partidas']= int(input('Quantas partidas foram jogadas: '))
    jogador['Gols'] = lista_gols = []
    for c in range(0,jogador['Partidas']):
        jogador['Gols'].append(int(input(f'Quantos gols o {jogador["Nome"]} fez na partida {c+1}: ')))
        jogador['Total de gols'] = sum(jogador['Gols'])
    jogadores.append(jogador.copy())
    escolha = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    while escolha[0] != 'S' and escolha[0] != 'N':
        print('Escolha inválida')
        escolha = str(input('Quer Continuar [S/N]: ')).strip().upper()
    if "N" in escolha:
        break

print('- '*35)
print(jogadores)
print('- '*35)

for i in range(0, len(jogadores)):
    print('- '*35)
    print(f'O Jogador {jogadores[i]["Nome"]} tem o seguinte aproveitamento:')
    print(f'  ➪   Número de partidas: {jogadores[i]["Partidas"]}')
    print(f'  ➪   Um total de {jogadores[i]["Total de gols"]} gols')
    for c in range(0, len(jogadores[i]["Gols"])):
        print(f'     ➪      Na partida {c+1} marcou {jogadores[i]["Gols"][c]} gols')
while True:
    teste = False
    print('\n')
    escolha = str(input('Escolha um jogador para ver os dados novamente ou sair para encerrar')).strip().title()
    print('- ' * 35)
    c=0
    if escolha == 'Sair':
        break
    else:
        for i in range(0, len(jogadores)):
            if escolha == jogadores[i]["Nome"]:
                teste = True
                print(f'O Jogador {jogadores[i]["Nome"]} tem o seguinte aproveitamento:')
                print(f'   ➪   Número de partidas: {jogadores[i]["Partidas"]}')
                print(f'   ➪   Um total de {jogadores[i]["Total de gols"]} gols')
                for c in range(0, len(jogadores[i]["Gols"])):
                    print(f'     ➪      Na partida {i + 1} marcou {jogadores[i]["Gols"][c]} gols')
        c+=1
        if teste == False:
            print('Comando Inválido. Tente novamente:')


