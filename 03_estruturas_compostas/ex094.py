perfil = {}
lista = []
soma = média = 0
while True:
    perfil['nome'] = str(input('Nome: ')).strip().title()
    while True:
        perfil['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if perfil['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F')
    perfil['idade'] = int(input('Idade: '))
    soma += perfil['idade']
    lista.append(perfil.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Digite S ou N')
    if continua in 'N':
        break
print('-' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
média = soma/len(lista)
print(f'B) A média da idade foi {média:5.2f} anos')
print('C) As mulheres cadastradas foram: ')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ')
print('-' * 30)
print(f'D) Pessoas acima da média:')
for p in lista:
    if p['idade'] > média:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
