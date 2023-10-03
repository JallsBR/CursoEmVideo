while True:
    print('\033[0:30:47m-\033[m'*60)
    escolha = str(input('Função ou biblioteca: [stop para parar]:').strip().lower())
    if escolha == 'stop':
        break
    else:
        help(escolha)
