print('=' * 22)
print('Sequência de Fibonacci')
print('=' * 22)
quant = int(input('Digite quantos termos deseja ver: '))
pri_Termo = 0
seg_Termo = 1
print(f'{pri_Termo} - {seg_Termo} - ', end='')
c = 0
while c <= quant:
    ter_Termo = pri_Termo + seg_Termo
    print(f'{ter_Termo} - ', end='')
    pri_Termo = seg_Termo
    seg_Termo = ter_Termo
    c += 1
print('Fim')
