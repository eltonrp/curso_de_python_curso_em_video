times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo',
         'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
         'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')
print('-=' * 12)
print('TABELA DE CLASSIFICAÇÃO')
print('-=' * 12)
for t in range(0, len(times)):
    print(f'{t+1}º -', times[t])
'''for pos, t in enumerate(times):
    print(pos+1, end='')
    print('º - ', end='')
    print(t)'''
print('-=' * 12)
print('Os cinco primeiros são:')
print('-=' * 12)
for t in times[0:5]:
    print(t)
print('-=' * 12)
print('Os quatro últimos são:')
print('-=' * 12)
for t in times[-4:]:
    print(t)
print('-=' * 12)
print(f'Times em ordem alfabética:')
print('-=' * 12)
for t in sorted(times):
    print(t)
print('-=' * 12)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª Posição')
print('-=' * 12)
