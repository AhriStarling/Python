s = input('R$/h? ')

#str.casefold = to ignore case diff

while True:
    c = str.casefold(input(f'O valor {s} está correto? (Y/N) '))
    if c == 'n':
        s = input('R$/h? ')
    elif c == 'y':
        break
    else:
        print('Y/N? ')

n = input('Quantas horas diárias? ')

while True:
    z = str.casefold(input(f'{n} hora(s) está correto? (Y/N) '))
    if z == 'n':
        n = input('Quantas horas diárias? ')
    elif z == 'y':
        break
    else:
        print('Y/N? ')

print(f'Salário mensal: R${(float(s)*float(n))*20}')
