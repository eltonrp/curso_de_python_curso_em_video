ficha = {}
ficha['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou: '))
gols = []
for n in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {n+1}: ')))
ficha['gols'] = gols
ficha['total'] = sum(gols)
print('-' * 30)
print(ficha)
print('-' * 30)
for k, v in ficha.items():
    print(f'{k} = {v}')
print('-' * 30)
print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])} partidas')
for i, v in enumerate(ficha['gols']):
    print(f'   => Na partida {i+1} fez {v} gols')
print(f'Foi um total de {ficha["total"]} gols')
