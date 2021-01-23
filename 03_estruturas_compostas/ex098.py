from time import sleep


def contagem(a, b, c):
    print('-' * 30)
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if c == 0:
        c = 1
    sleep(2)
    if a > b:
        for n in range(a, b-1, -abs(c)):
            sleep(0.5)
            print(n, end=' ')
        print('FIM!')
    else:
        for n in range(a, b+1, abs(c)):
            sleep(0.5)
            print(n, end=' ')
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim:    '))
z = int(input('Passo:  '))
contagem(x, y, z)
