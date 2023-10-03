#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
print('- '*25)
print('Cadastro de pessoas')
print('- '*25)
count = 0
listapessoas = []
media = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo[0] != 'M' and sexo !='F':
        print('Sexo inválido')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    media+=idade
    pessoa = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    listapessoas.append(pessoa.copy())
    escolha = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    while escolha[0] != 'S' and escolha[0] !='N':
        print('Escolha inválida')
        escolha = str(input('Quer Continuar [S/N]: ')).strip().upper()
    count += 1
    if "N" in escolha:
        break
print('- '*25)
print(listapessoas)
print('- '*25)
print(f'Foram {len(listapessoas)} pessoas cadastradas')

media = media/len(listapessoas)
print(f'A média de idade do grupo é de {media:.0f} anos')
print('- '*25)
mulheres = []
for i in range (0, int(len(listapessoas))):
    if 'F' in listapessoas[i]['Sexo']:
        mulheres.append(listapessoas[i]['Nome'])
print(f'A lista de mulheres é {mulheres}')
print('- '*25)
maioresidades = []
for i in range (0, int(len(listapessoas))):
    if media < listapessoas[i]['Idade']:
        maioresidades.append(listapessoas[i]['Nome'])
print(f'As pessoas com idade acima da média são: {maioresidades}')
print('- '*25)
