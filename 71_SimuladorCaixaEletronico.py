print('=' * 44)
print(' ' * 7, f'SIMULADOR DE CAIXA ELETÔNICO')
print('=' * 44)
val = int(input('Digite o valor que desja sacar: R$'))
ced_50 = val // 50
val %= 50
ced_20 = val // 20
val %= 20
ced_10 = val // 10
val %= 10
ced_1 = val // 1
val %= 1
if not ced_50 == 0:
    print(f'{ced_50} Notas de R$50,00')
if not ced_20 == 0:
    print(f'{ced_20} Notas de R$20,00')
if not ced_10 == 0:
    print(f'{ced_10} Notas de R$10,00')
if not ced_1 == 0:
    print(f'{ced_1} Notas de R$1,00')
print('=' * 44)
print('Fim do Programa')