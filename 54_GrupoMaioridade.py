import datetime

cont = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa:'))
    ida = datetime.date.today().year - ano
    if ida < 21:
        cont += 1
print(f'Dentre os mencionados {cont} são MENORES DE IDADE ')
print(f'Dentre os mencionados {7 - cont} são MAIORES DE IDADE')
