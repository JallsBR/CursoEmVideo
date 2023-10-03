# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar
# apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(n):
    while True:
        if n.isnumeric():
            return n
            break
        else:
            print('Inválido')
            n = (input('Digite um número: '))


n = str(input('Digite um número: '))
print(leiaint(n))
