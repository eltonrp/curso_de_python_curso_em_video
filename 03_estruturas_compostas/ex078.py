lista = list()
maior = menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print('='*40)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi: {maior}, nas posições ', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}... ', end='')
print()
print(f'O menor valor foi: {menor}, nas posições ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}... ', end='')
print()
