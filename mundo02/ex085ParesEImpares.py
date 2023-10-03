listatotal = [[], []]
c=1
while c!=7:
    temp = int(input(f'Número {c}: '))
    c+=1
    if temp % 2 == 0:
        listatotal[0].insert(0, temp)
    else:
        listatotal[1].insert(0, temp)

listatotal[0].sort()
listatotal[1].sort()
print(listatotal)
