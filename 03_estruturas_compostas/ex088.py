from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{" Palpites da Mega Sena ":^30}')
print('-' * 30)
quantidade = int(input('Digite o número de jogos: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 30)
print(f'{" Jogos Sorteados ":^30}')
print('-' * 30)
print()
sleep(2)
for j in range(quantidade):
    print(f'{j+1}º jogo: {jogos[j]}')
    sleep(1)
print(f'\n{" Boa Sorte!!!! ":-^30}')
