c = 1
tot_G = 0
cont_m1000 = 0
nom_prodB = 0
pre_prodB = 0
while True:
    print('')
    print('=' * 28)
    print(' ' * 7, f'{c}ª PRODUTO')
    print('=' * 28)
    nom = str(input('Nome do Produto: ')).title()
    pre = int(input('Preço do Produto: R$'))
    while True:
        cont = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SN':
            break
    if pre > 1000:
        cont_m1000 += 1
    if c == 1:
        nom_prodB = nom
        pre_prodB = pre
    if pre < pre_prodB:
        nom_prodB = nom
        pre_prodB = pre
    c += 1
    tot_G += pre
    if cont == 'N':
        break
print(f'''O total gasto na compra é de R${tot_G:.2f}
{cont_m1000} Produtos custam mais de R$1000.OO
{nom_prodB} é o produto mais barato, custando R${pre_prodB:.2f}''')
