listapeso = list()
pessoa = list()
maiorpeso = list()
pessoamaiorpeso= list()
menorpeso= list()
pessoamenorpeso= list()
c=0
while True:
    nome = str(input('Digite um nome: ').strip().capitalize())
    peso = float(input('Digite o peso: '))
    c+=1
    pessoa.append(nome)
    listapeso.append(nome)
    listapeso.append(peso)
    if c==1:
        maiorpeso.append(peso)
        pessoamaiorpeso.append(nome)
        menorpeso.append(peso)
        pessoamenorpeso.append(nome)
    elif peso > maiorpeso[0]:
        maiorpeso.clear()
        pessoamaiorpeso.clear()
        maiorpeso.append(peso)
        pessoamaiorpeso.append(nome)
    elif peso == maiorpeso[0]:
        pessoamaiorpeso.append(nome)
    elif peso < menorpeso[0]:
        menorpeso.clear()
        pessoamenorpeso.clear()
        menorpeso.append(peso)
        pessoamenorpeso.append(nome)
    elif peso == menorpeso[0]:
        pessoamenorpeso.append(nome)
    escolha = str(input('Quer Continuar [S/N]: ').strip().upper())
    if 'N' in escolha:
        break

print(f'o maior peso registrado na lista foi {maiorpeso}kg, de {pessoamaiorpeso}')
print(f'o menor peso registrado na lista foi {menorpeso}kg, de {pessoamenorpeso}')
print(f'A lista de todas as pessoas é: {pessoa}')
print(f'A lista de todos com seus respectivos pesos é: {listapeso}')
