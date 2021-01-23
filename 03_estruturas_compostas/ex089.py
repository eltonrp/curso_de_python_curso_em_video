lista = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, nota1, nota2])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if continua not in 'SN':
            print('Dados inválidos, tente novamente...')
    if continua == 'N':
        break
print('-' * 30)
print(f'{"Nº":<3}{"Nome":^19}{"Média":>8}')
print('-' * 30)
for pos, c in enumerate(lista):
    print(f'{pos:<3}{c[0]:<19}{(c[1] + c[2])/2:>8.2f}')
print('-' * 30)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if mostrar == 999:
        break
    elif mostrar not in range(0, len(lista)):
        print('Aluno não cadastrado...')
    else:
        print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1]:.2f} e {lista[mostrar][2]:.2f}')
print('-' * 30)
print(f'{"FIM DO PROGAMA":^30}')
print('-' * 30)
