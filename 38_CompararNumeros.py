print('\033[97;1m=\033[m' * 30)
print(' ' * 3, '\033[34;1mComparador de Números\033[m')
print('\033[97;1m=\033[m' * 30)
n1 = int(input('\033[97;1mPrimeiro Número:\033[m'))
print('\033[97;1m=\033[m' * 30)
n2 = int(input('\033[97;1mSegundo Número:\033[m'))
print('\033[97;1m=\033[m' * 40)
if n1 > n2:
    print('\033[32;1mAnalizando os dois Números, o Primeiro Número é o MAIOR.\033[m')
elif n1 < n2:
    print('\033[32;1mAnalizando os dois Números, o Segundo Número é o MAIOR.\033[m')
else:
    print(f'\033[32;1mAnalizando os dois Números, {n1} é IGUAL a {n2}.\033[m')
print('\033[97;1m=\033[m' * 40)
