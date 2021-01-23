valores = [[], []]
for v in range(7):
    num = (int(input(f'Digite o {v+1}º valor: ')))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares foram: {valores[0]}\n'
      f'E os valores ímpares foram: {valores[1]}')
