num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
escolha = int((input('Sua opção: ')))
if escolha == 1:
    print('{} convertido em binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido em octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha INCORRETA')
