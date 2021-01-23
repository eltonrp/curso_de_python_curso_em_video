cont = total = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    total += n
    n = int(input('Digite um número [999 para parar]: '))
print('Finalizando com {} números, totalizando {}'.format(cont, total))
