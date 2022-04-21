print('\033[97;1m=\033[m' * 28)
print('\033[7;1mSelecione o Preço do Produto\033[m')
print('\033[97;1m=\033[m' * 28)
pre = float(input('\033[97;4mPreço\033[m: R$'))
print('\033[97;1m=\033[m' * 31)
print('\033[7;1mSelecione o Método de Pagamento\033[m')
print('\033[97;1m=\033[m' * 31)
print('''
[ \033[32m1\033[m ] À vista Dinheiro/Cheque (10% off)
[ \033[32m2\033[m ] À vista Cartão de Crédito (5% off)
[ \033[32m3\033[m ] Em até 2x no Cartão de Crédito
[ \033[32m4\033[m ] 3x ou mais no Cartão de Crédito (20% de Juros)
''')
met = int(input('\033[32;4mMétodo Escolhido\033[m:'))
print(' ' * 20)
if met == 1:
    off = pre - (pre * 0.10)
    print(f'O Valor a ser pago escolhendo o Método 1 é de \033[31mR$ {off:.2f}\033[m')
elif met == 2:
    off = pre - (pre * 0.05)
    print(f'O Valor a ser pago escolhendo o Método 2 é de \033[31mR$ {off:.2f}\033[m')
elif met == 3:
    parc = pre / 2
    print(f'''Sua compra será parcelada em 2x de \033[31mR$ {parc:.2f}\033[m 
O Valor não se altera escolhendo o Método 3''')
elif met == 4:
    parc = int(input('\033[32;4mEm quantas Parcelas?\033[m:'))
    print(' ' * 20)
    total = pre + (pre * 0.20)
    parct = total / parc
    print(f'''Sua compra será parcelada em {parc}x de \033[31mR$ {parct:.2f}\033[m
O Valor a ser pago no total, será de \033[31mR$ {total:.2f}\033[m''')
else:
    print('\033[31mOpção INCORRETA\033[m')
