t = []
for c in range(1, 6):
    p = float(input(f'Peso da {c} pessoa:(kg) '))
    t += [p]
print(f'O maior peso foi {max(t)}kg\n'
      f'O menor peso foi {min(t)}kg')
