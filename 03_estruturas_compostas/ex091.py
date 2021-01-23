from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = []
print('-' * 30)
print(f'{"Valores sorteados:":^30}')
print('-' * 30)
for k, v in jogos.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-' * 30)
for k, v in enumerate(ranking):
    print(f'Em {k+1}º ficou {v[0]} com valor {v[1]}')
