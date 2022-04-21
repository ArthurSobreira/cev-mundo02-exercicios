while True:
    print('=' * 38)
    tab = int(input('Digite um Número para ver sua Tabuada: '))
    print('=' * 38)
    c = 1
    if tab < 0:
        break
    while c <= 10:
        print(f'{tab} * {c} = {tab * c} ')
        c += 1
print('Fim do Programa, Volte Sempre!!')
