import datetime

print('\033[97;1m=\033[m' * 19)
print('\033[32;1;40mAlistamento Militar\033[m')
print('\033[97;1m=\033[m' * 19)
print('''\033[32;1mDigite seu sexo:\033[m
[ \033[31;1m1\033[m ] Para Masculino
[ \033[31;1m2\033[m ] Para Feminino''')
sex = int(input('\033[32;1mSua Escolha:\033[m'))
if sex == 2:
    print('\033[31;1;40mComo sendo do sexo Feminino, não é obrigatório a sua alistação\033[m')

if sex == 1:
    nasc = int(input('\033[32;1mDigite seu ano Nascimento:\033[m'))
    ida = datetime.date.today().year - nasc
    print('\033[97;1m=\033[m' * 30)
    print(f'\033[97;1mSua idade é de {ida} anos.\033[m')
    if ida < 18:
        falt = 18 - ida
        print(f'\033[97;1mFaltam {falt} anos para você se alistar.\033[m')
        print(f'\033[97;1mSeu alistamento será no ano de {nasc + 18}.\033[m')
    elif ida == 18:
        print(f'\033[97;1mEstá no ano de alistação.\033[m')
    elif ida > 18:
        pas = ida - 18
        print(f'\033[97;1mPassaram-se {pas} anos do seu alistamento.\033[m')
