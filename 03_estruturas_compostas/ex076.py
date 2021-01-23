print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 2.62,
         'Borracha', 1.25,
         'Caderno', 15.75,
         'Estojo', 4.99,
         'Transferidor', 6.60,
         'Compasso', 9.99,
         'Mochila', 125.90,
         'Canetas', 22.30,
         'Livros', 34.90)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-'*40)
