c = 1
cont_m18 = 0
cont_Masc = 0
cont_Fem20 = 0
while True:
    print('')
    print('=' * 28)
    print(f'     CADASTRO {c}ª PESSOA     ')
    print('=' * 28)
    ida = int(input('Idade: '))
    while True:
        sex = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sex in 'MF':
            break
    print('=' * 28)
    while True:
        resp = str(input('Deseja Continuar?: [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    c += 1
    if ida > 18:
        cont_m18 += 1
    if sex == 'M':
        cont_Masc += 1
    if sex == 'F' and ida < 20:
        cont_Fem20 += 1
    if resp == 'N':
        break
print('=' * 29)
print(f'      FIM DO PROGRAMA     ')
print('=' * 29)
print(f'''Dos cadastrados, {cont_m18} possuem mais de 18 anos.
Dos cadastrados, {cont_Masc} são Homens.
Dos cadastrados, {cont_Fem20} Mulheres tem(têm) menos de 20 anos''')
