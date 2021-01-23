lista = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',\
        'dezenove', 'vinte'

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente...', end=' ')
    else:
        print(f'Você escolheu o número: {lista[n].capitalize()}')
        continua = ' '
        while continua not in 'SN':
            continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continua == 'N':
            break
print('Volte Sempre!!!')
