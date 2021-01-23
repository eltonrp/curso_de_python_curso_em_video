total = maismil = cont = preçobarato = 0
maisbarato = ' '
print('-' * 30)
print('{:^30}'.format('LOJAS DO POVÃO'))
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        maismil += 1
    if cont == 1 or preço < preçobarato:
        maisbarato = produto
        preçobarato = preço
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi: R$ {total:.2f}')
print(f'Temos {maismil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {maisbarato}, custando R$ {preçobarato:.2f}')
