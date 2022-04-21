from datetime import date

ano = int(input('Digite o ano de nascimento do atleta:'))
ida = date.today().year - ano
print(f'O atleta possui {ida} anos.')
if ida <= 9:
    print('O atleta é Mirim.')
elif ida <= 14:
    print('O atleta é Infatil.')
elif ida <= 19:
    print('O atleta é Junior.')
elif ida <= 25:
    print('O atleta é Sênior.')
else:
    print('O atleta é Master.')
