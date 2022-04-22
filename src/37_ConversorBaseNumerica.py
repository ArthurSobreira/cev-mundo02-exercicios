num = int(input('Digite um Número inteiro:'))
print('''Escolha uma das bases para conversão
[ \033[32mBin\033[m ] Converter o número para \033[4mBinário\033[m
[ \033[32mOct\033[m ] Converter o número para \033[4mOctal\033[m
[ \033[32mHex\033[m ] Converter o número para \033[4mHexadecimal\033[m''')
opc = str(input('Sua Opção:')).strip().capitalize()
if opc == 'Bin':
    print(f'\033[32m{num}\033[m convertido para número Binário é \033[m\033[4m{bin(num)[2:]}\033[m')
elif opc == 'Oct':
    print(f'\033[32m{num}\033[m convertido para Octal é \033[m\033[4m{oct(num)[2:]}\033[m')
elif opc == 'Hex':
    print(f'\033[32m{num}\033[m convertido para Hexadecimal é \033[m\033[4m{hex(num)[2:]}\033[m')
else:
    print('\033[31;4mSelecione apenas uma das opções mostradas!!\033[m')
