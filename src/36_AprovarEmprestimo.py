import time

print('\033[97;1m=\033[m' * 43)
print('\033[1;7m', ' ' * 10, 'Empréstimo Bancário', ' ' * 10, '\033[m')
print('\033[97;1m=\033[m' * 43)
ValC = float(input('\033[97;1mDigite o Valor do Imóvel:\033[m R$'))
print('\033[97;1m=\033[m' * 43)
SalC = float(input('\033[97;1mDigite sua Renda Salarial:\033[m R$'))
print('\033[97;1m=\033[m' * 43)
QuantA = int(input('\033[97;1mDigite (em anos) o Tempo de Parcelamento:\033[m'))
print('\033[97;1m=\033[m' * 43)
Prest = ValC / (QuantA * 12)
Porc = SalC * 0.30
print('\033[34mProcessando...\033[m')
time.sleep(2)
if Prest <= Porc:
    print(f'\033[32;1mO Valor a Ser Pago Será de \033[m\033[97m{Prest:.2f}\033[m\033[32;1m ao Mês.\033[m')
    print('\033[32;1;40mEmpréstimo Concedido!!\033[m')
elif Prest > Porc:
    print(f'\033[31;1mNão é possível realizar o Empréstimo, uma vez que o Valor da Parcela\033[m \033[97m(R$ '
          f'{Prest:.2f}/Mês) \033[m'
          f'\033[31;1mRepresenta mais de 30% da sua Renda Mensal de\033[m \033[97mR${SalC:.2f}\033[m')
    print('\033[31;1;40mEmpréstimo Negado!!\033[m')
