c = 1
num = int(input('Digite um Número para fatorar: '))
while num >= 1:
    c *= num
    num = num - 1
print(f'O factorial é {c}')

num = int(input('Digite um Número para fatorar: '))
c = 1
for num in range(num, 0, -1):
    c *= num
print(f'O fatorial é {c}')




