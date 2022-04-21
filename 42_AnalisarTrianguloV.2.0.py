print('\033[97;1m=' * 24)
print('\033[7mAnalizador de Triângulos\033[m')
print('\033[97;1m=' * 24)
r1 = float(input('\033[1;97mDigite o comprimento da Primeira Reta:\033[m'))
r2 = float(input('\033[1;97mDigite o comprimento da Segunda Reta:\033[m'))
r3 = float(input('\033[1;97mDigite o comprimento da Terceira Reta:\033[m'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'\033[32;1mCom as medidas de lado {r1}, {r2} e {r3}, é POSSÍVEL formar um Triângulo\033[m.')
    if r1 == r2 == r3:
        print('O Triângulo é classificado como \033[33mEquilátero\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O Triângulo é classificado como \033[36mIsóceles\033[m')
    elif r1 != r2 != r3 != r1:
        print('O Triângulo é classificado como \033[35mEscaleno\033[m')
else:
    print(f'\033[31;1mÉ IMPOSSÍVEL formar um Triângulo com estas medidas\033[m')
