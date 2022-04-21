num = int(input('Digite o Primeiro Termo da P.A: '))
r = int(input('Digite a Razão da P.A: '))
quant = 1
a1 = num
mais = 5
tot = 0
while mais != 0:
    tot += mais
    while quant <= tot:
        print(f'| {a1} ', end=' | ')
        a1 += r
        quant += 1
    mais = int(input('\nQuantos termos a mais você quer mostrar: '))
print('Acabou!!!')
