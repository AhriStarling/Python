p = input('Insert m² to paint -> ')

while True:
    s = str.casefold(input(f'Are the {p}² correct? (Y/N) '))
    if s == 'n':
        p = input('Insert square meters to paint -> ')
    elif s == 'y':
        break
    else:
        print('Choose Y or N!')

import math

liter = float(p)/6
cans = liter/18
p_cans = cans*80

galon = liter/3.6
p_galon = galon*25

cans_mix = ((liter+((10/100)*liter)))/18
galon_mix = (liter - liter)
p_cans_galon = cans_mix*80 + galon_mix*25

tab = [
    ['Latas', math.ceil(cans), 'un', f'{p_cans:.1f}', 'reais' ],
    ['Galões', math.ceil(galon), 'un', f'{p_galon:.1f}', 'reais' ],
    ['Latas e galões', f'{math.ceil(cans_mix)}+{math.ceil(galon_mix)}', 
     'un', f'{p_cans_galon:.1f}', 'reais' ],
]

from tabulate import tabulate

print(tabulate(tab, headers= ['List', 'Quantities', 'Type', 'Price', 
                              '$ type'],  colalign=['left', 'right', 
                                                    'left', 'left', 'left']))