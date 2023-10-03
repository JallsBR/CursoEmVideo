#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listaaluno = []
listatemp= []
c=0
while True:
    aluno = (str(input(f'Digite o Nome do aluno {c}: ').strip().capitalize()))
    nota1 = int(input(('Digite a Nota 1: ')))
    nota2 = int(input(('Digite a Nota 2: ')))
    listatemp.append(aluno)
    listatemp.append(nota1)
    listatemp.append(nota2)
    listaaluno.append(listatemp[:])
    listatemp.clear()
    c+=1
    escolha = str(input('Quer continuar [S/N]: ').strip())
    if escolha in 'Nn':
        break
print('-'*20)
print('     Boletim')
print('-'*20)
print(f'{"Número": <7}    {"Nome": <15} {"Média": >4}')
for c in range(0,len(listaaluno)):
    print(f'{c: <5}      {listaaluno[c][0]: <15} {(listaaluno[c][1]+listaaluno[c][2])/2: >4}')
print('\n')
while True:
    aluno = int(input('Escolha o número do aluno para ver suas notas: '))
    if aluno > len(listaaluno):
        print('Aluno Inválido')
    else:
        print(f'As notas do Aluno {listaaluno[aluno][0]}, são {listaaluno[aluno][1]} e {listaaluno[aluno][2]} ')
    escolha = str(input('Quer continuar [S/N]: ').strip())
    if escolha in 'Nn':
        break


