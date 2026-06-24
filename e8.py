m = input('Quantos m² serão pintados? ')

while True:
    y = str.casefold(input(f'{m}m² está correto? (Y/N) '))
    if y == 'n':
        input('Quantos m² serão pintados? ')
    elif y == 'y':
        break
    else:
        print('Y/N? ')

#3m = 1l = 18 = 80

import math

lits = math.ceil(float(m)/3)
lats = math.ceil(lits/18)
din = math.ceil((lats*80))

data = [ 
    ['Latas necessárias (unidades)', lats, 'lata(s)'],
    ['Valor total (R$)', din, 'reais'],
]

from tabulate import tabulate

print(tabulate(data, headers=['Lista', 'Quantidades', 'Tipo(s)'], 
               colalign= ('left', 'left')))

