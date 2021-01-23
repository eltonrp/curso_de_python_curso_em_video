def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} fez {gols} gols no campeonato')


n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
