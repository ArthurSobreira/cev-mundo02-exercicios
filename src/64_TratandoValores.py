num = int(input('Digite um valor (999 para parar): '))
c = 0
cont = 0
soma = 0
while num != 999:
    c += 1
    cont += 1
    soma += num
    num = int(input('Digite um Valor (999 para parar): '))
print(f'Você digitou {cont} números, e a soma deles é {soma}')
