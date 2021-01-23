p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dez = p + (10 - 1) * r
while p < dez:
    print('{} → '.format(p), end='')
    p += r
print('{}'.format(p), end=' → ACABOU')