cont = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1     # ou cont += 1
        n = n + c           # ou n += c
print('Foram encontrados {} valores e a soma deles é {}'.format(cont, n))
