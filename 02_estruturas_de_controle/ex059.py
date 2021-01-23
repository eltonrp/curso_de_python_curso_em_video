from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('>>>> Qual opção deseja? '))
    if opção == 1:
        print('A soma {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('A multiplicação {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif opção == 4:
        print('Digite novos valores')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('\033[31mOpção inválida, tente novamente...\033[m')
print('{:*^40}'.format(' FIM DO PROGRAMA!!! '))
