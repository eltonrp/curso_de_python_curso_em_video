lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor já presente na lista, tente outro valor...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso!!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').strip().upper()[0])
        if continuar not in 'SN':
            print('Dados inválidos, tente novamente...')
    if continuar == 'N':
        break
lista.sort()
print('='*40)
print(f'Você digitou os valores {lista}')
