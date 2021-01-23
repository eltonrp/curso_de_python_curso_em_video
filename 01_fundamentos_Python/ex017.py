from math import hypot
a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
h = hypot(a, b)
print('A hipotenusa é: {}'.format(h))
