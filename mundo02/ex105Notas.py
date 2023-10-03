#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*num, situação = False):
    """
        A função notas serve para analisar uma turma
        para *num: recebe várias notas
        para situação: indica se deve receber a informação da situação da turma ou não
        Return: Dicionario com o total de notas, a maior e menor nota, e a media. caso a situação esteja habilitada, mostra tambem essa informação

    """
    maior = max(num)
    menor = min(num)
    contador = len(num)
    media = (sum(num)/contador)
    aluno = {'total':contador, 'maior_nota': maior, 'menor_nota': menor, 'media': media }
    if situação:
        if media <= 4:
            aluno['situação']='ruim'
        if 4 < media < 7:
            aluno['situação']='razoável'
        if media >= 7:
            aluno['situação']='boa'
        if media >= 9:
            aluno['situação']='excelente'
    return aluno

print(notas(6, 7, 9, situação= True ))
help(notas)
