p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
décimo = p + (10 - 1) * r
for c in range(p, décimo + r, r):
    print('{}'.format(c), end=' → ')
print('ACABOU')
