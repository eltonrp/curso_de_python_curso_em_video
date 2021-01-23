jogador = {}
time = []
gols = []
while True:
    gols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for q in range(partidas):
        gols.append(int(input(f'  Quantos gols na partida {q+1}: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Digite S ou N')
    if continua == 'N':
        break
print()
print('-' * 40)
print(f'{"Cód. ":<5}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, v in enumerate(time):
    print(f'{i:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? [999] para parar: '))
    if mostrar == 999:
        break
    if mostrar in range(0, len(time)):
        print('-' * 40)
        print(f'--> Levantamento do jogador {time[mostrar]["Nome"]}:')
        for p in range(len(time[mostrar]['Gols'])):
           print(f'  No jogo {p+1} fez {time[mostrar]["Gols"][p]} gols')
        print('-' * 40)
    else:
        print('ERRO! Digite um código de jogador válido...')
print()
print('------- ENCERRADO --------')
