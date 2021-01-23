n1 = int(input('Qual número deseja calcular o fatorial? '))
n2 = n1
f = 1
print('{}! = '.format(n1), end='')
for c in range(1, n1 + 1):
    print('{}'.format(n2), end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    f *= n2
    n2 -= 1
print('{}'.format(f))
