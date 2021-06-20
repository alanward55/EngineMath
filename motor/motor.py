print('\n0. Supra X 125','\n1. Revo 110', '\n2. Blade 123','\n3. Beat ESP', '\n4. Spacy PGM', '\n5. Scoopy ESP', '\n6. Vario 110', '\n7. Vario 125', '\n8. Vario 150', '\n9. Sonic 150', '\n10. Verza New', '\n11. Mega Pro New', '\n12. CB 150 New', '\n13. PCX 150')
merk = ['Supra X 125', "Revo 110", "Blade 123", 'Beat ESP', 'Spacy PGM', 'Scoopy ESP', 'Vario 110', 'Vario 125', 'Vario 150', 'Sonic 150', 'Verza New', 'Mega Pro New', 'CB 150 New', 'PCX 150']
x_int = int(input('\nPilih merk kendaraan: '))

# Database motor
if merk[x_int] == ('Supra X 125'):
    km = 61
elif merk[x_int] == ('Revo 110'):
    km = 62
elif merk[x_int] == ('Blade 123'):
    km = 62
elif merk[x_int] == ('Beat ESP'):
    km = 59
elif merk[x_int] == ('Spacy PGM'):
    km = 41
elif merk[x_int] == ('Scoopy ESP'):
    km = 62
elif merk[x_int] == ('Vario 110'):
    km = 59
elif merk[x_int] == ('Vario 125'):
    km = 60
elif merk[x_int] == ('Vario 150'):
    km = 53
elif merk[x_int] == ('Sonic 150'):
    km = 41
elif merk[x_int] == ('Verza New'):
    km = 48
elif merk[x_int] == ('Mega Pro New'):
    km = 46
elif merk[x_int] == ('CB 150 New'):
    km = 38
elif merk[x_int] == ('PCX 150'):
    km = 51