soma = cont = 0
while True:
    num = int(input('Digite um Número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} Números que você digitou é {soma}')
