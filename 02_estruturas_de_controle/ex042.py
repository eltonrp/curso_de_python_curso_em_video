r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os sementos formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os Sementos NÃO FORMAM um triângulo')

#if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    #print('Os Sementos NÃO FORMAM um triângulo')
#elif r1 == r2 == r3:
    #print('Os sementos formam um triângulo do tipo EQUILÁTERO')
#elif r1 != r2 and r1 != r3 and r2 != r3:
    #print('Os segmentos formam um triângulo ESCALENO')
#else:
    #print('Os sementos formam um triângulo ISÓCELES')