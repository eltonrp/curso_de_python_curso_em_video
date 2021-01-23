num = int(input('\033[34mMe diga um número qualquer: \033[m'))
print('O número escolhido foi: \033[34m{}\033[m!!'.format(num))
res = num % 2
if res == 0:
    print('O número escolhido é {}{}{}'.format('\033[34m', 'PAR', '\033[m'))
else:
    print('O número escolhido é {}'.format('\033[31mÍMPAR'))
