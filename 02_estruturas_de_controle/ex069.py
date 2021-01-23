maior18 = menor20 = homens = 0
while True:
    print('-' * 22)
    print(' CADASTRE UMA PESSOA ')
    print('-' * 22)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Opção inválida, tente novamente...')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 22)
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        menor20 += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida, tente novamente...')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas maior de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homem(ens) cadastrado(s)')
print(f'E temos {menor20} mulher(es) menor(es) de 20 anos')
