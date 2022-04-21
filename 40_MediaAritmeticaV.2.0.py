not1 = float(input('Digite sua primeira nota:'))
not2 = float(input('Digite sua segunda nota:'))
med = (not1 + not2) / 2
print(f'\033[32mSua média foi de {med}\033[m')
if med >= 7:
    print('\033[34mO aluno está APROVADO!\033[m')
elif med >= 5 < 7:
    print('\033[33mO aluno está de RECUPERAÇÃO\033[m')
elif med < 5:
    print('\033[31mO aluno está REPROVADO\033[m')
