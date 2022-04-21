import random

cont_vit = 0
while True:
    print('')
    print('\033[97;1m=\033[m' * 36)
    print('\033[1;7m', ' ' * 10, 'ÍMPAR OU PAR', ' ' * 10, '\033[m')
    print('\033[97;1m=\033[m' * 36)

    num = int(input('Digite um Valor: '))
    par_impar = str(input('Par ou Ímpar?[P/I]: ')).strip().upper()[0]
    pc = random.randint(0, 10)
    resul = num + pc
    print('~' * 36)
    print(f'Você jogou {num} e o computador jogou {pc}')
    print('~' * 36)
    if par_impar == 'P':
        if resul % 2 == 0:
            print('\033[32mMeus Parabéns, Você Venceu!!\033[m')
            cont_vit += 1
        else:
            print('\033[31mVocê Perdeu!!\033[m, ', end='')
            break
    if par_impar == 'I':
        if resul % 2 != 0:
            print('\033[32mMeus Parabéns, Você Venceu!!\033[m')
            cont_vit += 1
        else:
            print('\033[31mVocê Perdeu!!\033[m, ', end='')
            break

print(f'Fim de Jogo, Você venceu {cont_vit} vezes')
