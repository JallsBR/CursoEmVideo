#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
print('\033[1:33m-\033[m'*40)
print('\033[1:30:42mEscola Santa Helena - Situação do Aluno\033[m')
print('\033[1:33m-\033[m'*40)
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = float(nota1 + nota2)/2
print('\033[1:33m-\033[m'*55)
print('O(a) aluno(a) \033[1:33m{}\033[m teve a média de \033[1:33m{:.2f}\033[m.'.format(nome, media))
if media >= 7:
    print('{} está \033[1:32mAprovado!'.format(nome))
elif media < 7 and media >= 5:
    print('{} está de \033[1:33mRecuperação'.format(nome))
elif media < 5:
    print('{} está \033[1:31mReprovado!'.format(nome))
