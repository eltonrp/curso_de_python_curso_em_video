from time import sleep


def maior(* num):
    cont = maior = 0
    print('-' * 35)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Nenhum valor passado')
    else:
        for valor in num:
            print(f'{valor}', end='')
            sleep(0.3)
            print(', ' if cont < len(num)-1 else '', end='')
            sleep(0.5)
            if cont == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            cont += 1
        print(f'\nForam informados {cont} valores.')
        sleep(1)
        print(f'O maior valor passado foi: {maior}.')


maior(100, 80, 2, 1034)
maior(1, 3)
maior(-5, -2, -1)
maior()
