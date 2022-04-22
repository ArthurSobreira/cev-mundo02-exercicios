f = str(input('Digite uma frase:')).replace(' ', '').upper()
fc = f[::-1]
if f == fc:
    print(f'A frase {f} representa um palíndromo, pois ao contrário é {fc}')
else:
    print(f'A frase {f} não representa um palíndromo, pois ao contrário é {fc}')
