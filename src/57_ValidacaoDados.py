s = 1
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('Sexo Incoerente!!')
print('Fim')