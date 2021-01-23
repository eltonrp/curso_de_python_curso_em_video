lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ').strip().upper()[0])
        if r not in 'SN':
            print('Resposta inválida...')
    if r == 'N':
        break
lista.sort(reverse = True)
print('='*40)
print(f'Você digitou {len(lista)} elementos!!')
print(f'Os valores digitados em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO faz parte da lista')
