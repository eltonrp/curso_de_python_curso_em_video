from random import randint
print('=-' * 12)
print('Vamos Jogar PAR ou ÍMPAR')
print('=-' * 12)
cont = 0
while True:
    n = int(input('Diga um número: '))
    cpu = randint(0, 10)
    soma = n + cpu
    opção = ' '
    while opção not in 'PI':
        opção = str(input('PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print('=-' * 12)
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Você colocou {n}, o computador colocou {cpu}\nO total foi {soma}')
    print('Você escolheu PAR.' if opção == 'P' else 'Você escolheu ÍMPAR.', end=' ')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    print('=-' * 12)
    if opção == resultado:
        print('Você acertou, mais uma rodada...')
    else:
        break
    cont +=1
print('Você perdeu...')
print('***** GAME OVER *****')
print(f'Você ganhou {cont} veze(s)!!')
