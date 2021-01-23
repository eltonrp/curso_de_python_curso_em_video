print('-' * 50)
print('{:^50}'.format(' Banco GEV '))
print('-' * 50)
valor = int(input('Quanto deseja sacar? R$ '))
total = valor
cédula = 50
totalcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'{totalcéd} cédulas de {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcéd = 0
        if total == 0:
            break
print('-' * 50)
print('{:^50}'.format(' Obrigado por utilizar o Banco GEV, Volte Sempre!! '))
print('-' * 50)
