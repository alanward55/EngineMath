print('\n0. Premium', '\n1. Pertalite', '\n2. Pertamax', '\n3. Solar')
bbm = ['premium','pertalite', 'pertamax', 'solar', ]
b = int(input('\nPilih jenis bahan bakar: '))

# Database bbm
if b == ('premium'):
    print('premium')
elif b == ('pertalite'):
    print ('pertalite')
elif b == ('pertamax'):
    print ('pertamax')
elif b == ('solar'):
    print ('solar')
