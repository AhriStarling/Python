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

print(f'Salário bruto: R${(float(s)*float(n))*20}')

brut = ((float(s)*float(n))*20)
ir = ((11/100)*brut) 
inss = ((8/100)*brut)
sind = ((5/100)*brut)
liqui = float(brut-(ir + inss + sind))

from tabulate import tabulate

info =[
    ['Salário bruto', brut],
    ['IR(11%)', -ir],
    ['INSS(8%)', -inss],
    ['Sindicato(5%)', -sind],
    ['Salário liquído', liqui],
]

print(tabulate(info, headers=['Valores', 'R$'], floatfmt='.2f', tablefmt='simple'))
