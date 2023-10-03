c = str(input('Informe seu sexo: (M/F/OUTRO): ')).strip().upper()
while c!='M' and c!='F' and c!='OUTRO':
    c = str(input('Dado inválido. Informe seu sexo: (M/F): ')).strip().upper()
print('Dado cadastrado com sucesso')
