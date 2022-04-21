num = int(input('Digite um Número: '))
cont = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
quant = soma = med = 0
num1 = num
men = num1 #Menor Número
man = num1 #Maior Número
while cont != 'N':
    num = int(input('Digite um Número: '))
    cont = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
    if num > num1:
        man = num
    if num > man:
        man = num
    if num < num1:
        men = num
    if num < men:
        men = num
    quant += 1
    soma += num
    med = (soma + num1) / (quant + 1)
print(f'A Média dos {quant + 1} números que você digitou é {med}')
print(f'Dentre os valores que você digitou, {man} é o Maior, e {men} é o Menor')
