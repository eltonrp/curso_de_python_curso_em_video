def area():
    l = float(input('LARGURA (m): '))
    c = float(input('Comprimento (m): '))
    a = l * c
    print(f'{"-"*30}\n{"Dimensões do terreno":^30}\n{"-"*30}\n'
          f'Largura: {l:.2f}m\n'
          f'Comprimento: {c:.2f}m\n'
          f'Área: {a:.2f}m²')


from time import sleep
print('-' * 30)
print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
area()
sleep(1)
print('Finalizando...')
sleep(2)
print('-' * 30)
print(f'{"Programa Finalizado":^30}')
print('-' * 30)
