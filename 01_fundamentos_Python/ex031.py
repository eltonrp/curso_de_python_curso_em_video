dist = float(input('Qual a distâcia da viagem: '))
'''if dist <= 200:
    print('Para a distância de \033[34m{:.2f}\033[m km, o valor da passagem é de '
          'R$ \033[31m{:.2f}\033[m'.format(dist, dist*0.50))
else:
    print('Para a distâcia de \033[34m{:.2f}\033[m km, o valor da passagem é de '
          'R$ \033[31m{:.2f}'.format(dist, dist*0.45))'''
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('A viagem será de R$ \033[34m{:.2f}'.format(preço))

