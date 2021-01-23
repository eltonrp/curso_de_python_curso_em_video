lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ').strip().upper()[0])
        if r not in 'SN':
            print('Opção incorreta...')
    if r in 'N':
        break
for pos, e in enumerate(lista):
    if e % 2 == 0:
        pares.append(e)
    else:
        ímpares.append(e)
lista.sort()
print(f'Valores digitados: {lista}')
if pares == []:
    print('Não foram digitados valores pares!!!')
else:
    print(f'Os valores pares foram: {pares}')
if ímpares == []:
    print('Não foram digitados valores ímpares!!!')
else:
    print(f'Os valores ímpares foram: {ímpares}')
