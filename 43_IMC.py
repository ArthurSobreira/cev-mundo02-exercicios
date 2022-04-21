print('\033[97;1m=\033[m' * 24)
print('\033[7;1mÍndice de Massa Corporal\033[m')
print('\033[97;1m=\033[m' * 24)
peso = float(input('\033[27;1mDigite seu Peso (em quilos):\033[m'))
alt = float(input('\033[27;1mDigite sua Altura (em metros):\033[m'))
imc = peso / (alt * alt)
print(f'\033[34mSeu IMC é de {imc:.1f}\033[m')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('\033[31mPESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[31mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[31mOBESIDADE\033[m')
else:
    print('\033[31mOBESIDADE MÓRBIDA\033[m')
