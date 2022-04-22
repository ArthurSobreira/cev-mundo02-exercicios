from random import randint

print('\033[97;1m=\033[m' * 66)
print('\033[1;7m', ' ' * 10, 'O COMPUTADOR PENSOU EM UM NÚMERO DE 1 A 10', ' ' * 10, '\033[m')
print('\033[97;1m=\033[m' * 66)
numsort = randint(1, 10)
num = int(input('Digite sua escolha: '))
n = 0
cont = 0
if num > numsort:
    while num != numsort:
        print('Opção Errada, Tente Um Pouco Menos!!')
        num = int(input('Digite sua escolha: '))
        cont += 1
if num < numsort:
    while num != numsort:
        print('Opção Errada, Tente Um Pouco Mais!!')
        num = int(input('Digite sua escolha: '))
        cont += 1
if num == numsort:
    print(f'Você acertou em {cont + 1} tentativas, o computador pensou em {numsort}')
