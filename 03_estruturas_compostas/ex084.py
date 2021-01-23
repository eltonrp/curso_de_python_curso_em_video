lista = []
cadastro = []
maior = menor = 0
while True:
    cadastro.append(str(input('Digite o nome: ')))
    cadastro.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    lista.append(cadastro[:])
    cadastro.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').strip().upper()[0])
        if continuar not in 'SN':
            print('Opção inválida, tente novamente...')
    if continuar in 'N':
        break
print('-'*30)
print(f'Foram cadastradas {len(lista)} pessoas: ')
print('-'*30)
for e in lista:
    print(f'Nome: {e[0].title()}')
    print(f'Peso: {e[1]:.2f} kg')
    print('-'*30)
print('Os maiores pesos foram: ', end='')
for e in lista:
    if maior == e[1]:
        print(f'[{e[0].title()}] ', end='')
print(f'com {maior:.2f} kg.')
print('Os menores pesos foram: ', end='')
for e in lista:
    if menor == e[1]:
        print(f'[{e[0].title()}] ', end='')
print(f'com {menor:.2f} kg.')
