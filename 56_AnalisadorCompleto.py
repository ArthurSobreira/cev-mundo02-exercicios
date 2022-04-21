si = 0
medi = 0
mih = 0
nmv = 0
contm = 0
for p in range(1, 5):
    print(f'========== {p}ª Pessoa ========== ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    si += idade
    if p == 1 and sexo in 'Mm':
        mih = idade
        nmv = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        nmv = nome
    if sexo in 'Ff' and idade < 20:
        contm += 1

medi = si / 4
print(f'A Média de idade do grupo é de {medi}')
print('O Homem mais velho se chama {} e tem {} anos'.format(nmv, mih))
print(f'Ao todo são {contm} com menos de 20 anos')
