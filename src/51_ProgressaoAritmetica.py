a1 = int(input('Digite o primeiro termo da P.A:'))
r = int(input('Digite a Razão da P.A:'))
décimo = a1 + (10 - 1) * r
print('Os 10 primeiros termos da PA são')
for c in range(a1, décimo + r, r):
    print(c, end=' - ')
print('Acabou!')
