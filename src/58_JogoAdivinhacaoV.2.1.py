from random import randint

cont = 0
print('\033[97;1m=\033[m' * 66)
print('\033[1;7m', ' ' * 10, 'O COMPUTADOR PENSOU EM UM NÚMERO DE 1 A 10', ' ' * 10, '\033[m')
print('\033[97;1m=\033[m' * 66)
numsort = randint(1, 10)
acertou = False
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    cont += 1
    if jogador == numsort:
        acertou = True
    else:
        if jogador < numsort:
            print('Mais...Tente Novamente')
        elif jogador > numsort:
            print('Menos...Tente Novamente')

print(f'Acertou em {cont} Palpites')