#Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
media = int(input('Digite a média do aluno: '))
if media>7:
    situação = 'Aprovado'
else:
    situação = 'Reprovado'
aluno = {'Nome': nome, 'Media': media, 'Situação': situação}
print('-'*30)
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')