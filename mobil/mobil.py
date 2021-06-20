print('\n0. Avanza 2010', '\n1. Avanza Veloz', '\n2. Avanza G Matic 2010')
merk = ['Avanza 2010','Avanza Veloz','Avanza G Matic 2010']
x_int = int(input('\nPilih merk kendaraan: '))

# Database mobil
if merk[x_int] == ('Avanza 2010'):
    km = 8
elif merk[x_int] == ('Avanza Veloz'):
    km = 7
elif merk[x_int] == ('Avanza G Matic 2010'):
    km = 9
