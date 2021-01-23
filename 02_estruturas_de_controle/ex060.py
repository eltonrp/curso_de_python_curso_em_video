# from math import factorial >>>> jeito mais fácil
n1 = -1
while n1 <= 0:
    n1 = int(input('Qual número deseja calcular o fatorial? '))
    if n1 <= 0:
        print('Digite um número inteiro maior que 0...')
    n2 = n1
    f = 1
print('{}! = '.format(n1), end='')
while n2 > 0:
    print('{}'.format(n2), end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    f *= n2
    n2 -= 1
print('{}'.format(f))
