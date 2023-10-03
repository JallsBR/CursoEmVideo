#Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols = 0):
    if nome == '':
        nome = 'Desconhecido'
    if gols == '' or gols not in '1234567890':
        gols = 0
    print(f'O Jogador {nome} fez {gols} gols ')


jogador = str(input('Digite o nome do  jogador:').strip().title())
gols = (input('Quantos gols: '))
ficha(jogador, gols)