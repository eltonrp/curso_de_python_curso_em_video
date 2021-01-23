print('\033[31m-=' * 20)
print('{:^50}'.format('\033[33mAnalisador de Triângulos\033[m'))
print('\033[31m-=\033[m' *20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos \033[34mFORMAM UM TRIÂNGULO')
else:
    print('Os segmentos \033[31mNÃO FORMAM UM TRIÂNGULO')
