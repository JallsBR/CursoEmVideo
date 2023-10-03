def Print(txt):
    comp = len(txt)
    print('~' * (12+comp))
    print(' ' * 5, txt, ' ' * 5)
    print('~' * (12+comp))

Print(str(input('Digite um texto').strip().capitalize()))

