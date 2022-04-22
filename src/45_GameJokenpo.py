from random import *
from time import *


def apart(msg):
    size = 39
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def animation():
    print('JO...', end='')
    sleep(1)
    print('KEN...', end='')
    sleep(1)
    print('PO!!!', end='\n')


def machine():
    return choice([1, 2, 3])


def user():
    while True:
        try:
            choi = int(input('Digite sua escolha: '))
        except (ValueError, TypeError):
            print('\033[31mEntrada inválida, Tente Novamente!\033[m')
            continue
        else:
            if choi in range(1, 4):
                return choi
            else:
                print('\033[31mEntrada inválida, Tente Novamente!\033[m')


def win(user_play, machine_play):
    if user_play == 1:
        user_play = 'Pedra'
        if machine_play == 1:
            machine_play = 'Pedra'
            print('Empate', end=', ')
        if machine_play == 2:
            machine_play = 'Papel'
            print('Derrota', end=', ')
        if machine_play == 3:
            machine_play = 'Tesoura'
            print('Vitória', end=', ')

    if user_play == 2:
        user_play = 'Papel'
        if machine_play == 1:
            machine_play = 'Pedra'
            print('Vitória', end=', ')
        if machine_play == 2:
            machine_play = 'Papel'
            print('Empate', end=', ')
        if machine_play == 3:
            machine_play = 'Tesoura'
            print('Derrota', end=', ')

    if user_play == 3:
        user_play = 'Tesoura'
        if machine_play == 1:
            machine_play = 'Pedra'
            print('Derrota', end=', ')
        if machine_play == 2:
            machine_play = 'Papel'
            print('Vitória', end=', ')
        if machine_play == 3:
            machine_play = 'Tesoura'
            print('Empate', end=', ')

    print(f'Você escolheu {user_play} e o computador escolheu {machine_play}.')


def main():
    apart('Bem Vindo ao Jogo da Velha!')
    print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
    print()
    user_choice = user()
    machine_choice = machine()
    print()
    animation()
    print()
    win(user_choice, machine_choice)


if __name__ == '__main__':
    main()
