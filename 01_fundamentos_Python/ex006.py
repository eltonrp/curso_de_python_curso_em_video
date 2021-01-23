from math import sqrt
n = int(input('Digite um número: '))
print('Você digitou: {}'.format(n))
print('Tripo: {}'.format(n*3))
print('Raíz quadrada: {}'.format(n**(1/2)), end=' ')
print('Raíz quadrada: \033[46m{}\033[m'.format(sqrt(n)))
