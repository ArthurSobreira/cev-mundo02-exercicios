num = int(input('Digite o Primeiro Termo da P.A: '))
r = int(input('Digite a Razão da P.A: '))
quant = 1
a1 = num
while quant <= 10:
    print(f'| {a1} ', end=' | ')
    a1 += r
    quant += 1
