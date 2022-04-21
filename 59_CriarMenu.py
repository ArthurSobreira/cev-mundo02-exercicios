from time import sleep
n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
esc = 0
while esc != 5:
    print('''
[ 1 ] Se deseja Somar
[ 2 ] Se deseja Multiplicar
[ 3 ] Se deseja ver qual é o Maior
[ 4 ] Se deseja selecionar Novos Números
[ 5 ] Se deseja sair do programa''')
    print('')
    esc = int(input('Digite sua escolha: '))
    print('=' * 30)
    if esc == 1:
        print(f'A soma entre {n1} + {n2} é igual a {n1 + n2}')
    elif esc == 2:
        print(f'A multiplicação entre {n1} * {n2} é {n1 * n2}')
    elif esc == 3:
        if n1 > n2:
            print(f'Dentre os dois, {n1} é o maior')
        elif n1 == n2:
            print('Os dois números são iguais')
        else:
            print(f'Dentre os dois, {n2} é o maior')
    elif esc == 4:
        print('Informe os Números Novamente')
        n1 = int(input('Digite o Primeiro Número: '))
        n2 = int(input('Digite o Segundo Número: '))
    elif esc == 5:
        print('')
    else:
        print('Opção Inválida, Tente Novamente!')
    sleep(3)
print('Fim do Programa, Volte sempre!!')
