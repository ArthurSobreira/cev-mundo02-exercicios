soma = 0
cont = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Você informou {cont} números e a soma deles é {soma}')
